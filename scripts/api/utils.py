from pathlib import Path
import subprocess

REPO_DIR = Path(__file__).resolve().parents[2]
PROJETOS_DIR = REPO_DIR / "Projetos"


def current_branch(worktree_path: Path = None) -> str:
    """Detect current git branch. Optionally from a worktree path."""
    cwd = worktree_path if worktree_path else REPO_DIR
    try:
        return subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, cwd=cwd, timeout=5
        ).stdout.strip()
    except Exception:
        return "unknown"


def resolve_projetos_dir(branch: str = None) -> tuple[Path, str]:
    """Resolve (Projetos_dir, real_branch) for a given branch.

    If branch is None or matches the current checkout, use default.
    Otherwise look for a git worktree directory.
    Returns (path, actual_branch_name).
    """
    if not branch:
        return PROJETOS_DIR, current_branch()

    current = current_branch()
    if branch == current:
        return PROJETOS_DIR, current

    # Look for worktree: ../REPO_NAME-{branch}/
    worktree_root = REPO_DIR.parent / f"{REPO_DIR.name}-{branch}"
    worktree_projetos = worktree_root / "Projetos"
    if worktree_projetos.exists():
        actual = current_branch(worktree_root)
        return worktree_projetos, actual

    from fastapi import HTTPException
    raise HTTPException(
        status_code=404,
        detail=f"Branch '{branch}' não encontrada. Crie o worktree: git worktree add ../{REPO_DIR.name}-{branch} {branch}",
    )
