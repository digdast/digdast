@echo off
title LinkedIn Daily Post Autopilot
cls
echo ================================================================
echo       LinkedIn Daily Post Autopilot (Efrain Rivas)
echo ================================================================
echo.
echo Running automated daily post engine...
echo.
python "%~dp0daily_post_engine.py" %*
echo.
pause
