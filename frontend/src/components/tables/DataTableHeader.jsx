export default function DataTableHeader({
  title,
  subtitle,
  action,
}) {
  return (
    <div className="mb-6 flex items-center justify-between">
      <div>
        <h1 className="text-3xl font-bold">
          {title}
        </h1>

        <p className="text-muted-foreground">
          {subtitle}
        </p>
      </div>

      {action}
    </div>
  );
}