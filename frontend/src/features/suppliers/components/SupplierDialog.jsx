import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";

import SupplierForm from "../forms/SupplierForm";

export default function SupplierDialog({
  open,
  onOpenChange,
  supplier,
}) {
  return (
    <Dialog
      open={open}
      onOpenChange={onOpenChange}
    >
      <DialogContent className="max-w-3xl">
        <DialogHeader>
          <DialogTitle>
            {supplier ? "Edit Supplier" : "Add Supplier"}
          </DialogTitle>
        </DialogHeader>

        <SupplierForm
          supplier={supplier}
          onSuccess={() => onOpenChange(false)}
        />
      </DialogContent>
    </Dialog>
  );
}