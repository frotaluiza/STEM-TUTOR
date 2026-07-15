import { apiFetch } from "./api";

export interface ProjectSummary {
  slug: string;
  nome: string;
  area: string | null;
  status: string | null;
  repositorio_codigo: string | null;
  objetivo: string | null;
  session_count?: number;
}

export interface ProjectState {
  projeto: string;
  slug: string;
  perfil: string;
  area: string;
  status: string;
  objetivo: string;
  repositorio_codigo?: string;
  caminho?: { fase: string; descricao: string; fontes?: string[] }[];
  decisoes_acumuladas?: { contexto: string; escolha: string }[];
  proximos_passos?: { descricao: string; prioridade: string }[];
  ultima_atualizacao?: string;
  branch_detectada?: string;
}

export interface ProjectDetail {
  slug: string;
  project_state: ProjectState;
  repositorio_codigo: string | null;
  fontes: Record<string, { nome: string; arquivo: string; conteudo?: string }[]>;
  relatorios: Record<string, { nome: string; arquivo: string }[]>;
}

export interface BranchInfo {
  path: string;
  branch: string;
}

export interface BranchesResponse {
  branches: BranchInfo[];
  current: string;
}

export interface SessionEntry {
  slug: string;
  arquivo: string;
  projeto: string;
  origem?: string;
}

const BASE = "/orchestrator/api/v1";

function qs(params: Record<string, string | undefined>): string {
  const entries = Object.entries(params).filter(
    ([, v]) => v !== undefined && v !== "",
  );
  return entries.length ? "?" + new URLSearchParams(entries).toString() : "";
}

export async function fetchProjects(branch?: string): Promise<ProjectSummary[]> {
  const res = await apiFetch(`${BASE}/projects${qs({ branch })}`);
  const data = await res.json();
  return data.projects ?? [];
}

export async function fetchProject(
  slug: string,
  branch?: string,
): Promise<ProjectDetail> {
  const res = await apiFetch(`${BASE}/projects/${slug}${qs({ branch })}`);
  return res.json();
}

export async function fetchProjectState(
  slug: string,
  branch?: string,
): Promise<ProjectState> {
  const res = await apiFetch(`${BASE}/projects/${slug}/state${qs({ branch })}`);
  return res.json();
}

export async function fetchProjectDatabase(
  slug: string,
  database: string,
  branch?: string,
): Promise<{ nome: string; arquivo: string; conteudo?: string }[]> {
  const res = await apiFetch(
    `${BASE}/projects/${slug}/${database}${qs({ branch })}`,
  );
  const data = await res.json();
  return data[database] ?? [];
}

export async function fetchSessions(
  projeto?: string,
  origem?: string,
  branch?: string,
): Promise<SessionEntry[]> {
  const res = await apiFetch(
    `${BASE}/sessions${qs({ projeto, origem, branch })}`,
  );
  const data = await res.json();
  return data.sessions ?? [];
}

export async function fetchBranches(): Promise<BranchesResponse> {
  const res = await apiFetch(`${BASE}/branches`);
  return res.json();
}

export async function fetchProfile(branch?: string) {
  const res = await apiFetch(`${BASE}/profile${qs({ branch })}`);
  return res.json();
}
