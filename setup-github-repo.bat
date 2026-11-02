@echo off
setlocal
echo ======================================================================
echo    UI/UX Pro Max - GitHub Repository Publisher for Google AI Studio
echo ======================================================================
echo.

set /p REPO_URL="Enter your GitHub Repository URL (e.g., https://github.com/username/ui-ux-pro-max-google-ai-studio.git): "

if "%REPO_URL%"=="" (
    echo [!] No URL entered. Aborting.
    pause
    exit /b 1
)

echo.
echo [*] Initializing Git repository...
git init

echo [*] Staging all files...
git add .

echo [*] Committing files...
git commit -m "feat: Initial commit of UI/UX Pro Max for Google AI Studio"

echo [*] Renaming default branch to main...
git branch -M main

echo [*] Setting remote origin to %REPO_URL%...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo [*] Pushing to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo [SUCCESS] Your repository is now live on GitHub!
    echo Anyone can now install it to Google AI Studio directly from your repo.
    echo ======================================================================
) else (
    echo.
    echo [!] Push failed. Check your GitHub permissions or credentials.
)

echo.
pause
