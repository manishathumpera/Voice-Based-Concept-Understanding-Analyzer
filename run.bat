@echo off
cd /d %~dp0

call venv\Scripts\activate.bat

set PATH=C:\Users\thump\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin;%PATH%

python -m streamlit run app.py

pause