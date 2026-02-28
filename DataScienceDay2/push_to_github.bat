@echo off
echo ========================================
echo Pushing to GitHub Repository
echo ========================================

REM Check if git is initialized
if not exist ".git" (
    echo Initializing Git repository...
    git init
    git remote add origin https://github.com/SIDDHARThMNC/DATA-SCIENCE-.git
    git branch -M main
)

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Added e-commerce data wrangling project with complete analysis"

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo Push completed successfully!
echo ========================================
pause
