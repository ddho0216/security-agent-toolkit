# 2교시 요청서 함수와 목록
from req_create import REQUESTS, create_request
# 방금 만든 승인 · 반려 함수
from req_review import approve_request, reject_request

# 접수에 성공하는 요청 네 건
# (요청자, 자원, 행위, 만료 시각, 이유, 접수 시각)
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
# 요청을 하나씩 꺼내 접수한다
for user, resource, action, until, reason, received_at in INBOX:
    create_request(user, resource, action,
                    until, reason, received_at)

# security_manager 가 내리는 처리 여섯 건
# (요청 번호, 처리)
DECISIONS = [
    (1, "승인"),
    (2, "반려"),
    (3, "승인"),
    (4, "승인"),
    # 이미 승인한 1번을 다시 승인해 본다
    (1, "승인"),
    # 이미 반려한 2번을 승인해 본다
    (2, "승인"),
]

print("--- 단계 1: 처리 - 본인 요청 시험 한 건, "
      "승인 · 반려 여섯 건을 처리한다")
# seoyeon 이 자기 요청 1번을 스스로 승인해 본다
ok, result = approve_request(REQUESTS[0], "seoyeon")
print(1, "본인 승인 ->", ok, result)
for number, decision in DECISIONS:
    # 번호는 1부터, 목록 자리는 0부터
    request = REQUESTS[number - 1]
    if decision == "승인":
        ok, result = approve_request(
            request, "security_manager")
    else:
        ok, result = reject_request(
            request, "security_manager")
    print(number, decision, "->", ok, result)

print("--- 단계 2: 점검 - 요청서 목록")
for request in REQUESTS:
    # 번호 · 요청자 · 상태 · 처리한 사람
    print(request["id"], request["user"],
          request["status"], request.get("approver"))