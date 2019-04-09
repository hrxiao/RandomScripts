echo off
:run
python check_class.py
timeout /t 10 >null
GOTO run
