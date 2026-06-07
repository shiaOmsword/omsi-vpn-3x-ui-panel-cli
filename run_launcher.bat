@echo off
chcp 65001 > nul
title Panel Launcher

cd /d "%~dp0"

poetry run launch menu --config config/local.yml

echo.
echo Launcher finished.
pause