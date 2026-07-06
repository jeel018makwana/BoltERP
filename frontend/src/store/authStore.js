import { create } from "zustand";
import { persist } from "zustand/middleware";

const useAuthStore = create(
  persist(
    (set) => ({
      user: null,
      accessToken: null,
      refreshToken: null,

      setAuth: ({ user, access, refresh }) =>
        set({
          user,
          accessToken: access,
          refreshToken: refresh,
        }),

      updateAccessToken: (token) =>
        set({
          accessToken: token,
        }),

      logout: () =>
        set({
          user: null,
          accessToken: null,
          refreshToken: null,
        }),
    }),
    {
      name: "bolterp-auth",
    }
  )
);

export default useAuthStore;