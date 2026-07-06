import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { customerSchema } from "../schema/customerSchema";
import { useCreateCustomer } from "../hooks/useCreateCustomer";
import { useUpdateCustomer } from "../hooks/useUpdateCustomer";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

export default function CustomerForm({
    customer,
    onSuccess,
}) {
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors },
    
    } = useForm({
        resolver: zodResolver(customerSchema),
        defaultValues: {
            customer_code: customer?.customer_code || "",
            name: customer?.name || "",
            company_name: customer?.company_name || "",
            phone: customer?.phone || "",
            email: customer?.email || "",
            gst_number: customer?.gst_number || "",
            address: customer?.address || "",
        },
    });
    const updateMutation = useUpdateCustomer();
    const { mutateAsync, isPending } =
        useCreateCustomer();

    const onSubmit = async (data) => {
        if (customer) {
            await updateMutation.mutateAsync({
            id: customer.id,
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
                placeholder="Customer Code"
                {...register("customer_code")}
            />
            <p className="text-sm text-red-500">
                {errors.customer_code?.message}
            </p>
            </div>

            <div>
            <Input
                placeholder="Customer Name"
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
            {customer
                ? "Update Customer"
                : "Save Customer"}
            </Button>

        </div>
        </form>
    );
    }