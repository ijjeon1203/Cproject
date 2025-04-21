
# PyCharm 프로젝트의 불필요한 파일/폴더 목록

제외 대상	설명
.idea/	PyCharm 설정 폴더 (개인 설정 포함, 공유 비권장)
__pycache__/	파이썬 바이트코드 캐시
*.pyc, *.pyo	파이썬 컴파일 결과물
.DS_Store	macOS에서 생성되는 폴더 메타파일
*.log, *.swp	로그, Vim 임시파일 등
venv/ 또는 .venv/	가상환경 (보통 Git에 올리지 않고 requirements.txt로 대체)


# requirements.txt
아래 명령어로 현재 가상환경에서 설치된 패키지를 기준으로 파일 생성할 수 있습니다: