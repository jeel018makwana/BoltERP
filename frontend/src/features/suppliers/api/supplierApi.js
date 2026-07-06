import axiosInstance from "@/api/axios";

export const getSuppliers = async (params) => {
    const response = await axiosInstance.get("/suppliers/", {
        params,
    });
    return response.data;
};

export const createSupplier = async (data) => {
    const response = await axiosInstance.post(
        "/suppliers/",
        data
    );
    return response.data;
};

export const updateSupplier = async ({
    id,
    data,
}) => {
    const response = await axiosInstance.put(
        `/suppliers/${id}/`,
        data
    );
    return response.data;
};

export const deleteSupplier = async (id) => {
    const response = await axiosInstance.delete(
        `/suppliers/${id}/`
    );
    return response.data;
};