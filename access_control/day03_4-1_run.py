from datetime import datetime
from req_create import REQUESTS, create_request
from req_review import approve_request, reject_request
from req_grant import grant_request
# 10/22 최종 판정 함수
from policy import evaluate_access

# 오늘 실습의 지금 시각(고정)
NOW = datetime.strptime("2026-10-23 10:00",
                        "%Y-%m-%d %H:%M")

# 접수에 성공하는 요청 네 건
INBOX = [
    ("seoyeon", "SETTLE", "QUERY",
     "2026-10-27 18:00", "정산 대조 지원",
     "2026-10-23 08:30"),
    ("gaeun", "SALES", "QUERY",
     "2026-10-28 18:00", "감사 자료 대응",
     "2026-10-23 08:40"),
    ("dami", "SALES", "QUERY",
     "2026-10-27 18:00", "인수인계 자료 확인",
     "2026-10-23 08:50"),
    ("junho", "SETTLE", "QUERY",
     "2026-10-27 18:00", "정산 확인",
     "2026-10-23 09:00"),
]
for user, resource, action, until, reason, received_at in INBOX:
    create_request(user, resource, action,
                   until, reason, received_at)
# 1 · 3 · 4번은 승인
for number in [1, 3, 4]:
    approve_request(REQUESTS[number - 1],
                    "security_manager")
# 2번은 반려
reject_request(REQUESTS[1], "security_manager")


# 요청서마다 최종 판정을 출력하는 함수
def show(title):
    print("---", title)
    for request in REQUESTS:
        ok, reason = evaluate_access(
            request["user"], request["resource"],
            request["action"], NOW)
        print(request["id"], request["user"],
              request["permission"], "->", ok, reason)


# 부여 전 판정
show("단계 1: 판정 - 부여 전")

print("--- 단계 2: 부여 - 요청서마다 부여를 시도한다")
for request in REQUESTS:
    ok, result = grant_request(request)
    print(request["id"], request["user"],
          request["status"], "->", ok, result)

for request in REQUESTS:
    # 부여된 요청서만 예외 번호를 출력한다
    if "exception_id" in request:
        print("부여된 예외 번호:",
              request["exception_id"])

# 부여 후 판정
show("단계 3: 점검 - 부여 후")