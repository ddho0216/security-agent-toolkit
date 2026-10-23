# 10/21 역할 판정 함수
from rbac import check_permission
# 10/22 예외 목록
from exception_policy import EXCEPTIONS


def grant_request(request):
    """승인된 요청서를 정책으로 한 번 더 확인하고
    통과하면 예외 권한을 부여한다.
    (성공 여부, 이유)를 리턴한다."""
    # 승인된 요청서가 아니면 막는다
    if request["status"] != "approved":
        return False, "승인되지 않음"
    # 요청자를 지금 정책으로 판정한다
    ok, judge_reason = check_permission(
        request["user"], request["resource"],
        request["action"])
    # 이미 허용이거나 사람이 거부 대상이면 막는다
    if ok or judge_reason != "권한 없음":
        return False, f"부여하지 않음({judge_reason})"
    # 요청서 내용으로 예외 한 건을 만든다
    exception = {"id": len(EXCEPTIONS) + 1,
                 "user": request["user"],
                 "permission": request["permission"],
                 "expires": request["until"],
                 "reason": request["reason"]}
    # 예외 목록에 더한다
    EXCEPTIONS.append(exception)
    # 어느 예외인지 요청서에 적어 둔다
    request["exception_id"] = exception["id"]
    # 상태를 부여됨으로 바꾼다
    request["status"] = "granted"
    return True, "부여"