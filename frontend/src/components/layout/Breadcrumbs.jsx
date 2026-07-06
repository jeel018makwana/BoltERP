import { useLocation } from "react-router-dom";

export default function Breadcrumbs() {
  const location = useLocation();

  const page =
    location.pathname === "/"
      ? "Dashboard"
      : location.pathname.replace("/", "");

  return (
    <div>
      <h2 className="text-lg font-semibold capitalize">
        {page}
      </h2>
    </div>
  );
}