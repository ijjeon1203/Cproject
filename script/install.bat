@echo off

setlocal

chcp 65001

::start /wait ./setup.exe
xcopy "./IETM.zip" "C:\FMTS\IETM.zip" /E /I /Y


:: 대상 폴더 및 압축 파일 설정
set "TARGET_FOLDER=C:\FMTS\IETM"
set "ZIP_FILE=.\IETM.zip"

:: 폴더 존재 여부 확인
if exist "%TARGET_FOLDER%" (
    echo : 이미 %TARGET_FOLDER% 폴더가 존재합니다.     
	
) else (
	
    :: PowerShell을 사용하여 ZIP 압축 해제
    powershell -command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%TARGET_FOLDER%' -Force"
    echo 압축 해제 완료!
	)

endlocal


start /wait C:/FMTS/IETM/KAIS_42/Bin/Firebird-2.5.1.26351_1_Win32.exe

echo 설치가 완료되었습니다. 5초 후 자동으로 종료됩니다.
timeout /t 5

exit
@echo off

release 모드로 빌드 한 뒤에 setup 빌드 다시 해야하나?

