@echo off
echo ============================
echo   Daily Git Push Script
echo ============================

echo.
echo Checking current status...
git status

echo.
echo Adding all changes...
git add .

echo.
set /p msg=Enter commit message: 

echo.
echo Committing changes...
git commit -m "%msg%"

echo.
echo Pulling latest changes from GitHub (safe rebase)...
git pull origin main --rebase

echo.
echo Pushing to GitHub...
git push

echo.
echo Done! Your code is uploaded 🚀
pause
