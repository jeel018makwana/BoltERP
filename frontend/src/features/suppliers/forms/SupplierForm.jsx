import { supplierSchema } from "../schema/supplierSchema";
import { useCreateSupplier } from "../hooks/useCreateSupplier";
import { useUpdateSupplier } from "../hooks/useUpdateSupplier";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

export default function SupplierForm({
    supplier,
    onSuccess,
}) {
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors },
    
    } = useForm({
        resolver: zodResolver(supplierSchema),
        defaultValues: {
            supplier_code: supplier?.supplier_code || "",
            name: supplier?.name || "",
            company_name: supplier?.company_name || "",
            phone: supplier?.phone || "",
            email: supplier?.email || "",
            gst_number: supplier?.gst_number || "",
            address: supplier?.address || "",
        },
    });
    const updateMutation = useUpdateSupplier();
    const { mutateAsync, isPending } =
        useCreateSupplier();

    const onSubmit = async (data) => {
        if (supplier) {
            await updateMutation.mutateAsync({
            id: supplier.id,
            data,
            });
        } else {
            await mutateAsync(data);
        }

        reset();

        onSuccess?.();
    };

    return (
        <form
        onSubmit={handleSubmit(onSubmit)}
        className="space-y-6"
        >
        <div className="grid grid-cols-2 gap-4">

            <div>
            <Input
                placeholder="Supplier Code"
                {...register("supplier_code")}
            />
            <p className="text-sm text-red-500">
                {errors.supplier_code?.message}
            </p>
            </div>

            <div>
            <Input
                placeholder="Supplier Name"
                {...register("name")}
            />
            <p className="text-sm text-red-500">
                {errors.name?.message}
            </p>
            </div>

            <div>
            <Input
                placeholder="Company Name"
                {...register("company_name")}
            />
            </div>

            <div>
            <Input
                placeholder="Phone"
                {...register("phone")}
            />
            <p className="text-sm text-red-500">
                {errors.phone?.message}
            </p>
            </div>

            <div>
            <Input
                placeholder="Email"
                {...register("email")}
            />
            <p className="text-sm text-red-500">
                {errors.email?.message}
            </p>
            </div>

            <div>
            <Input
                placeholder="GST Number"
                {...register("gst_number")}
            />
            </div>

        </div>

        <div>
            <Textarea
            rows={4}
            placeholder="Address"
            {...register("address")}
            />
        </div>

        <div className="flex justify-end gap-2">

            <Button
            type="button"
            variant="outline"
            onClick={onSuccess}
            >
            Cancel
            </Button>

            <Button
            type="submit"
            disabled={isPending || updateMutation.isPending}
            >
            {supplier
                ? "Update Supplier"
                : "Save Supplier"}
            </Button>

        </div>
        </form>
    );
    }