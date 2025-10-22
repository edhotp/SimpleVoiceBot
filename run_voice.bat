@echo off
REM Voice Chatbot - CLI Voice Mode
REM Author: Edhot Purwoko - Microsoft Indonesia
REM License: MIT - Use at your own risk
echo Mengaktifkan virtual environment dan menjalankan Voice Chatbot CLI...
call venv\Scripts\activate.bat
echo Voice Chatbot dengan fitur Speech-to-Text dan Text-to-Speech
python voice_main.py
pause