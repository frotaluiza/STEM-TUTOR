export type ProjectInfo = {
  name: string;
  slug: string;
  count: number;
  cost: number;
};

export type ProjectsResponse = {
  projects: ProjectInfo[];
  total_sessions: number;
  total_cost: number;
};

export type StatsResponse = {
  total_sessions: number;
  total_cost: number;
  total_live_docs: number;
  total_projects: number;
  stem_tutor_sessions: number;
  stem_tutor_cost: number;
};

export type SessionBrief = {
  slug: string;
  title: string;
  project: string;
  date: string;
  agent: string;
  cost: number;
};

export type SessionsResponse = {
  sessions: SessionBrief[];
  total: number;
  offset: number;
  limit: number;
};

export type Decision = {
  text: string;
  session_slug: string | null;
};

export type ProjectDetail = {
  slug: string;
  name: string;
  total_sessions: number;
  total_cost: number;
  date_range: { min: string | null; max: string | null } | null;
  branch: string | null;
  last_commit: string | null;
  last_updated: string | null;
  decisions: Decision[];
  todos: string[];
  recent_sessions: SessionBrief[];
  session_files_available: number;
};

export type PMState = {
  projects: ProjectInfo[];
  selectedSlug: string | null;
  selectedProject: ProjectDetail | null;
  sessions: SessionBrief[];
  sessionsTotal: number;
  stats: StatsResponse | null;
  loading: boolean;
  error: string | null;
};
