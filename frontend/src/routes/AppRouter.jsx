import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "@/pages/Dashboard";
import Login from "@/pages/Login";
import NotFound from "@/pages/Notfound";

export default function AppRouter() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Dashboard />}/>
                <Route path="/login" element={<Login />}/>
                <Route path="*" element={<NotFound />}/>
            </Routes>
        </BrowserRouter>
    );
}

