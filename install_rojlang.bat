@echo off
:: ╔══════════════════════════════════════════════════════╗
:: ║         RojLang Installer for Windows               ║
:: ║   Run this ONCE as Administrator                    ║
:: ╚══════════════════════════════════════════════════════╝

echo.
echo  ██████╗  ██████╗      ██╗██╗      █████╗ ███╗   ██╗ ██████╗ 
echo  ██╔══██╗██╔═══██╗     ██║██║     ██╔══██╗████╗  ██║██╔════╝ 
echo  ██████╔╝██║   ██║     ██║██║     ███████║██╔██╗ ██║██║  ███╗
echo  ██╔══██╗██║   ██║██   ██║██║     ██╔══██║██║╚██╗██║██║   ██║
echo  ██║  ██║╚██████╔╝╚█████╔╝███████╗██║  ██║██║ ╚████║╚██████╔╝
echo  ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
echo.
echo  [*] RojLang Installer - Windows
echo  [*] Sazkirina RojLang li ser Windowsê...
echo ──────────────────────────────────────────────────────
echo.

:: ── Step 1: Create installation folder ─────────────────
set INSTALL_DIR=C:\RojLang
echo  [1/5] Amadekirina peldanka sazkirinê: %INSTALL_DIR%
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: ── Step 2: Copy interpreter.py ────────────────────────
echo  [2/5] Kopîkirina interpreter.py ...
set SCRIPT_DIR=%~dp0
if exist "%SCRIPT_DIR%interpreter.py" (
    copy /Y "%SCRIPT_DIR%interpreter.py" "%INSTALL_DIR%\interpreter.py" >nul
    echo       OK - interpreter.py hat kopîkirin.
) else (
    echo       ÇEWT - interpreter.py di heman peldankê de nebû!
    echo       Bicivîne ku interpreter.py û install_rojlang.bat di heman peldankê de bin.
    pause
    exit /b 1
)

:: ── Step 3: Create rojlang.bat launcher ────────────────
echo  [3/5] Afirandina rojlang.bat ...
(
    echo @echo off
    echo python "%INSTALL_DIR%\interpreter.py" %%*
) > "%INSTALL_DIR%\rojlang.bat"
echo       OK - rojlang.bat hat afirandin.

:: ── Step 4: Add C:\RojLang to system PATH ──────────────
echo  [4/5] Zêdekirina RojLang bo PATH a Sîstemê...
powershell -Command ^
  "$p = [System.Environment]::GetEnvironmentVariable('Path','Machine');" ^
  "if ($p -notlike '*C:\RojLang*') {" ^
  "  [System.Environment]::SetEnvironmentVariable('Path', $p + ';C:\RojLang', 'Machine');" ^
  "  Write-Host '      OK - PATH hat nûkirin.'" ^
  "} else {" ^
  "  Write-Host '      OK - RojLang jixwe di PATH de ye.'" ^
  "}"

:: ── Step 5: Register .ku file association ──────────────
echo  [5/5] Tescîlkirina celebê dosyayê .ku ...
reg add "HKCR\.ku"                          /ve /d "RojLangFile"    /f >nul 2>&1
reg add "HKCR\RojLangFile"                  /ve /d "RojLang Source" /f >nul 2>&1
if exist "%SCRIPT_DIR%rojlang.ico" (
    copy /Y "%SCRIPT_DIR%rojlang.ico" "%INSTALL_DIR%\rojlang.ico" >nul
    echo       OK - rojlang.ico hat kopîkirin.
) else (
    echo       (rojlang.ico nebû, aykonê xwerû tê bikar anîn)
)
reg add "HKCR\RojLangFile\DefaultIcon"      /ve /d "%INSTALL_DIR%\rojlang.ico" /f >nul 2>&1
reg add "HKCR\RojLangFile\shell\open\command" /ve /d "cmd.exe /k python \"%INSTALL_DIR%\interpreter.py\" \"%%1\"" /f >nul 2>&1
echo       OK - .ku dosyayan bi RojLang re hatin girêdan.

:: ── Done ───────────────────────────────────────────────
echo.
echo ──────────────────────────────────────────────────────
echo  [✓] Sazkirin qediya! RojLang hate saz kirin!
echo ──────────────────────────────────────────────────────
echo.
echo  Niha tu dikarî bikar bînî:
echo.
echo    1. Ji her cihî di CMD / Terminal de:
echo       rojlang game.ku
echo.
echo    2. Rasterast bixe du-klîk li ser *.ku dosyayan
echo       da ku ew bixebite!
echo.
echo  Balkêşî: Terminalê nû veke da ku PATH bixebite.
echo.
pause
