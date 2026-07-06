import { Bell, Search } from "lucide-react";

import { SidebarTrigger } from "@/components/ui/sidebar";
import { Input } from "@/components/ui/input";
import ThemeToggle from "./ThemeToggle";
import UserMenu from "./UserMenu";
import Breadcrumbs from "./Breadcrumbs";

export default function Header() {
  return (
    <header className="sticky top-0 z-40 flex h-16 items-center justify-between border-b bg-background/80 px-6 backdrop-blur-md">
      <div className="flex items-center gap-4">
        <SidebarTrigger />
        <Breadcrumbs />
      </div>

      <div className="flex items-center gap-3">
        <div className="relative hidden md:block">
          <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />

          <Input
            placeholder="Search..."
            className="w-72 pl-9"
          />
        </div>

        <button className="rounded-lg p-2 transition hover:bg-accent">
          <Bell className="h-5 w-5" />
        </button>

        <ThemeToggle />

        <UserMenu />
      </div>
    </header>
  );
}