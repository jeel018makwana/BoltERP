import React from "react";
import ReactDOM from "react-dom/client";

import "./index.css";

import App from "./App";
import ThemeProvider from "./components/common/ThemeProvider";
import { Toaster } from "react-hot-toast";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>

      <ThemeProvider>
        <App />
        <Toaster 
          position="top-right"
          reverseOrder={false}
        />
      </ThemeProvider>
    </QueryClientProvider>
  </React.StrictMode>
);