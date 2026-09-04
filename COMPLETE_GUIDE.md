# ST AI 로봇박사 - 완전 통합 버전 가이드

## 🎉 완성!

**모든 기능이 main.py 한 파일에 통합되었습니다!**

```
main.py 하나로:
✅ 런처 기능
✅ GitHub Releases 자동 업데이트
✅ 진행률 표시
✅ 주식 AI 분석
✅ 암세포 AI 분석
✅ 대시보드
✅ 설정 관리
```

## 📁 파일 구조

```
your-repo/
├── main.py              # 🎯 전체 통합 파일!
├── requirements.txt     # 필요한 패키지
└── README.md           # 설명서
```

## 🚀 빠른 시작

### 1. main.py 설정

파일 상단의 설정을 수정하세요:

```python
# main.py 10-14줄
LAUNCHER_VERSION = "1.0.0"
GITHUB_USER = "79tokcom-sudo"           # ← 본인 GitHub ID
GITHUB_REPO = "st_ai_stock"             # ← 본인 저장소명
DEFAULT_RELEASE_TAG = "v1.0.0"
ASSET_NAME = "main_app.zip"
```

### 2. GitHub에 업로드

```bash
git add main.py requirements.txt
git commit -m "ST AI 로봇박사 통합 버전"
git push
```

### 3. GitHub Release 생성

1. GitHub 저장소 → "Releases" → "Create a new release"
2. Tag: `v1.0.0` (또는 `v1.0.1` 등)
3. Title: `Version 1.0.0`
4. "Attach binaries" → `main_app.zip` 업로드
   - **주의**: ZIP 파일 안에 앱 파일들이 들어있어야 함
5. "Publish release" 클릭

### 4. Streamlit Cloud 배포

1. https://share.streamlit.io 접속
2. "New app" 클릭
3. 설정:
   - Repository: `79tokcom-sudo/st_ai_stock`
   - Branch: `main`
   - Main file path: `main.py`
4. Deploy!

## 🎮 동작 흐름

### 첫 실행
```
[앱 시작]
    ↓
[🚀 런처 화면]
    ↓
[자동 업데이트 확인]
    ↓
[최신 버전?]
  ↙        ↘
YES         NO
 ↓          ↓
[시작하기]  [업데이트 UI]
 ↓          ↓
[메인 앱]   [다운로드 0-100%]
           ↓
          [설치 완료]
           ↓
          [메인 앱]
```

### 런처 화면 (최신 버전)
```
┌────────────────────────┐
│  🩺 ST AI 로봇박사     │
│ 암세포 사멸 + 증권 AI   │
│                        │
│ 📁 설치 경로           │
│ C:\Users\...\ST_AI...  │
│ ────────────────────   │
│ 🔍 업데이트 확인 중... │
│                        │
│ ✅ 최신 버전: 1.0.0    │
│ 🚀 준비 완료!          │
│                        │
│   [🚀 시작하기]        │
└────────────────────────┘
```

### 업데이트 있을 때
```
┌────────────────────────┐
│  🩺 ST AI 로봇박사     │
│                        │
│ 📦 새 버전 v1.0.1 발견!│
│                        │
│ 📝 업데이트 내용 보기  │
│ - 버그 수정            │
│ - 새로운 기능 추가     │
│                        │
│ 💡 자동으로 실행됩니다 │
│                        │
│ [⬇️ 업데이트 시작]     │
│ [⏭️ 건너뛰기]          │
└────────────────────────┘
        ↓
┌────────────────────────┐
│ 다운로드 준비 중...    │
│ main_app.zip           │
│ ████░░░░░░░░ 45%      │
└────────────────────────┘
        ↓
┌────────────────────────┐
│ ✅ 업데이트 완료!      │
│ 🎈🎈🎈               │
└────────────────────────┘
        ↓
[메인 앱 자동 실행]
```

### 메인 앱 화면
```
사이드바:              메인 화면:
┌──────────────┐      ┌────────────────────┐
│🩺 ST AI      │      │ 🩺 ST AI 로봇박사  │
│버전: 1.0.0   │      │                    │
│──────────────│      │ 프로젝트 진행률: 85%│
│⬅️ 런처로     │      │ AI 정확도: 94.2%   │
│──────────────│      │ 분석 완료: 1,234건 │
│메뉴          │      │                    │
│🏠 홈         │      │ [대시보드] [분석]  │
│📈 주식 분석  │      │                    │
│🔬 암세포 AI  │      │ (차트 및 데이터)   │
│⚙️ 설정      │      │                    │
└──────────────┘      └────────────────────┘
```

## 🔄 업데이트 방법

### 앱 업데이트하기

1. **main.py 수정** (새 기능 추가, 버그 수정 등)

2. **버전 번호 변경**:
```python
# main.py 상단
LAUNCHER_VERSION = "1.0.1"  # 1.0.0 → 1.0.1
```

3. **GitHub에 푸시**:
```bash
git add main.py
git commit -m "Update to v1.0.1"
git push
```

4. **GitHub Release 생성**:
   - Tag: `v1.0.1`
   - `main_app.zip` 업로드

