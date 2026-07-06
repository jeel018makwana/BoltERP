import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createSupplier } from "../api/supplierApi";
import toast from "react-hot-toast";

export const useCreateSupplier = () => {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: createSupplier,
        onSuccess: () => {
            toast.success("Supplier created successfully");
            queryClient.invalidateQueries({
                queryKey:["suppliers"],
            });
        },


        onError: (error) => {
            toast.error(
                error?.response?.data?.message || "Failed to create supplier"
            );
        },
    });
};