import { Skeleton } from "@/components/ui/skeleton";

export default function DataTableLoading({
  rows = 8,
  columns = 6,
}) {
  return (
    <div className="rounded-xl border bg-card">
      {/* Header */}
      <div className="border-b p-4">
        <Skeleton className="h-6 w-48" />
      </div>

      {/* Rows */}
      <div className="divide-y">
        {Array.from({ length: rows }).map((_, row) => (
          <div
            key={row}
            className="grid gap-4 p-4"
            style={{
              gridTemplateColumns: `repeat(${columns}, minmax(0, 1fr))`,
            }}
          >
            {Array.from({ length: columns }).map((_, col) => (
              <Skeleton
                key={col}
                className="h-5 w-full"
              />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}