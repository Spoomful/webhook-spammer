@echo off
title (h)
:menu
cls
echo [1] to start the spammer
echo [2] to install the modules
set /p input=%computername%@%username% 
if %input% == 1 goto start
if %input% == 2 goto install
goto menu 
:install
cls
pip install -r requirements.txt
pause >nul
cls
goto menu
:start
set /p webhook=Webhook:
set /p delay=Delay:
set /p threads=Threads:
cls
python spammer.py -w %webhook% -d %delay% -t %threads%