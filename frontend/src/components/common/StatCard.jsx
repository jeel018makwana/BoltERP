import { Card, CardContent } from "@/components/ui/card";
import { TrendingUp } from "lucide-react";

export default function StatCard({
  title,
  value,
  icon: Icon,
  change,
}) {
  return (
    <Card className="border-0 shadow-sm hover:shadow-lg transition-all duration-300">
      <CardContent className="flex items-center justify-between p-6">
        <div>
          <p className="text-sm text-muted-foreground">
            {title}
          </p>

          <h2 className="mt-2 text-3xl font-bold">
            {value}
          </h2>

          <div className="mt-3 flex items-center gap-1 text-emerald-500 text-sm">
            <TrendingUp className="h-4 w-4" />
            {change}
          </div>
        </div>

        <div className="rounded-2xl bg-primary/10 p-4">
          <Icon className="h-7 w-7 text-primary" />
        </div>
      </CardContent>
    </Card>
  );
}