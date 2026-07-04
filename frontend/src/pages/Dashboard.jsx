import DashboardLayout from "@/layouts/DashboardLayout";
import ThemeToggle from "@/components/layout/ThemeToggle";

export default function Dashboard() {
  return (
    <DashboardLayout>
      <div className="flex items-center justify-between p-8">
        <div>
          <h1 className="text-4xl font-bold">Dashboard</h1>
          <p className="text-muted-foreground mt-2">
            Welcome to BoltERP ERP System.
          </p>
        </div>

        <ThemeToggle />
      </div>
    </DashboardLayout>
  );
}