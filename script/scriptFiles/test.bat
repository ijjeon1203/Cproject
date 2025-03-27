@echo off
chcp 65001
start /wait ./setup.exe
xcopy "./IETM" "src/" /E /I /Y
start /wait ./IETM/KAIS_42/Bin/Firebird-2.5.1.26351_1_Win32.exe


echo 설치가 완료되었습니다. 5초 후 자동으로 종료됩니다.
timeout /t 5
exit

