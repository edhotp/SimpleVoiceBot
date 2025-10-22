@echo off
REM Voice Chatbot - Web Interface
REM Author: Edhot Purwoko - Microsoft Indonesia
REM License: MIT - Use at your own risk
echo Mengaktifkan virtual environment dan menjalankan chatbot web...
call venv\Scripts\activate.bat
echo Web chatbot akan berjalan di: http://localhost:5000
python web_app.py
pause