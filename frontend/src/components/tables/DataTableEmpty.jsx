import { Database } from "lucide-react";

export default function DataTableEmpty({
  title = "No Data Found",
  description = "There is nothing to display.",
}) {
  return (
    <div className="flex flex-col items-center justify-center rounded-xl border border-dashed bg-card py-16 text-center">
      <Database className="mb-4 h-12 w-12 text-muted-foreground" />

      <h3 className="text-lg font-semibold">
        {title}
      </h3>

      <p className="mt-2 max-w-md text-sm text-muted-foreground">
        {description}
      </p>
    </div>
  );
}