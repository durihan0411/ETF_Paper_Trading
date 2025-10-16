# 배포 가이드 (Deployment Guide)

SOXL-VXX 리밸런싱 계산기를 배포하는 방법을 단계별로 안내합니다.

## 🚀 빠른 배포 (Vercel - 추천)

### 방법 1: Vercel CLI 사용 (가장 빠름)

#### 1단계: Vercel CLI 설치

```bash
npm install -g vercel
```

#### 2단계: 로그인

```bash
vercel login
```

#### 3단계: 배포

```bash
cd ETF_Paper_Trading
vercel
```

**질문에 답변:**
- Set up and deploy? → **Y**
- Which scope? → 본인의 계정 선택
- Link to existing project? → **N**
- Project name? → `soxl-vxx-calculator` (원하는 이름)
- Directory? → `./`
- Override settings? → **N**

#### 4단계: 프로덕션 배포

```bash
vercel --prod
```

#### 5단계: 완료!

배포 URL이 표시됩니다:
```
https://soxl-vxx-calculator.vercel.app
```

---

### 방법 2: Vercel 웹 인터페이스 사용

#### 1단계: GitHub 저장소 준비

```bash
# 현재 디렉토리에서
git init
git add .
git commit -m "Initial commit: SOXL-VXX Rebalancing Calculator"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/soxl-vxx-calculator.git
git push -u origin main
```

#### 2단계: Vercel 접속

1. [https://vercel.com](https://vercel.com) 접속
2. "Sign Up" 또는 "Log In"
3. GitHub 계정으로 로그인

#### 3단계: 새 프로젝트 생성

1. "Add New..." → "Project" 클릭
2. GitHub 저장소 목록에서 `soxl-vxx-calculator` 선택
3. "Import" 클릭

#### 4단계: 프로젝트 설정

**Configure Project:**
- **Framework Preset**: Other
- **Root Directory**: `ETF_Paper_Trading`
- **Build Command**: (비워두기)
- **Output Directory**: (비워두기)

**Environment Variables**: (필요 없음)

#### 5단계: 배포

"Deploy" 버튼 클릭

#### 6단계: 완료!

배포가 완료되면 자동으로 URL이 생성됩니다:
```
https://soxl-vxx-calculator.vercel.app
```

---

## 🌐 GitHub Pages 배포

### 1단계: GitHub 저장소 생성

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/soxl-vxx-calculator.git
git push -u origin main
```

### 2단계: index.html 생성

```bash
cd ETF_Paper_Trading
cp Rebalancing_Calculator.html index.html
git add index.html
git commit -m "Add index.html for GitHub Pages"
git push
```

### 3단계: GitHub Pages 활성화

1. GitHub 저장소 페이지로 이동
2. **Settings** 클릭
3. 왼쪽 메뉴에서 **Pages** 클릭
4. **Source** 섹션에서:
   - Branch: `main` 선택
   - Folder: `/ (root)` 선택
5. **Save** 클릭

### 4단계: 완료!

배포 URL:
```
https://YOUR_USERNAME.github.io/soxl-vxx-calculator/
```

**참고**: 배포에 1~2분 정도 소요될 수 있습니다.

---

## 📦 Netlify 배포

### 1단계: Netlify 접속

1. [https://netlify.com](https://netlify.com) 접속
2. "Sign up" 또는 "Log in"
3. GitHub 계정으로 로그인

### 2단계: 새 사이트 생성

1. "Add new site" → "Import an existing project" 클릭
2. GitHub 연결
3. 저장소 목록에서 `soxl-vxx-calculator` 선택

### 3단계: 빌드 설정

**Build settings:**
- **Base directory**: `ETF_Paper_Trading`
- **Build command**: (비워두기)
- **Publish directory**: (비워두기)

### 4단계: 배포

"Deploy site" 버튼 클릭

### 5단계: 완료!

배포 URL:
```
https://soxl-vxx-calculator.netlify.app
```

---

## 🔄 업데이트 배포

### Vercel

```bash
cd ETF_Paper_Trading
git add .
git commit -m "Update: 새로운 기능 추가"
git push
```

Vercel이 자동으로 변경사항을 감지하고 재배포합니다.

### GitHub Pages

```bash
git add .
git commit -m "Update: 새로운 기능 추가"
git push
```

GitHub Pages도 자동으로 업데이트됩니다.

### Netlify

```bash
git add .
git commit -m "Update: 새로운 기능 추가"
git push
```

Netlify가 자동으로 재배포합니다.

---

## 🧪 로컬 테스트

배포 전 로컬에서 테스트:

### Python HTTP 서버

```bash
cd ETF_Paper_Trading
python -m http.server 8000
```

브라우저에서 접속:
```
http://localhost:8000/Rebalancing_Calculator.html
```

### Node.js HTTP 서버

```bash
cd ETF_Paper_Trading
npx http-server . -p 8080
```

브라우저에서 접속:
```
http://localhost:8080/Rebalancing_Calculator.html
```

---

## 🎨 커스텀 도메인 연결 (선택사항)

### Vercel

1. Vercel 대시보드에서 프로젝트 선택
2. **Settings** → **Domains** 클릭
3. 원하는 도메인 입력
4. DNS 설정 안내에 따라 도메인 설정

### Netlify

1. Netlify 대시보드에서 사이트 선택
2. **Domain settings** 클릭
3. **Add custom domain** 클릭
4. 도메인 입력 및 DNS 설정

---

## 📊 배포 상태 확인

### Vercel

```
https://vercel.com/dashboard
```

### GitHub Pages

```
https://github.com/YOUR_USERNAME/soxl-vxx-calculator/settings/pages
```

### Netlify

```
https://app.netlify.com/sites/YOUR_SITE_ID
```

---

## 🔧 문제 해결

### Vercel 배포 실패

```bash
# 캐시 삭제 후 재배포
vercel --force
```

### GitHub Pages 404 에러

1. `index.html` 파일이 루트에 있는지 확인
2. GitHub Pages 설정 확인
3. 브라우저 캐시 삭제 후 재시도

### Netlify 배포 실패

1. Build logs 확인
2. Root directory 설정 확인
3. 파일명 대소문자 확인

---

## 📝 체크리스트

배포 전 확인사항:

- [ ] 모든 파일이 저장소에 포함되어 있는가?
- [ ] `vercel.json` 또는 `netlify.toml` 설정이 올바른가?
- [ ] 로컬에서 테스트가 완료되었는가?
- [ ] README.md가 업데이트되었는가?
- [ ] 라이선스 파일이 있는가?

---

## 🎉 배포 완료!

배포가 완료되면 다음을 공유하세요:

1. 배포 URL
2. GitHub 저장소 링크
3. 프로젝트 설명

**예시:**
```
🎉 SOXL-VXX 리밸런싱 계산기 배포 완료!

📱 사용하기: https://soxl-vxx-calculator.vercel.app
💻 소스코드: https://github.com/YOUR_USERNAME/soxl-vxx-calculator
📖 문서: https://github.com/YOUR_USERNAME/soxl-vxx-calculator#readme

주요 기능:
✅ 5% 단위 포트폴리오 비율 조정
✅ 다년도 데이터 관리
✅ 실시간 리밸런싱 계산
✅ 투자 히스토리 추적
```

---

## 📧 지원

배포 중 문제가 발생하면:

1. GitHub Issues에 문의
2. 로그 파일 확인
3. 공식 문서 참조

**유용한 링크:**
- [Vercel 문서](https://vercel.com/docs)
- [GitHub Pages 문서](https://docs.github.com/en/pages)
- [Netlify 문서](https://docs.netlify.com)
