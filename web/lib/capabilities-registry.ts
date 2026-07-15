/**
 * Capabilities Registry — catalogo de todas as features do sistema.
 * Cada capability é uma feature que pode ser ativada/desativada por branch.
 * 
 * Uso:
 *   const caps = useBranchCapabilities();
 *   if (caps.pm_dashboard_v2) { ... }
 */

export const CAPABILITIES = {
  /** PM Dashboard v2 — tabelas, sessões, stats */
  pm_dashboard_v2: { label: "PM Dashboard v2", default: true },
  /** Branch selector no header do PM */
  branch_selector: { label: "Branch Selector", default: true },
  /** Sync status no header do PM */
  sync_status: { label: "Sync Status", default: true },
  /** Tarefas (tasks system) no PM */
  tarefas: { label: "Tarefas", default: true },
  /** Análise de conflitos entre branches */
  conflict_analysis: { label: "Análise de Conflitos", default: true },
  /** Mind Map como Project Space visual */
  mind_map: { label: "Mind Map", default: true },
  /** SessionViewer com abas Chat + Live Doc + Terminal */
  session_viewer: { label: "SessionViewer", default: true },
  /** Live Doc gerado do opencode DB */
  live_doc: { label: "Live Doc", default: true },
  /** Terminal via WebSocket no SessionViewer */
  terminal: { label: "Terminal", default: true },
  /** Fork de sessões via opencode --fork */
  fork_session: { label: "Fork de Sessão", default: true },
  /** NoteBlocks multi-modal com abas */
  noteblocks_multi: { label: "NoteBlocks Multi-modal", default: true },
  /** MarkdownBlock estilo Notion */
  markdown_block: { label: "MarkdownBlock", default: true },
  /** Drag-and-drop para reordenar blocos */
  drag_drop_blocks: { label: "Drag-and-drop Blocos", default: true },
  /** Projects page / Orchestrator Dashboard */
  projects_page: { label: "Projects Page", default: true },
  /** Session-to-branch mapping */
  session_branch_map: { label: "Sessão → Branch", default: false },
  /** Wolfram Alpha integration (futuro) */
  wolfram_alpha: { label: "Wolfram Alpha", default: false },
} as const;

export type CapabilityId = keyof typeof CAPABILITIES;
export type CapabilitiesMap = Partial<Record<CapabilityId, boolean>>;

export function hasCap(caps: CapabilitiesMap | null | undefined, id: CapabilityId): boolean {
  if (!caps) return CAPABILITIES[id]?.default ?? false;
  return caps[id] ?? CAPABILITIES[id]?.default ?? false;
}
