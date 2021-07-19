@echo off

set root=%cd%

if not exist %appdata%\pip\pip.ini (
mkdir %appdata%\pip
copy %root%\config\pip.ini %appdata%\pip
)


call pip install newspaper3k selenium bs4 jsonpath requests PySide2 urllib3==1.25.8
call python %root%\main.py
