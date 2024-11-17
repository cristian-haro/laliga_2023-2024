@echo off
setlocal enabledelayedexpansion
cls

tasklist | findstr /i "httpd.exe"
if "!errorlevel!" NEQ "1" (
    echo Activo
)else C:\xampp\apache_start.bat
