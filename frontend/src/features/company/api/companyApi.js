import axiosInstance from "@/api/axios";

export const getCompany = async () => {
  const response = await axiosInstance.get("/company/profile/");

  return response.data;
};