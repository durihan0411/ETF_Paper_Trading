# SOXL-VXX 리밸런싱 계산기

SOXL과 VXX ETF의 포트폴리오 리밸런싱을 위한 웹 기반 계산기입니다.

## 📋 주요 기능

- 🎯 **사용자 정의 포트폴리오 비율**: 5% 단위로 비율 조정 (기본: 75% SOXL, 25% VXX)
- 📅 **다년도 데이터 관리**: 2024~2027년 데이터 저장 및 관리
- 💾 **데이터 저장/불러오기**: 년도/월별 데이터 저장 및 수정
- 📊 **실시간 리밸런싱 계산**: 현재 포트폴리오를 목표 비율로 조정
- 📈 **투자 히스토리 추적**: 월별 투자 내역 및 성과 분석
- 📊 **성과 시각화**: 포트폴리오 가치 및 수익률 차트

## 🚀 빠른 시작

### 로컬에서 실행

1. 파일 다운로드
2. `Rebalancing_Calculator.html` 파일을 브라우저에서 열기
3. 즉시 사용 가능!

## 🌐 배포하기

### 방법 1: Vercel (추천 - 무료, 간편)

#### 1단계: GitHub 저장소 생성

```bash
# 새 저장소 생성
git init
git add .
git commit -m "Initial commit: SOXL-VXX Rebalancing Calculator"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/soxl-vxx-calculator.git
git push -u origin main
```

#### 2단계: Vercel 배포

1. [Vercel](https://vercel.com) 접속
2. "New Project" 클릭
3. GitHub 저장소 선택
4. 설정:
   - **Framework Preset**: Other
   - **Root Directory**: `ETF_Paper_Trading`
   - **Build Command**: (비워두기)
   - **Output Directory**: (비워두기)
5. "Deploy" 클릭

#### 3단계: 완료!

배포가 완료되면 자동으로 URL이 생성됩니다:
```
https://your-project-name.vercel.app
```

### 방법 2: GitHub Pages (무료)

#### 1단계: 저장소 생성 및 푸시

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/soxl-vxx-calculator.git
git push -u origin main
```

#### 2단계: GitHub Pages 활성화

1. GitHub 저장소 페이지로 이동
2. **Settings** → **Pages** 클릭
3. **Source** 선택:
   - Branch: `main`
   - Folder: `/ (root)`
4. **Save** 클릭

#### 3단계: 파일 이동

GitHub Pages는 루트 디렉토리의 `index.html`을 찾으므로:

```bash
# index.html 생성 (Rebalancing_Calculator.html을 복사)
cp Rebalancing_Calculator.html index.html
git add index.html
git commit -m "Add index.html for GitHub Pages"
git push
```

#### 4단계: 완료!

배포 URL:
```
https://YOUR_USERNAME.github.io/soxl-vxx-calculator/
```

### 방법 3: Netlify (무료, 간편)

#### 1단계: Netlify 접속

1. [Netlify](https://netlify.com) 접속
2. "Add new site" → "Import an existing project"

#### 2단계: GitHub 연결

1. GitHub 저장소 선택
2. 설정:
   - **Base directory**: `ETF_Paper_Trading`
   - **Build command**: (비워두기)
   - **Publish directory**: (비워두기)
3. "Deploy site" 클릭

#### 3단계: 완료!

배포 URL:
```
https://your-project-name.netlify.app
```

## 📁 프로젝트 구조

```
ETF_Paper_Trading/
├── Rebalancing_Calculator.html    # 메인 계산기 (배포 파일)
├── Paper_Trading_Dashboard.html   # 모의투자 대시보드
├── soxl_vxx_paper_trading.py     # Python 시뮬레이션 스크립트
├── monthly_*.html                 # 1개월 리밸런싱 차트
├── quarterly_*.html               # 3개월 리밸런싱 차트
├── monthly_results_*.xlsx         # Excel 결과 파일
├── quarterly_results_*.xlsx       # Excel 결과 파일
└── README.md                      # 프로젝트 설명서
```

## 🛠️ 기술 스택

- **HTML5**: 웹 구조
- **CSS3**: 스타일링 및 반응형 디자인
- **JavaScript**: 동적 기능 및 계산
- **Chart.js**: 데이터 시각화
- **Plotly**: Python 차트 생성

## 📖 사용 가이드

### 1. 포트폴리오 비율 설정

```
SOXL 비율: [━━━━━━━━━●━━━━━━━━] 75%
VXX 비율:  [━━━━●━━━━━━━━━━━━━━] 25%
```

### 2. 투자 기간 선택

```
년도: [2025년 ▼]  월: [1월 ▼]
```

### 3. 현재 포트폴리오 입력

- SOXL 현재 가격 ($)
- SOXL 보유 주식 수
- VXX 현재 가격 ($)
- VXX 보유 주식 수

### 4. 리밸런싱 계산

"🔄 리밸런싱 계산" 버튼 클릭

### 5. 결과 확인 및 저장

- 조정 방안 확인
- "💾 리밸런싱 저장" 클릭

## 🔧 커스터마이징

### 비율 변경

`Rebalancing_Calculator.html` 파일에서 기본 비율 변경:

```javascript
let targetSoxlRatio = 75;  // SOXL 기본 비율
let targetVxxRatio = 25;   // VXX 기본 비율
```

### 년도 범위 확장

```html
<select id="yearSelect">
    <option value="2023">2023년</option>
    <option value="2024">2024년</option>
    <option value="2025" selected>2025년</option>
    <option value="2026">2026년</option>
    <option value="2027">2027년</option>
    <option value="2028">2028년</option>
</select>
```

## 📊 기능 상세

### 리밸런싱 계산

- 현재 포트폴리오 가치 계산
- 목표 비율에 따른 조정 방안 제시
- 매수/매도 주식 수 및 금액 표시

### 데이터 관리

- 년도/월별 데이터 저장
- 저장된 데이터 불러오기
- 데이터 수정 및 삭제

### 성과 분석

- 월별 투자 히스토리
- 포트폴리오 가치 추이 차트
- 월간 수익률 분석
- 총 수익률, 연간 수익률, 최대 낙폭 계산

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

MIT License

## 📧 문의

프로젝트에 대한 문의사항이 있으시면 이슈를 등록해주세요.

## 🙏 감사의 글

- Chart.js
- Plotly
- yfinance

---

**주의사항**: 이 계산기는 교육 및 모의투자 목적으로 제작되었습니다. 실제 투자 결정 전 전문가의 조언을 구하시기 바랍니다.
