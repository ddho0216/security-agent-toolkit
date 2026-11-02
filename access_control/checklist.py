import json
from datetime import datetime

TIME_FORMAT = "%Y-%m-%d %H:%M"


def load_state(path):
    with open(path, encoding="utf-8") as json_file:
        return json.load(json_file)


def check_employed(users):
    problems = []
    for name, info in users.items():
        # 1. info["employed"] 가 거짓이면 (if not …)
        if not info["employed"]:
        # 2.   name 을 problems 에 추가한다
            problems.append(name)
    return problems


def check_expired(exceptions, now):
    problems = []
    for exception in exceptions:
        # 3. exception["expires"] 를 TIME_FORMAT 으로 읽어 시각 expires_at 에 담는다 (datetime.strptime)
        expires_at = datetime.strptime(exception["expires"], TIME_FORMAT)
        # 4. expires_at 이 now 보다 이르거나 같으면 (<=)
        if expires_at <= now:
            # 5.   exception["id"] 를 problems 에 추가한다
            problems.append(exception["id"])
    return problems


def check_dept(users, role_dept):
    problems = []
    for name, info in users.items():
        # 6. role_dept 에서 info["role"] 의 부서를 찾아 expected_dept 에 담는다
        expected_dept = role_dept.get(info["role"])
        # 7. expected_dept 가 info["dept"] 와 다르면 (!=)
        if expected_dept != info["dept"]:
            # 8.   name 을 problems 에 추가한다
            problems.append(name)
    return problems


def run_checklist(state, now):
    users = state["users"]
    exceptions = state["exceptions"]
    role_dept = state["role_dept"]
    results = []
    results.append({"name": "퇴사자 계정 점검", "problems": check_employed(users)})
    results.append({"name": "만료 예외 점검", "problems": check_expired(exceptions, now)})
    results.append({"name": "부서와 역할 점검", "problems": check_dept(users, role_dept)})
    return results