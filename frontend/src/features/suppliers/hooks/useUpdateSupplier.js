import { useMutation, useQueryClient } from "@tanstack/react-query";
import { updateSupplier } from "../api/supplierApi";
import toast from "react-hot-toast";

export const useUpdateSupplier = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateSupplier,

    onSuccess: () => {
      toast.success("Supplier updated successfully");

      queryClient.invalidateQueries({
        queryKey: ["suppliers"],
      });
    },

    onError: (error) => {
      toast.error(
        error?.response?.data?.message ||
        "Failed to update supplier"
      );
    },
  });
};