5. **Streamlit Cloud 자동 재배포**
   - 푸시하면 자동으로 재배포됨

6. **사용자 경험**:
   - 사용자가 앱 접속
   - 런처에서 자동으로 `v1.0.1` 발견
   - "업데이트 시작" 클릭
   - 진행률 0-100% 표시
   - 100% 완료 시 메인 앱 자동 실행

## 💡 주요 기능 설명

### 1️⃣ 런처 (자동 업데이트)
- GitHub Releases API로 최신 버전 확인
- `main_app.zip` 다운로드 및 자동 설치
- 진행률 표시
- 업데이트 완료 후 메인 앱 자동 실행

### 2️⃣ 메인 앱 - 홈
- 대시보드 (진행률, 정확도, 통계)
- 실시간 차트
- AI 분석 시뮬레이션

### 3️⃣ 메인 앱 - 주식 분석
- 종목 코드 입력
- AI 예측 점수
- 매수/매도 추천
- 최근 분석 종목 리스트

### 4️⃣ 메인 앱 - 암세포 AI
- 이미지/데이터 업로드
- AI 분석 (전처리 → 패턴 분석 → 검출)
- 분석 결과 (양성/음성, 신뢰도, 위험도)

### 5️⃣ 메인 앱 - 설정
- 테마 설정
- 알림 설정
- 데이터 보관 기간 설정

## 🎨 커스터마이징

### 메인 앱 코드 수정

`main_app()` 함수에서 페이지별로 코드를 수정하세요:

```python
def main_app():
    # ...
    
    if page == "🏠 홈":
        st.title("🩺 ST AI 로봇박사")
        
        # 여기에 홈 화면 코드 추가
        # 예: 데이터베이스 연결, API 호출 등
    
    elif page == "📈 주식 분석":
        st.title("📈 주식 AI 분석")
        
        # 여기에 주식 분석 코드 추가
        # 예: yfinance 사용, 실시간 데이터 가져오기
        
        # import yfinance as yf
        # data = yf.download(ticker)
        # st.line_chart(data['Close'])
    
    elif page == "🔬 암세포 AI":
        # 여기에 암세포 분석 코드 추가
        # 예: TensorFlow/PyTorch 모델 로드 및 예측
```

### 런처 스타일 변경

```python
def show_launcher():
    st.markdown("""
    <style>
        .launcher-title {
            color: #FF6B6B;  /* 색상 변경 */
            font-size: 4rem;  /* 크기 변경 */
        }
    </style>
    """, unsafe_allow_html=True)
```

## 📦 main_app.zip 구조

Release에 업로드할 `main_app.zip`은 다음과 같이 구성:

```
main_app.zip
├── app_data/           # 앱 데이터 폴더
│   ├── models/        # AI 모델 파일
│   ├── config/        # 설정 파일
│   └── cache/         # 캐시 데이터
├── assets/            # 리소스 파일
│   ├── images/
│   └── icons/
└── version.txt        # 버전 정보 (자동 생성)
```

**주의**: ZIP 파일은 실제 앱 데이터만 포함하고, `main.py`는 포함하지 마세요!
(main.py는 Streamlit Cloud에서 실행되는 파일)

## 🐛 문제 해결

### Q: "Release에서 main_app.zip 파일을 찾을 수 없습니다"
A:
1. GitHub 저장소 → Releases 확인
2. 최신 릴리즈에 `main_app.zip` 업로드 되었는지 확인
3. 파일명이 정확히 `main_app.zip`인지 확인 (대소문자 구분)

### Q: 업데이트가 확인되지 않습니다
A:
1. `LAUNCHER_VERSION`과 Release Tag 버전 비교
2. Release Tag가 `v1.0.1` 형식인지 확인
3. GitHub API 접근 제한 확인 (시간당 60회)

### Q: 다운로드는 되는데 설치가 안 됩니다
A:
1. ZIP 파일이 손상되지 않았는지 확인
2. 압축 해제 권한 확인
3. 디스크 공간 확인

### Q: 메인 앱이 표시되지 않습니다
A:
1. `st.session_state.launcher_done` 값 확인
2. 브라우저 콘솔에서 오류 확인
3. Streamlit Cloud 로그 확인

## ✅ 배포 체크리스트

배포 전 확인:
- [ ] `GITHUB_USER`와 `GITHUB_REPO` 수정
- [ ] `LAUNCHER_VERSION` 설정
- [ ] `main.py`에 실제 앱 코드 작성
- [ ] `requirements.txt`에 필요한 패키지 추가
- [ ] GitHub에 푸시
- [ ] GitHub Release 생성 (태그: v1.0.0)
- [ ] `main_app.zip` 업로드
- [ ] Streamlit Cloud 배포
- [ ] 업데이트 테스트

완료! 🎉

## 📞 지원

문제가 발생하면:
1. Streamlit Cloud 로그 확인
2. GitHub Issues에 문의
3. 커뮤니티 포럼 검색

---

**만든 이**: ST AI Team  
**프로젝트**: 암세포 사멸 + 증권 AI 2030 프로젝트  
**버전**: 1.0.0
