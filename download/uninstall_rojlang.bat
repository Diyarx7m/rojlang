@echo off
:: RojLang Uninstaller
:: Run as Administrator

echo.
echo  *** RojLang Uninstaller ***
echo  Rakirina RojLang ji Windowsê...
echo  Removing RojLang from Windows...
echo.

:: ── Step 1: Remove C:\RojLang folder ────────────────────────────
echo [1/4] Rakirina peldanka C:\RojLang...
if exist "C:\RojLang" (
    rmdir /S /Q "C:\RojLang"
    echo       OK - C:\RojLang hat rakirin.
) else (
    echo       C:\RojLang jixwe tune bû.
)

:: ── Step 2: Remove from system PATH ─────────────────────────────
echo [2/4] Rakirina RojLang ji PATH a Sîstemê...
powershell -Command ^
  "$p = [System.Environment]::GetEnvironmentVariable('Path','Machine');" ^
  "$p2 = ($p -split ';' | Where-Object { $_ -notlike '*RojLang*' }) -join ';';" ^
  "[System.Environment]::SetEnvironmentVariable('Path', $p2, 'Machine');" ^
  "Write-Host '      OK - PATH hat nûkirin.'"

:: ── Step 3: Remove .ku file association ─────────────────────────
echo [3/4] Rakirina tescîlkirina .ku...
reg delete "HKCR\.ku"         /f >nul 2>&1
reg delete "HKCR\RojLangFile" /f >nul 2>&1
echo       OK - .ku tescîlkirin hat rakirin.

:: ── Step 4: Refresh icons ────────────────────────────────────────
echo [4/4] Nûkirina Aykona Sîstemê...
powershell -Command "& { $code = '[DllImport(\"shell32.dll\")] public static extern void SHChangeNotify(int eventId, int flags, IntPtr item1, IntPtr item2);'; Add-Type -MemberDefinition $code -Name WinAPI -Namespace SHChange; [SHChange.WinAPI]::SHChangeNotify(0x8000000, 0, [IntPtr]::Zero, [IntPtr]::Zero); }" >nul 2>&1
echo       OK.

echo.
echo ==========================================
echo  RojLang bi temamî hate rakirin!
echo  RojLang fully removed!
echo ==========================================
echo.
echo  Ji bo sazkirin ji nû ve, installer bixebitîne.
echo  To reinstall, run install_rojlang.bat again.
echo.
pause
