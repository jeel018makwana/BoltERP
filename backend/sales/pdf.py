from io import BytesIO

from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def generate_invoice(sale):

    buffer = BytesIO()

    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(180, 800, "BoltERP Invoice")

    p.setFont("Helvetica", 12)

    p.drawString(50, 760, f"Invoice No : {sale.sale_number}")
    p.drawString(50, 740, f"Date : {sale.sale_date}")

    p.drawString(50, 710, f"Customer : {sale.customer.name}")

    y = 670

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

    p.save()

    pdf = buffer.getvalue()

    buffer.close()

    return pdf