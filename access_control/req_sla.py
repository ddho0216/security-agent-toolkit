from datetime import datetime
# 10/22 안전한 읽기 함수
from config_loader import load_json
# 시각 글자의 형식("%Y-%m-%d %H:%M")
from exception_policy import TIME_FORMAT

# 처리 기한(시간). 파일이 없거나 깨지면 기본값 4
SLA_HOURS = load_json("config/sla.json",
                      {"hours": 4})["hours"]


def check_sla_breach(requests, now):
    """검토 중인 요청서 가운데 접수한 지
    SLA_HOURS 시간을 초과한 것의 목록을 리턴한다."""
    # 1. 기한을 초과한 요청서를 담을 빈 목록
    breached = []
    # 2. requests 에서 request 를 하나씩 꺼낸다
    for request in requests:
        # 3. 검토 중인 것만 본다
        if request["status"] == "reviewing":
            # 4. 접수 시각 글자를 시각으로 바꾼다
            requested = datetime.strptime(request["requested_at"], TIME_FORMAT)
            # 5. 걸린 시간을 시간 단위 숫자로 구한다
            hours = (now - requested).total_seconds() / 3600
            # 6. SLA 시간보다 크면(같으면 아직 아니다)
            if hours > SLA_HOURS:
                # 7. 요청서를 복사한다
                overdue = request.copy()
                # 8. 지난 시간을 소수 첫째 자리로 반올림해 적는다
                overdue["wait_hours"] = round(hours, 1)
                # 9. 초과 목록에 더한다
                breached.append(overdue)
    # 10. 반복이 끝나면 리턴한다
    return breached