@echo off
cd /d "%~dp0"

echo =========================================
echo    Starting Law Firm Website...
echo =========================================

echo.
echo Checking for Python...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not added to PATH!
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

echo.
echo Installing missing dependencies...
python -m pip install -r requirements.txt

echo.
echo Launching the server...
:: Start the Django server in a new command window
start "Django Server" cmd /k "python manage.py runserver"

:: Wait 4 seconds to let the server start up
timeout /t 4 /nobreak >nul

:: Open your web browser
start http://127.0.0.1:8000/

exit
