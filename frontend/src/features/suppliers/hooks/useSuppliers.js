import { useQuery } from "@tanstack/react-query";
import { getSuppliers } from "../api/supplierApi";

export const useSuppliers = (params) => {
    return useQuery({
        queryKey: ["suppliers", params],
        queryFn: () => getSuppliers(params),
        keepPreviousData: true,
    });
};