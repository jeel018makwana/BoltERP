from io import BytesIO
from company.models import Company
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from num2words import num2words

def generate_invoice(sale):
    company = Company.objects.first()
    buffer = BytesIO()

    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(170, 810, company.name)

    p.setFont("Helvetica", 10)
    p.drawString(50,790, company.address)
    p.drawString(50,775, f"Phone: {company.phone}")
    p.drawString(250,775, f"Email: {company.email}")
    p.drawString(50,760, f"GSTIN: {company.gst_number}")
    p.line(40,750,550,750)
    p.setFont("Helvetica-Bold",12)

    p.drawString(50, 730, f"Invoice No : {sale.sale_number}")
    p.drawString(320, 730, f"Date : {sale.sale_date}")

    customer = sale.customer
    p.setFont("Helvetica-Bold",12)
    p.drawString(50,700, "Bill To")
    p.setFont("Helvetica", 10)
    p.drawString(50,680,customer.name)
    p.drawString(50,665,customer.phone)
    p.drawString(50,650,customer.address)
    p.drawString(50,635, f"GST: {customer.gst_number}")

    y = 600

    p.drawString(50, y, "Product")
    p.drawString(250, y, "Qty")
    p.drawString(320, y, "Rate")
    p.drawString(420, y, "Total")

    y -= 25

    for item in sale.items.all():

        p.drawString(50, y, item.product.name)

        p.drawString(250, y, str(item.quantity))

        p.drawString(320, y, str(item.selling_price))

        p.drawString(420, y, str(item.line_total))

        y -= 20

    y -= 20

    p.drawString(320, y, "Grand Total")

    p.drawString(430, y, str(sale.grand_total))
    
    y -= 40

    amount_words = num2words(
        sale.grand_total,
        lang="en_IN"
    )

    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, y, "Amount in Words:")

    y -= 15

    p.setFont("Helvetica", 10)
    p.drawString(
        50,
        y,
        amount_words.title() + " Rupees Only"
    )
    y -= 40

    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, y, "Bank Details")

    y -= 15

    p.setFont("Helvetica", 10)
    p.drawString(50, y, "Bank : State Bank of India")

    y -= 15
    p.drawString(50, y, "A/C No : 1234567890")

    y -= 15
    p.drawString(50, y, "IFSC : SBIN0001234")

    p.line(420, y + 20, 540, y + 20)

    p.drawString(
        425,
        y,
        "Authorized Signatory"
    )

    p.setFont("Helvetica-Oblique", 9)

    p.drawCentredString(
        300,
        30,
        "Thank you for your business!"
    )

    p.save()

    pdf = buffer.getvalue()

    buffer.close()

    return pdf