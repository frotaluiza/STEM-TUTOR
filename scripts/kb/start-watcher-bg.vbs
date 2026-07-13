' start-watcher-bg.vbs
' Runs the watcher in background without a console window.
' Used by Task Scheduler to start the Python process silently.

Dim shell, pythonExe, scriptFile, aitutorDir, args
Set shell = CreateObject("WScript.Shell")

aitutorDir = "C:\Users\frota\Documents\Projetos\AI TUTOR"
pythonExe = "python"
scriptFile = aitutorDir & "\scripts\kb\watch-opencode-db.py"
args = "-u """ & scriptFile & """ --interval 30 --settle 120 --watchdog"

shell.Run pythonExe & " " & args, 0, False
