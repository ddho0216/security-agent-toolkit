# 5-1 의 안전한 읽기 함수를 불러온다
from config_loader import load_json

# 시험할 경로 세 개
PATHS = [
    # 정상 파일
    "config/users.json",
    # 이름을 잘못 적은 경로 (없는 파일)
    "config/users_typo.json",
    # 일부러 깨진 파일
    "config/users_broken.json",
]

# 경로를 하나씩 꺼낸다
for path in PATHS:
    # 안전하게 읽고, 실패하면 빈 딕셔너리
    users = load_json(path, {})
    # seoyeon 이 있으면
    if "seoyeon" in users:
        print(path, "-> 사용자", len(users), "명을 읽음, 판정을 계속한다")
    # 없으면
    else:
        print(path, "-> 사용자 0 명, 등록된 사용자가 없다")