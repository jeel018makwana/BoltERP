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

export default function SupplierViewDialog({
  open,
  onOpenChange,
  supplier,
}) {
  if (!supplier) return null;

  return (
    <Dialog
      open={open}
      onOpenChange={onOpenChange}
    >
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>
            Supplier Details
          </DialogTitle>
        </DialogHeader>

        <div className="space-y-1">

          <Row
            label="Supplier Code"
            value={supplier.supplier_code}
          />

          <Row
            label="Supplier Name"
            value={supplier.name}
          />

          <Row
            label="Company Name"
            value={supplier.company_name}
          />

          <Row
            label="Phone"
            value={supplier.phone}
          />

          <Row
            label="Email"
            value={supplier.email}
          />

          <Row
            label="GST Number"
            value={supplier.gst_number}
          />

          <Row
            label="Address"
            value={supplier.address}
          />

          <Row
            label="Opening Balance"
            value={new Intl.NumberFormat("en-IN", {
              style: "currency",
              currency: "INR",
            }).format(supplier.opening_balance)}
          />

          <Row
            label="Status"
            value={
              supplier.is_active
                ? "🟢 Active"
                : "🔴 Inactive"
            }
          />

        </div>
      </DialogContent>
    </Dialog>
  );
}