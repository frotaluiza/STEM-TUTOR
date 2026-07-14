export type BlockType = "text" | "heading" | "ask" | "command" | "output" | "attachment" | "question" | "toggle";

export type BlockOrigin = "human" | "opencode" | "tutor";

export interface QuestionOption {
  id: string;
  label: string;
}

export interface BlockMeta {
  options?: QuestionOption[];
  allow_custom?: boolean;
  session_id?: string;
  model?: string;
  agent?: string;
  command?: string;
  reasoning?: string;
  [key: string]: unknown;
}

export interface Block {
  id: string;
  type: BlockType;
  origin: BlockOrigin;
  content: string;
  collapsed?: boolean;
  pinned?: boolean;
  meta?: BlockMeta;
}

export interface Note {
  id: string;
  title: string;
  blocks: Block[];
  tags: string[];
  project?: string;
  session?: string;
  module?: string;
  node?: string;
  created: string;
  updated: string;
}

export const BLOCK_ORIGIN_LABELS: Record<BlockOrigin, { icon: string; label: string; color: string }> = {
  human: { icon: "👤", label: "Anotação", color: "text-gray-300" },
  opencode: { icon: "🤖", label: "opencode", color: "text-cyan-400" },
  tutor: { icon: "🎓", label: "Tutor", color: "text-emerald-400" },
};
