# -*- coding: utf-8 -*-
"""
ST AI Launcher - 통합 버전
- 런처에서 업데이트 확인
- 업데이트 완료 후 자동으로 메인 앱 실행
"""
import os
import json
import urllib.request
import shutil
import time
import streamlit as st

# ===============================
# 설정
# ===============================
CURRENT_VERSION = "1.0.0"
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/version.json"
MAIN_APP_PATH = "main.py"

# ===============================
# 세션 상태 초기화
# ===============================
if 'update_checked' not in st.session_state:
    st.session_state.update_checked = False
if 'needs_update' not in st.session_state:
    st.session_state.needs_update = False
if 'latest_version' not in st.session_state:
    st.session_state.latest_version = CURRENT_VERSION
if 'download_url' not in st.session_state:
    st.session_state.download_url = None
if 'show_launcher' not in st.session_state:
    st.session_state.show_launcher = True
if 'update_completed' not in st.session_state:
    st.session_state.update_completed = False

# ===============================
# 함수
# ===============================
def check_for_updates():
    """업데이트 확인"""
    try:
        with urllib.request.urlopen(UPDATE_CHECK_URL, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            latest_version = data.get("version", CURRENT_VERSION)
            download_url = data.get("download_url", "")
            
            current_parts = [int(x) for x in CURRENT_VERSION.split(".")]
            latest_parts = [int(x) for x in latest_version.split(".")]
            
            return latest_parts > current_parts, latest_version, download_url
    except Exception as e:
        return False, CURRENT_VERSION, None

def download_update(url):
    """업데이트 다운로드"""
    try:
        temp_path = MAIN_APP_PATH + ".tmp"
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        with urllib.request.urlopen(url, timeout=30) as response:
            total_size = int(response.headers.get('Content-Length', 0))
            downloaded = 0
            
            with open(temp_path, 'wb') as f:
                while True:
                    chunk = response.read(8192)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        progress = downloaded / total_size
                        progress_bar.progress(progress)
                        status_text.text(f"다운로드 중... {int(progress * 100)}%")
        
        # 백업 및 교체
        if os.path.exists(MAIN_APP_PATH):
            backup_path = MAIN_APP_PATH + ".backup"
            if os.path.exists(backup_path):
                os.remove(backup_path)
            shutil.move(MAIN_APP_PATH, backup_path)
        
        shutil.move(temp_path, MAIN_APP_PATH)
        
        progress_bar.progress(1.0)
        status_text.text("다운로드 완료! 100% ✅")
        
        return True
    except Exception as e:
        st.error(f"다운로드 실패: {e}")
        return False

def load_and_run_main():
    """main.py 로드 및 실행"""
    if not os.path.exists(MAIN_APP_PATH):
        st.error(f"❌ {MAIN_APP_PATH} 파일을 찾을 수 없습니다.")
        st.info("💡 업데이트를 먼저 진행해주세요.")
        return False
    
    try:
        # main.py 내용 읽기
        with open(MAIN_APP_PATH, 'r', encoding='utf-8') as f:
            main_code = f.read()
        
        # main.py 실행
        exec(main_code, globals())
        return True
    except Exception as e:
        st.error(f"메인 앱 실행 오류: {e}")
        import traceback
        st.code(traceback.format_exc())
        return False

# ===============================
# 메인 로직
# ===============================

# 런처 화면을 보여줄지 결정
if st.session_state.show_launcher:
    # ===============================
    # 런처 UI
    # ===============================
    st.set_page_config(
        page_title="ST AI Launcher",
        page_icon="🚀",
        layout="centered"
    )
    
    st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #1f77b4;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        div.stButton > button {
            width: 100%;
            height: 3rem;
            font-size: 1.1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-title">🚀 천신대왕 ST AI 런처</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; color: #666; margin-bottom: 2rem;">
        현재 버전: <strong>{CURRENT_VERSION}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # 자동 업데이트 확인 (최초 1회)
    if not st.session_state.update_checked:
        with st.spinner("🔍 업데이트 확인 중..."):
            needs_update, latest_version, download_url = check_for_updates()
            st.session_state.update_checked = True
            st.session_state.needs_update = needs_update
            st.session_state.latest_version = latest_version
            st.session_state.download_url = download_url
            time.sleep(1)
            st.rerun()
    
    # 업데이트 상태 표시
    if st.session_state.needs_update and not st.session_state.update_completed:
        st.warning(f"📦 새 버전 **{st.session_state.latest_version}** 발견!")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.info("💡 업데이트를 진행하면 자동으로 메인 앱이 실행됩니다.")
        
        with col2:
            if st.button("⬇️ 업데이트", type="primary", use_container_width=True):
                with st.spinner("업데이트 진행 중..."):
                    if download_update(st.session_state.download_url):
                        st.success("✅ 업데이트 완료! (100%)")
                        st.balloons()
                        st.session_state.update_completed = True
                        st.session_state.needs_update = False
                        time.sleep(2)
                        
                        # 메인 앱으로 전환
                        st.session_state.show_launcher = False
                        st.rerun()
        
        st.divider()
        
        # 업데이트 없이 실행
        if st.button("⏭️ 업데이트 건너뛰고 실행", use_container_width=True):
            st.session_state.show_launcher = False
            st.rerun()
    
    else:
        # 최신 버전일 때
        st.success("✅ 최신 버전 사용 중")
        
        st.divider()
        
        # 메인 앱 실행 버튼
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <p style="font-size: 1.2rem; color: #555;">
                준비가 완료되었습니다!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 메인 앱 실행", type="primary", use_container_width=True, key="run_main"):
            with st.spinner("🔄 메인 앱 로딩 중..."):
                time.sleep(1)
                st.session_state.show_launcher = False
                st.rerun()
        
        st.divider()
        
        # 수동 업데이트 확인
        if st.button("🔄 업데이트 다시 확인", use_container_width=True):
            st.session_state.update_checked = False
            st.rerun()
    
    # 정보
    with st.expander("ℹ️ 상세 정보"):
        st.markdown(f"""
        **현재 버전**: {CURRENT_VERSION}  
        **최신 버전**: {st.session_state.latest_version}  
        **업데이트 필요**: {'예' if st.session_state.needs_update else '아니오'}  
        **메인 앱 파일**: {MAIN_APP_PATH} ({'존재' if os.path.exists(MAIN_APP_PATH) else '없음'})  
        **업데이트 URL**: {UPDATE_CHECK_URL}
        """)
    
    st.markdown("---")
    st.markdown(
        '<div style="text-align: center; color: #888; font-size: 0.8rem;">© 2026 천신대왕 ST AI</div>',
        unsafe_allow_html=True
    )

else:
    # ===============================
    # 메인 앱 실행
    # ===============================
    
    # 런처로 돌아가기 버튼 (사이드바)
    with st.sidebar:
        st.markdown("### 🚀 런처")
        if st.button("⬅️ 런처로 돌아가기", use_container_width=True):
            st.session_state.show_launcher = True
            st.rerun()
        
        st.divider()
        st.caption(f"버전: {CURRENT_VERSION}")
    
    # 메인 앱 로드 및 실행
    load_and_run_main()
