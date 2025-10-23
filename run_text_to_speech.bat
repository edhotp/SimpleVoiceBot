@echo off
REM Simple Text-to-Speech Chatbot Runner
REM Edhot Purwoko - Microsoft Indonesia

echo ==========================================
echo    Simple Text-to-Speech Chatbot
echo ==========================================
echo.
echo Starting chatbot with text input and voice output...
echo.

REM Activate virtual environment if exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python tidak ditemukan!
    echo Pastikan Python sudah terinstall dan ada di PATH.
    pause
    exit /b 1
)

REM Run the text-to-speech chatbot
python text_to_speech_main.py

echo.
echo Text-to-Speech Chatbot stopped.
pause