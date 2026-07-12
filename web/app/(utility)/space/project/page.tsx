"use client";

import dynamic from "next/dynamic";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";

const ProjectMindMap = dynamic(() => import("@/components/project/ProjectMindMap"), {
  ssr: false,
  loading: () => <div className="p-8 text-center text-[var(--muted-foreground)]">Loading project state...</div>,
});

export default function ProjectPage() {
  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center gap-3 px-6 py-3 border-b border-[var(--border)]">
        <Link
          href="/space"
          className="flex items-center gap-1 text-sm text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to Learning Space
        </Link>
        <div className="h-4 w-px bg-[var(--border)]" />
        <h1 className="text-sm font-semibold">Project Mind Map</h1>
      </div>
      <div className="flex-1 relative">
        <ProjectMindMap />
      </div>
    </div>
  );
}
