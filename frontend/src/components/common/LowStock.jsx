import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const products = [
  { name: "Wireless Mouse", stock: 3 },
  { name: "Keyboard", stock: 5 },
  { name: "Monitor", stock: 2 },
  { name: "USB Cable", stock: 6 },
];

export default function LowStock() {
  return (
    <Card className="h-full">
      <CardHeader>
        <CardTitle>Low Stock Products</CardTitle>
      </CardHeader>

      <CardContent>
        <div className="space-y-4">
          {products.map((item) => (
            <div
              key={item.name}
              className="flex items-center justify-between"
            >
              <span>{item.name}</span>

              <span className="rounded bg-red-500/10 px-2 py-1 text-sm font-semibold text-red-500">
                {item.stock} Left
              </span>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}