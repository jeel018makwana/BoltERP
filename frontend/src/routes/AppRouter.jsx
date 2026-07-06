import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "@/pages/Dashboard";
import Login from "@/pages/Login";
import NotFound from "@/pages/Notfound";
import LoginPage from "@/features/auth/pages/LoginPage";
import ProtectedRoute from "./ProtectedRoute";
import CustomersPage from "@/features/customers/pages/CustomersPage";

export default function AppRouter() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={
                    <ProtectedRoute>
                        <Dashboard />
                    </ProtectedRoute>
                }/>
                <Route path="/login" element={<LoginPage />}/>
                <Route path="*" element={<NotFound />}/>
                <Route path="/customers" element={<CustomersPage />} />
            </Routes>
        </BrowserRouter>
    );
}

