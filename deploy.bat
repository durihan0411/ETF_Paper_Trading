@echo off
REM SOXL-VXX 리밸런싱 계산기 배포 스크립트 (Windows)

echo.
echo ================================================
echo   SOXL-VXX 리밸런싱 계산기 배포 시작
echo ================================================
echo.

REM Git 초기화 확인
if not exist ".git" (
    echo [1/5] Git 저장소 초기화 중...
    git init
    git branch -M main
)

REM 파일 추가
echo [2/5] 파일 추가 중...
git add .

REM 커밋 메시지 입력
echo.
set /p commit_msg="커밋 메시지를 입력하세요 (기본: Update): "
if "%commit_msg%"=="" set commit_msg=Update

REM 커밋
echo [3/5] 커밋 중...
git commit -m "%commit_msg%"

REM 원격 저장소 확인
git remote | findstr /C:"origin" >nul
if errorlevel 1 (
    echo.
    echo 원격 저장소가 설정되지 않았습니다.
    set /p repo_url="GitHub 저장소 URL을 입력하세요: "
    git remote add origin %repo_url%
)

REM 푸시
echo [4/5] GitHub에 푸시 중...
git push -u origin main

echo.
echo [5/5] 배포 준비 완료!
echo.
echo ================================================
echo   다음 단계:
echo ================================================
echo.
echo 1. Vercel: https://vercel.com
echo    - New Project 클릭
echo    - GitHub 저장소 선택
echo    - Deploy 클릭
echo.
echo 2. GitHub Pages: 저장소 Settings ^> Pages
echo    - Source: main 브랜치 선택
echo    - Save 클릭
echo.
echo 3. Netlify: https://netlify.com
echo    - Import project 클릭
echo    - GitHub 저장소 선택
echo    - Deploy site 클릭
echo.
echo 배포 가이드: DEPLOYMENT_GUIDE.md
echo.
pause
