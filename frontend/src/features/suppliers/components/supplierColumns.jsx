import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-react";
import SupplierRowActions from "./SupplierRowActions";
export const supplierColumns = [
  {
    accessorKey: "supplier_code",
    header: "Code",
  },
  {
    accessorKey: "name",
    header: "Supplier",
  },
  {
    accessorKey: "phone",
    header: "Phone",
  },
  {
    accessorKey: "email",
    header: "Email",
    cell: ({ row }) =>
        row.original.email || "-",
    },
  {
    accessorKey: "opening_balance",
    header: "Balance",
    cell: ({ row }) => {
        return new Intl.NumberFormat("en-IN", {
        style: "currency",
        currency: "INR",
        }).format(row.original.opening_balance);
    },
   },
   {
    id: "actions",
    header: "Actions",
    cell: ({ row }) => (
        <SupplierRowActions
        supplier={row.original}
        onView={row.original.onView}
        onEdit={row.original.onEdit}
        onDelete={row.original.onDelete}
        />
    ),
    },
];