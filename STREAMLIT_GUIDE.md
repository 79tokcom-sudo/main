# ST AI Launcher - Streamlit 버전

## Streamlit Cloud 배포 방법

### 1. GitHub에 파일 업로드
다음 파일들을 GitHub 저장소에 업로드하세요:
- `launcher.py` (메인 런처)
- `requirements.txt` (필요한 패키지)
- `version.json` (버전 정보)

### 2. Streamlit Cloud 배포

1. https://share.streamlit.io 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 저장소, 브랜치, 파일 선택:
   - Repository: `your-username/st-ai-launcher`
   - Branch: `main`
   - Main file path: `launcher.py`
5. "Deploy!" 클릭

### 3. 업데이트 URL 설정

`launcher.py` 파일에서 다음 부분을 수정:

```python
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/version.json"
```

실제 GitHub 저장소 주소로 변경하세요.

예시:
```python
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/johndoe/st-ai-launcher/main/version.json"
```

## 로컬에서 실행 방법

```bash
# 패키지 설치
pip install -r requirements.txt

# 실행
streamlit run launcher.py
```

## 버전 업데이트 방법

1. `version.json` 파일 수정:
```json
{
  "version": "1.0.1",
  "download_url": "https://raw.githubusercontent.com/your-username/your-repo/main/main_app.py",
  "release_notes": "버그 수정"
}
```

2. GitHub에 커밋 & 푸시
3. Streamlit Cloud가 자동으로 재배포
4. 사용자가 런처 접속 시 자동으로 업데이트 확인

## 주요 차이점 (Tkinter vs Streamlit)

### Tkinter (데스크톱)
- ❌ 웹에서 실행 불가
- ❌ Streamlit Cloud 호환 안 됨
- ✅ 독립 실행 파일 생성 가능
- ✅ 오프라인 실행 가능

### Streamlit (웹)
- ✅ 웹 브라우저에서 실행
- ✅ Streamlit Cloud 무료 호스팅
- ✅ 모바일에서도 접근 가능
- ✅ 업데이트 즉시 반영
- ❌ 인터넷 연결 필요

## 문제 해결

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### 업데이트 확인이 안 됨
- UPDATE_CHECK_URL이 올바른지 확인
- GitHub 저장소가 public인지 확인
- version.json 파일이 main 브랜치에 있는지 확인

### CORS 오류
GitHub raw URL 사용 시 CORS 문제가 없지만, 
자체 서버 사용 시 CORS 헤더 추가 필요:
```python
Access-Control-Allow-Origin: *
```

## 데스크톱 앱이 필요한 경우

Streamlit은 웹 기반이므로, 데스크톱 앱이 필요하다면:

1. **Electron + Streamlit**: 웹앱을 데스크톱으로 패키징
2. **PyQt/PySide**: 완전한 데스크톱 GUI
3. **Tkinter**: 가벼운 데스크톱 GUI (로컬에서만)

웹에 올리려면 Streamlit이 가장 좋은 선택입니다!
