@echo off
REM Download Python
curl -O https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe
REM Install Python
start /wait python-3.8.10-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
REM Install some ilbs
pip install colorama webbrowser pytz pyttsx3 googletrans requests pydub Pillow pyshorteners lorem-text
REM start pxshell
python px.py
