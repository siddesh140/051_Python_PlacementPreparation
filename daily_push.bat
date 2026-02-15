@echo off
echo ============================
echo   Daily Git Push Script
echo ============================

git status

echo.
echo Adding all changes...
git add .

echo.
set /p msg=Enter commit message: 

git commit -m "%msg%"

echo.
echo Pushing to GitHub...
git push

echo.
echo Done! Your code is uploaded 🚀
pause
