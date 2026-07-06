import { loginUser } from "../api/authApi";
import useAuthStore from "@/store/authStore";

export const useLogin = () => {
  const setAuth = useAuthStore((state) => state.setAuth);

  const login = async (credentials) => {
    const response = await loginUser(credentials);

    const data = response.data;

    setAuth({
      user: data.user,
      access: data.tokens.access,
      refresh: data.tokens.refresh,
    });

    return data;
  };

  return { login };
};