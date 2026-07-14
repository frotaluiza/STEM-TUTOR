from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import projects, sessions, readings, tasks, daily_reports

app = FastAPI(
    title="Project Orchestrator API",
    description="API REST dos project-states — consumida pelo DeepTutor e PM",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/api/v1", tags=["projects"])
app.include_router(sessions.router, prefix="/api/v1", tags=["sessions"])
app.include_router(readings.router, prefix="/api/v1", tags=["readings"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(daily_reports.router, prefix="/api/v1", tags=["reports"])


@app.get("/api/v1/health")
def health():
    return {"status": "ok", "version": "1.0.0", "perfil": "Frota"}
