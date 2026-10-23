from rbac import ROLES                                           # 어제 rbac.py 가 읽어 둔 역할 딕셔너리를 불러온다


def assign_role(users, name, role):                              # 사용자 딕셔너리 · 이름 · 역할을 받는 함수
    """사용자에게 역할을 부여한다(입사 · 부서 이동). (성공 여부, 이유)를 리턴한다."""
    if role not in ROLES:                                        # 역할 파일에 없는 역할이면
        return False, "없는 역할"                                 # 부여하지 않고 거부한다
    users[name] = {"role": role, "employed": True}               # 사용자 항목을 새로 만들거나 덮어쓴다
    return True, "부여"                                           # 부여했다고 알린다


def revoke_access(users, name):                                  # 사용자 딕셔너리 · 이름을 받는 함수
    """퇴사한 사용자의 접근을 회수한다. 역할은 남기고 `employed` 값만 바꾼다. (성공 여부, 이유)를 리턴한다."""
    if name not in users:                                        # 사용자 파일에 없는 이름이면
        return False, "없는 사용자"                               # 회수할 것이 없다고 알린다
    users[name]["employed"] = False                              # employed 값을 False 로 바꾼다
    return True, "회수"                                           # 회수했다고 알린다