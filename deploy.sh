#!/bin/bash

# SOXL-VXX 리밸런싱 계산기 배포 스크립트

echo "🚀 SOXL-VXX 리밸런싱 계산기 배포 시작..."
echo ""

# 색상 정의
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Git 초기화 확인
if [ ! -d ".git" ]; then
    echo -e "${BLUE}📦 Git 저장소 초기화 중...${NC}"
    git init
    git branch -M main
fi

# 파일 추가
echo -e "${BLUE}📝 파일 추가 중...${NC}"
git add .

# 커밋 메시지 입력
echo ""
read -p "커밋 메시지를 입력하세요 (기본: Update): " commit_msg
commit_msg=${commit_msg:-Update}

# 커밋
echo -e "${BLUE}💾 커밋 중...${NC}"
git commit -m "$commit_msg"

# 원격 저장소 확인
if ! git remote | grep -q "origin"; then
    echo ""
    echo -e "${RED}⚠️  원격 저장소가 설정되지 않았습니다.${NC}"
    read -p "GitHub 저장소 URL을 입력하세요: " repo_url
    git remote add origin $repo_url
fi

# 푸시
echo -e "${BLUE}📤 GitHub에 푸시 중...${NC}"
git push -u origin main

echo ""
echo -e "${GREEN}✅ 배포 준비 완료!${NC}"
echo ""
echo "다음 단계:"
echo "1. Vercel: https://vercel.com → New Project → GitHub 저장소 선택"
echo "2. GitHub Pages: 저장소 Settings → Pages → Branch: main 선택"
echo "3. Netlify: https://netlify.com → Import project → GitHub 저장소 선택"
echo ""
echo -e "${BLUE}배포 가이드: DEPLOYMENT_GUIDE.md${NC}"
