import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";

function Row({ label, value }) {
  return (
    <div className="grid grid-cols-2 border-b py-3">
      <span className="text-muted-foreground">
        {label}
      </span>

      <span className="font-medium">
        {value || "-"}
      </span>
    </div>
  );
}

export default function CustomerViewDialog({
  open,
  onOpenChange,
  customer,
}) {
  if (!customer) return null;

  return (
    <Dialog
      open={open}
      onOpenChange={onOpenChange}
    >
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>
            Customer Details
          </DialogTitle>
        </DialogHeader>

        <div className="space-y-1">

          <Row
            label="Customer Code"
            value={customer.customer_code}
          />

          <Row
            label="Customer Name"
            value={customer.name}
          />

          <Row
            label="Company Name"
            value={customer.company_name}
          />

          <Row
            label="Phone"
            value={customer.phone}
          />

          <Row
            label="Email"
            value={customer.email}
          />

          <Row
            label="GST Number"
            value={customer.gst_number}
          />

          <Row
            label="Address"
            value={customer.address}
          />

          <Row
            label="Opening Balance"
            value={new Intl.NumberFormat("en-IN", {
              style: "currency",
              currency: "INR",
            }).format(customer.opening_balance)}
          />

          <Row
            label="Status"
            value={
              customer.is_active
                ? "🟢 Active"
                : "🔴 Inactive"
            }
          />

        </div>
      </DialogContent>
    </Dialog>
  );
}