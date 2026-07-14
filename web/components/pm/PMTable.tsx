"use client";

import { ArrowUpDown, Search } from "lucide-react";
import { useCallback, useMemo, useState } from "react";

export interface Column<T> {
  key: string;
  label: string;
  render: (row: T) => React.ReactNode;
  sortable?: boolean;
  sortValue?: (row: T) => string | number;
  filterable?: boolean;
  filterValue?: (row: T) => string;
  width?: string;
}

interface PMTableProps<T> {
  columns: Column<T>[];
  data: T[];
  title: string;
  total?: number;
  emptyMessage?: string;
  defaultSort?: { key: string; dir: "asc" | "desc" };
  filterable?: boolean;
  onRowClick?: (row: T) => void;
}

export default function PMTable<T extends Record<string, unknown>>({
  columns,
  data,
  title,
  total,
  emptyMessage = "Nenhum registro",
  defaultSort,
  filterable = true,
  onRowClick,
}: PMTableProps<T>) {
  const [sortKey, setSortKey] = useState<string>(defaultSort?.key || "");
  const [sortDir, setSortDir] = useState<"asc" | "desc">(defaultSort?.dir || "desc");
  const [filterText, setFilterText] = useState("");

  const handleSort = useCallback(
    (key: string) => {
      if (sortKey === key) {
        setSortDir((d) => (d === "asc" ? "desc" : "asc"));
      } else {
        setSortKey(key);
        setSortDir("desc");
      }
    },
    [sortKey],
  );

  const filtered = useMemo(() => {
    if (!filterText || !filterable) return data;
    const q = filterText.toLowerCase();
    return data.filter((row) =>
      columns.some((col) => {
        if (!col.filterable) return false;
        const val = col.filterValue ? col.filterValue(row) : String(col.render(row));
        return val.toLowerCase().includes(q);
      }),
    );
  }, [data, filterText, columns, filterable]);

  const sorted = useMemo(() => {
    if (!sortKey) return filtered;
    const col = columns.find((c) => c.key === sortKey);
    if (!col) return filtered;
    return [...filtered].sort((a, b) => {
      const va = col.sortValue ? col.sortValue(a) : String(col.render(a));
      const vb = col.sortValue ? col.sortValue(b) : String(col.render(b));
      const cmp = typeof va === "number" && typeof vb === "number" ? va - vb : String(va).localeCompare(String(vb));
      return sortDir === "asc" ? cmp : -cmp;
    });
  }, [filtered, sortKey, sortDir, columns]);

  return (
    <div className="bg-[var(--card)] rounded-lg border border-[var(--border)]">
      <div className="flex items-center justify-between px-4 py-3 border-b border-[var(--border)]/40">
        <div className="flex items-center gap-2">
          <h3 className="text-sm font-semibold text-[var(--foreground)]">{title}</h3>
          {total !== undefined && (
            <span className="text-[11px] text-[var(--muted-foreground)] bg-[var(--muted)]/40 px-1.5 py-0.5 rounded">
              {total}
            </span>
          )}
        </div>
        {filterable && (
          <div className="flex items-center gap-1.5 rounded-md border border-[var(--border)]/55 bg-[var(--background)] px-2 py-1 text-[12px] text-[var(--muted-foreground)] focus-within:border-[var(--primary)]/40">
            <Search size={12} strokeWidth={1.8} />
            <input
              type="text"
              value={filterText}
              onChange={(e) => setFilterText(e.target.value)}
              placeholder="Filtrar..."
              className="min-w-0 flex-1 bg-transparent outline-none text-[var(--foreground)] placeholder:text-[var(--muted-foreground)]/60"
            />
          </div>
        )}
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-[12.5px]">
          <thead>
            <tr className="border-b border-[var(--border)]/30">
              {columns.map((col) => (
                <th
                  key={col.key}
                  className={`text-left text-[11px] font-medium text-[var(--muted-foreground)] px-3 py-2 ${
                    col.sortable ? "cursor-pointer hover:text-[var(--foreground)] select-none" : ""
                  }`}
                  style={col.width ? { width: col.width } : undefined}
                  onClick={() => col.sortable && handleSort(col.key)}
                >
                  <div className="flex items-center gap-1">
                    {col.label}
                    {col.sortable && (
                      <ArrowUpDown
                        size={10}
                        strokeWidth={1.8}
                        className={`shrink-0 transition-opacity ${
                          sortKey === col.key ? "opacity-100 text-[var(--primary)]" : "opacity-40"
                        }`}
                      />
                    )}
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {sorted.length === 0 ? (
              <tr>
                <td colSpan={columns.length} className="text-center py-8 text-[13px] text-[var(--muted-foreground)]">
                  {emptyMessage}
                </td>
              </tr>
            ) : (
              sorted.map((row, i) => (
                <tr
                  key={row.slug as string || i}
                  onClick={() => onRowClick?.(row)}
                  className={`border-b border-[var(--border)]/15 transition-colors ${
                    onRowClick ? "cursor-pointer hover:bg-[var(--accent)]/30" : "hover:bg-[var(--muted)]/20"
                  }`}
                >
                  {columns.map((col) => (
                    <td key={col.key} className="px-3 py-2 text-[var(--foreground)]" style={col.width ? { width: col.width } : undefined}>
                      {col.render(row)}
                    </td>
                  ))}
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {total && total > sorted.length && (
        <div className="px-4 py-2 text-[11px] text-[var(--muted-foreground)] border-t border-[var(--border)]/20">
          Mostrando {sorted.length} de {total}
        </div>
      )}
    </div>
  );
}
