@echo off
REM run-pipeline.bat
REM Post-session pipeline: extract live docs + update project state
REM Usage: run-pipeline.bat [slug]
REM If slug is provided, only processes that session.
REM Otherwise processes all AI STEM Tutor sessions from opencode.db.

setlocal
set AI_TUTOR_DIR=%~dp0..\..
set PYTHON=python

echo [KB Pipeline] Starting post-session pipeline...
echo.

echo [KB Pipeline] Step 1: Extract live docs from opencode.db
if "%1"=="" (
    %PYTHON% "%AI_TUTOR_DIR%\scripts\kb\extract-live-docs.py"
) else (
    %PYTHON% "%AI_TUTOR_DIR%\scripts\kb\extract-live-docs.py" --slug %1
)
if %ERRORLEVEL% neq 0 (
    echo [KB Pipeline] ERROR: Extraction failed!
    exit /b 1
)
echo.

echo [KB Pipeline] Step 2: Update project state
%PYTHON% "%AI_TUTOR_DIR%\scripts\kb\update-project-state.py"
if %ERRORLEVEL% neq 0 (
    echo [KB Pipeline] ERROR: Project state update failed!
    exit /b 1
)
echo.

echo [KB Pipeline] Done! Project state updated.
