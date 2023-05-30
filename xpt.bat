@echo off
setlocal

REM get the directory of the batch script
set BATCH_PATH=%~dp0
cd /d %BATCH_PATH%

REM set the path of the Python script relative to the batch script
set SCRIPT_PATH=./xpt.py

REM check if Python is installed and added to PATH
where /q python
if ErrorLevel 1 (
    echo Python was not found. Please install it and add it to PATH
    exit /b
)

REM execute the script with all the passed arguments
python "%SCRIPT_PATH%" %*

endlocal
