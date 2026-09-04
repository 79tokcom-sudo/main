# ST AI Launcher - 통합 버전 사용 가이드

## ✅ 이 방법의 특징

런처와 메인 앱이 **하나의 파일**에 통합되어 있습니다.
- 런처 화면에서 업데이트 확인
- 업데이트 100% 완료 시 자동으로 메인 앱 실행
- 메인 앱에서 런처로 돌아가기 가능

## 📁 GitHub 파일 구조

```
your-repo/
├── launcher_integrated.py  # 런처 (이 파일을 메인으로 배포)
├── main.py                 # 실제 앱 (업데이트 대상)
├── version.json            # 버전 정보
└── requirements.txt        # 필요한 패키지
```

## 🚀 배포 방법

### 1. GitHub에 파일 업로드

```bash
# launcher_integrated.py의 이름을 원하는 대로 변경 (예: app.py)
mv launcher_integrated.py app.py

# Git 추가
git add app.py main.py version.json requirements.txt
git commit -m "Add integrated launcher"
git push
```

### 2. Streamlit Cloud 배포

1. https://share.streamlit.io 접속
2. "New app" 클릭
3. 설정:
   - Repository: `your-username/st-ai-stock`
   - Branch: `main`
   - Main file path: `app.py` (또는 `launcher_integrated.py`)
4. Deploy!

### 3. 런처 설정 수정

`launcher_integrated.py` (또는 `app.py`) 파일에서:

```python
CURRENT_VERSION = "1.0.0"  # 런처 버전
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/your-username/st-ai-stock/main/version.json"
MAIN_APP_PATH = "main.py"  # 업데이트할 파일
```

실제 GitHub 정보로 변경:
```python
CURRENT_VERSION = "1.0.0"
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/johndoe/st-ai-stock/main/version.json"
MAIN_APP_PATH = "main.py"
```

## 🔄 업데이트 방법

### main.py 업데이트 하기

1. **main.py 수정** (실제 앱 코드 변경)

2. **version.json 수정**:
```json
{
  "version": "1.0.1",
  "download_url": "https://raw.githubusercontent.com/johndoe/st-ai-stock/main/main.py",
  "release_notes": "새로운 기능 추가"
}
```

3. **GitHub에 푸시**:
```bash
git add main.py version.json
git commit -m "Update to v1.0.1"
git push
```

4. **사용자 경험**:
   - 사용자가 앱 접속
   - 런처가 자동으로 업데이트 확인
   - "새 버전 발견!" 메시지 표시
   - "업데이트" 버튼 클릭
   - 진행률 0% → 100% 표시
   - **100% 완료 시 자동으로 메인 앱 실행** ✨

## 💡 동작 흐름

```
[사용자 접속]
      ↓
[런처 화면 표시]
      ↓
[자동 업데이트 확인]
      ↓
[업데이트 있음?]
  ↙          ↘
YES          NO
  ↓           ↓
[업데이트 다운로드]  [메인 앱 실행 버튼]
  ↓           ↓
[진행률 표시 0-100%] [버튼 클릭]
  ↓           ↓
[100% 완료]   [메인 앱 실행]
  ↓
[자동으로 메인 앱 실행]
```

## 🎮 사용자 화면

### 1. 런처 화면 (최신 버전)
```
🚀 천신대왕 ST AI 런처
현재 버전: 1.0.0

✅ 최신 버전 사용 중
─────────────────────
준비가 완료되었습니다!

[🚀 메인 앱 실행]
─────────────────────
[🔄 업데이트 다시 확인]
```

### 2. 런처 화면 (업데이트 있음)
```
🚀 천신대왕 ST AI 런처
현재 버전: 1.0.0

📦 새 버전 1.0.1 발견!

💡 업데이트를 진행하면 자동으로 메인 앱이 실행됩니다.

[⬇️ 업데이트]
─────────────────────
다운로드 중... 45%
████████░░░░░░░░
─────────────────────
[⏭️ 업데이트 건너뛰고 실행]
```

### 3. 업데이트 완료
```
✅ 업데이트 완료! (100%)
🎈🎈🎈

🔄 메인 앱 로딩 중...

→ 자동으로 메인 앱 실행됨
```

### 4. 메인 앱 실행 중
```
사이드바:
┌─────────────────┐
│ 🚀 런처         │
│ [⬅️ 런처로 돌아가기] │
│ ───────────── │
│ 버전: 1.0.0   │
└─────────────────┘

메인 화면:
(여기에 실제 main.py 내용 표시)
```

## ⚙️ 고급 설정

### 자동 업데이트 건너뛰기

사용자가 업데이트를 원하지 않으면:
- "⏭️ 업데이트 건너뛰고 실행" 버튼 클릭
- 바로 메인 앱 실행

### 런처로 돌아가기

메인 앱 실행 중:
- 사이드바의 "⬅️ 런처로 돌아가기" 클릭
- 다시 업데이트 확인 가능

## 🐛 문제 해결

### Q: 메인 앱이 실행되지 않습니다
A: 
1. `main.py` 파일이 같은 폴더에 있는지 확인
2. `main.py`에 문법 오류가 없는지 확인
3. 에러 메시지 확인

### Q: 업데이트가 100%인데 앱이 안 열립니다
A:
1. 2초 대기 후 자동 실행됨
2. 수동으로 "🚀 메인 앱 실행" 버튼 클릭

### Q: "파일을 찾을 수 없습니다" 오류
A:
1. `version.json`의 `download_url` 확인
2. GitHub 저장소가 public인지 확인
3. URL에 오타가 없는지 확인

## 📝 체크리스트

배포 전 확인사항:
- [ ] `UPDATE_CHECK_URL`을 실제 GitHub URL로 변경
- [ ] `version.json` 파일 생성 및 업로드
- [ ] `main.py` 파일 존재 확인
- [ ] `requirements.txt` 생성
- [ ] Streamlit Cloud에서 배포
- [ ] 배포 후 업데이트 테스트

완료! 🎉
