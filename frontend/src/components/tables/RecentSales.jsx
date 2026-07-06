import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const sales = [
  {
    id: "#INV-1001",
    customer: "John Smith",
    amount: "₹12,500",
    status: "Paid",
  },
  {
    id: "#INV-1002",
    customer: "Priya Patel",
    amount: "₹8,200",
    status: "Pending",
  },
  {
    id: "#INV-1003",
    customer: "Rahul Sharma",
    amount: "₹16,000",
    status: "Paid",
  },
  {
    id: "#INV-1004",
    customer: "Amit Kumar",
    amount: "₹5,700",
    status: "Pending",
  },
];

export default function RecentSales() {
  return (
    <Card className="h-full">
      <CardHeader>
        <CardTitle>Recent Sales</CardTitle>
      </CardHeader>

      <CardContent>
        <div className="space-y-4">
          {sales.map((sale) => (
            <div
              key={sale.id}
              className="flex items-center justify-between rounded-lg border p-3"
            >
              <div>
                <p className="font-medium">{sale.customer}</p>
                <p className="text-sm text-muted-foreground">{sale.id}</p>
              </div>

              <div className="text-right">
                <p className="font-semibold">{sale.amount}</p>

                <span
                  className={`text-xs font-medium ${
                    sale.status === "Paid"
                      ? "text-green-500"
                      : "text-orange-500"
                  }`}
                >
                  {sale.status}
                </span>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}