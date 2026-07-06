import { Boxes, ChartColumn, Package, ShieldCheck } from "lucide-react";

const features = [
  {
    icon: Package,
    title: "Inventory Management",
  },
  {
    icon: ChartColumn,
    title: "Sales Analytics",
  },
  {
    icon: Boxes,
    title: "Purchase Tracking",
  },
  {
    icon: ShieldCheck,
    title: "Secure ERP Platform",
  },
];

export default function AuthHero() {
  return (
    <div className="hidden lg:flex flex-1 flex-col justify-center p-16 text-white">
      <div className="max-w-md">
        <h1 className="text-5xl font-bold">
          BoltERP
        </h1>

        <p className="mt-4 text-lg text-slate-300">
          Modern Business Management Platform.
        </p>

        <div className="mt-12 space-y-6">
          {features.map((item) => {
            const Icon = item.icon;

            return (
              <div
                key={item.title}
                className="flex items-center gap-4"
              >
                <div className="rounded-xl bg-white/10 p-3 backdrop-blur">
                  <Icon size={22} />
                </div>

                <span className="text-lg">
                  {item.title}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}