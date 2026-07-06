import axiosInstance from "@/api/axios";

export const getCustomers = async (params) => {
  const response = await axiosInstance.get("/customers/", {
    params,
  });

  return response.data;
};

export const createCustomer = async (data) => {
  const response = await axiosInstance.post(
    "/customers/",
    data
  );

  return response.data;
};

export const updateCustomer = async ({
  id,
  data,
}) => {
  const response = await axiosInstance.put(
    `/customers/${id}/`,
    data
  );

  return response.data;
};

export const deleteCustomer = async (id) => {
  const response = await axiosInstance.delete(
    `/customers/${id}/`
  );

  return response.data;
};