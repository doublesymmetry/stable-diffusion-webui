@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--listen --nowebui --port=7860 --cors-allow-origins=*

call webui.bat
