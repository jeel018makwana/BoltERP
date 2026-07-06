import DashboardLayout from "@/layouts/DashboardLayout";
import RevenueChart from "../components/charts/RevenueChart";
import StatCard from "@/components/common/StatCard";
import SalesOverview from "@/components/charts/SalesOverview";
import {
  DollarSign,
  Package,
  Users,
  ShoppingCart,
} from "lucide-react";
import RecentSales from "@/components/tables/RecentSales";
import LowStock from "@/components/common/LowStock";
import { useDashboard } from "@/features/dashboard/hooks/useDashboard";


export default function Dashboard() {

    const {
        data,
        isLoading,
        error,
    } = useDashboard();

  return (
    
    <DashboardLayout>
      <div className="space-y-8">

        <div>
          <h1 className="text-4xl font-bold">
            Welcome back 👋
          </h1>

          <p className="mt-2 text-muted-foreground">
            Here's what's happening in your business today.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

          <StatCard
            title="Revenue"
            value="₹2,45,000"
            icon={DollarSign}
            change="+12.5%"
          />

          <StatCard
            title="Products"
            value="426"
            icon={Package}
            change="+8%"
          />

          <StatCard
            title="Customers"
            value="1,286"
            icon={Users}
            change="+15%"
          />

          <StatCard
            title="Sales"
            value="352"
            icon={ShoppingCart}
            change="+10%"
          />

        </div>
        <div className="grid gap-6 lg:grid-cols-3">
            <div className="lg:col-span-2">
                <RevenueChart />
            </div>

            <div>
                <SalesOverview />
            </div>
        </div>
        <div className="grid gap-6 lg:grid-cols-3">
            <div className="lg:col-span-2">
                <RecentSales />
            </div>

            <div>
                <LowStock />
            </div>
        </div>
      </div>
    </DashboardLayout>
  );
}