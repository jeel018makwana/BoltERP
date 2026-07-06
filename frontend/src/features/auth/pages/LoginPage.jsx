import { motion } from "framer-motion";

import LoginForm from "../components/LoginForm";
import AuthHero from "../components/AuthHero";

export default function LoginPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950">
      <div className="mx-auto flex min-h-screen max-w-7xl">
        
        <AuthHero />

        <div className="flex flex-1 items-center justify-center p-6">
          <motion.div
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
          >
            <LoginForm />
          </motion.div>
        </div>

      </div>
    </div>
  );
}