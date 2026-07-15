@echo off
cd /d "%~dp0"
node --max-old-space-size=4096 ./node_modules/next/dist/bin/next dev
