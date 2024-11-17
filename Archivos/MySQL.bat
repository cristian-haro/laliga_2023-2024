@echo off
setlocal enabledelayedexpansion
cls

tasklist | findstr /i "mysqld.exe"
if "!errorlevel!" NEQ "1" (
    echo Activo
)else C:\xampp\mysql_start.bat
