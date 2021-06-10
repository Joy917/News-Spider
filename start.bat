@echo off
rem cd /d %~dp0
set root=%~dp0

rem 拷贝国内pip镜像源配置
if not exist %appdata%\pip\pip.ini (
mkdir %appdata%\pip
copy %root%config\pip.ini %appdata%\pip
)

rem 下载依赖
call pip install newspaper3k selenium bs4 jsonpath requests PySide2 urllib3==1.25.8  
call python %root%main.py
rem pause