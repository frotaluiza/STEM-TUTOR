import { apiFetch } from "./api";

export interface ProjectSummary {
  slug: string;
  nome: string;
  area: string | null;
  status: string | null;
  repositorio_codigo: string | null;
  objetivo: string | null;
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
}

export interface ProjectDetail {
  slug: string;
  project_state: ProjectState;
  repositorio_codigo: string | null;
  fontes: Record<string, { nome: string; arquivo: string; conteudo?: string }[]>;
  relatorios: Record<string, { nome: string; arquivo: string }[]>;
}

export interface Profile {
  perfil: string;
  usuario: string;
  github: string;
  projetos: { slug: string; nome: string; repositorio_codigo?: string }[];
}

const BASE = "/orchestrator/api/v1";

export async function fetchProjects(): Promise<ProjectSummary[]> {
  const res = await apiFetch(`${BASE}/projects`);
  const data = await res.json();
  return data.projects ?? [];
}

export async function fetchProject(slug: string): Promise<ProjectDetail> {
  const res = await apiFetch(`${BASE}/projects/${slug}`);
  return res.json();
}

export async function fetchProjectState(slug: string): Promise<ProjectState> {
  const res = await apiFetch(`${BASE}/projects/${slug}/state`);
  return res.json();
}

export async function fetchProjectDatabase(
  slug: string,
  database: string,
): Promise<{ nome: string; arquivo: string; conteudo?: string }[]> {
  const res = await apiFetch(`${BASE}/projects/${slug}/${database}`);
  const data = await res.json();
  return data[database] ?? [];
}

export async function fetchProfile(): Promise<Profile> {
  const res = await apiFetch(`${BASE}/profile`);
  return res.json();
}
