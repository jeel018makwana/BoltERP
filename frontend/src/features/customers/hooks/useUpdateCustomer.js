import { useMutation, useQueryClient } from "@tanstack/react-query";
import { updateCustomer } from "../api/customerApi";
import toast from "react-hot-toast";

export const useUpdateCustomer = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateCustomer,

    onSuccess: () => {
      toast.success("Customer updated successfully");

      queryClient.invalidateQueries({
        queryKey: ["customers"],
      });
    },

    onError: (error) => {
      toast.error(
        error?.response?.data?.message ||
          "Failed to update customer"
      );
    },
  });
};