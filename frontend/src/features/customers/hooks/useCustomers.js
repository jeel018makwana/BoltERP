import { useQuery } from "@tanstack/react-query";
import { getCustomers } from "../api/customerApi";

export const useCustomers = (params) => {
  return useQuery({
    queryKey: ["customers", params],
    queryFn: () => getCustomers(params),
    keepPreviousData: true,
  });
};