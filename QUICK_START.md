# 빠른 시작 가이드 (Quick Start Guide)

## 🚀 3분 안에 배포하기

### 옵션 1: Vercel (가장 빠름 - 추천)

#### 1단계: Vercel CLI 설치 및 배포

```bash
# Vercel CLI 설치
npm install -g vercel

# 로그인
vercel login

# 배포 (현재 디렉토리에서)
vercel
```

**질문에 답변:**
- Set up and deploy? → **Y**
- Which scope? → 본인 계정 선택
- Link to existing project? → **N**
- Project name? → `soxl-vxx-calculator`
- Directory? → `./`
- Override settings? → **N**

#### 2단계: 프로덕션 배포

```bash
vercel --prod
```

#### 3단계: 완료! 🎉

배포 URL이 표시됩니다:
```
https://soxl-vxx-calculator.vercel.app
```

---

### 옵션 2: GitHub + Vercel 웹 인터페이스

#### 1단계: GitHub에 푸시

```bash
# Git 초기화 (처음 한 번만)
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/soxl-vxx-calculator.git
git push -u origin main
```

#### 2단계: Vercel에서 배포

1. [https://vercel.com](https://vercel.com) 접속
2. "Add New..." → "Project" 클릭
3. GitHub 저장소 선택
4. "Deploy" 클릭

#### 3단계: 완료! 🎉

---

### 옵션 3: GitHub Pages (무료, 간단)

#### 1단계: index.html 생성

```bash
cp Rebalancing_Calculator.html index.html
git add index.html
git commit -m "Add index.html"
git push
```

#### 2단계: GitHub Pages 활성화

1. GitHub 저장소 → **Settings**
2. 왼쪽 메뉴 → **Pages**
3. Source: **main** 브랜치 선택
4. **Save** 클릭

#### 3단계: 완료! 🎉

배포 URL:
```
https://YOUR_USERNAME.github.io/soxl-vxx-calculator/
```

---

## 📱 배포 후 바로 사용하기

배포가 완료되면:

1. **URL 접속**: 배포된 URL로 이동
2. **포트폴리오 비율 설정**: 슬라이더로 원하는 비율 조정
3. **투자 데이터 입력**: 가격 및 주식 수 입력
4. **리밸런싱 계산**: 계산 버튼 클릭
5. **결과 확인 및 저장**: 조정 방안 확인 후 저장

---

## 🔄 업데이트 배포

변경사항을 배포하려면:

```bash
git add .
git commit -m "Update: 새로운 기능 추가"
git push
```

**Vercel/Netlify**: 자동으로 재배포됩니다.
**GitHub Pages**: 1~2분 후 자동 업데이트됩니다.

---

## 🛠️ 로컬 테스트

배포 전 로컬에서 테스트:

```bash
# Python HTTP 서버
python -m http.server 8000

# 또는 Node.js
npx http-server . -p 8080
```

브라우저에서 접속:
```
http://localhost:8000/Rebalancing_Calculator.html
```

---

## 📊 자동 배포 스크립트 사용

### Windows

```bash
deploy.bat
```

### Mac/Linux

```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 🎯 주요 기능

- ✅ **5% 단위 비율 조정**: 슬라이더로 포트폴리오 비율 설정
- ✅ **다년도 관리**: 2024~2027년 데이터 저장
- ✅ **실시간 계산**: 목표 비율로 리밸런싱 계산
- ✅ **히스토리 추적**: 월별 투자 내역 및 성과 분석
- ✅ **성과 시각화**: 차트로 포트폴리오 성과 확인

---

## 📖 상세 가이드

더 자세한 내용은 다음 문서를 참조하세요:

- **README.md**: 프로젝트 전체 설명
- **DEPLOYMENT_GUIDE.md**: 상세 배포 가이드
- **Rebalancing_Calculator.html**: 메인 계산기

---

## 🆘 문제 해결

### 배포가 안 될 때

1. **GitHub 저장소 확인**: 파일이 모두 푸시되었는지 확인
2. **로그 확인**: Vercel/Netlify 대시보드에서 빌드 로그 확인
3. **캐시 삭제**: 브라우저 캐시 삭제 후 재시도

### 404 에러

1. **index.html 확인**: GitHub Pages는 루트에 index.html 필요
2. **URL 확인**: 올바른 URL로 접속하는지 확인
3. **대소문자**: 파일명 대소문자 확인

---

## 📧 지원

문제가 발생하면:

1. GitHub Issues에 문의
2. 로그 파일 확인
3. 공식 문서 참조

---

## 🎉 성공!

배포가 완료되면 친구들과 공유하세요:

```
🎉 SOXL-VXX 리밸런싱 계산기 배포 완료!

📱 사용하기: https://your-url.vercel.app
💻 소스코드: https://github.com/YOUR_USERNAME/soxl-vxx-calculator

주요 기능:
✅ 5% 단위 포트폴리오 비율 조정
✅ 다년도 데이터 관리
✅ 실시간 리밸런싱 계산
✅ 투자 히스토리 추적
```

---

**즐거운 투자 되세요! 📈**
