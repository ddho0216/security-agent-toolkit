from datetime import datetime
from log_parse import split_request, read_request, read_status, read_client

NGINX_TIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"     # nginx 시각의 모양
COMMON_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"       # 공통 시각의 모양


def read_time_text(prefix):
    """요청 앞 조각에서 대괄호 안의 시각 문자열을 꺼낸다."""
    parts = prefix.split()
    bracket_text = parts[3] + " " + parts[4]
    time_text = bracket_text.strip("[]")
    return time_text


def convert_time(time_text):
    """nginx 시각을 공통 모양의 문자열로 바꾼다.
    예: 02/Nov/2026:09:12:03 +0900 → 2026-11-02 09:12:03
    """
    # ← 아래를 직접 씁니다
    # 1. datetime.strptime(time_text, NGINX_TIME_FORMAT) 의 결과를 parsed 에 담는다
    parsed = datetime.strptime(time_text, NGINX_TIME_FORMAT)
    
    # 2. parsed.replace(tzinfo=None) 의 결과를 local_time 에 담는다 (+0900 정보를 떼고 한국 시각만 남긴다)
    local_time = parsed.replace(tzinfo=None)
    # 3. local_time.strftime(COMMON_TIME_FORMAT) 의 결과를 time_out 에 담는다
    time_out = local_time.strftime(COMMON_TIME_FORMAT)
    return time_out


def convert_result(status):
    """상태 코드가 400 이상이면 「실패」, 아니면 「성공」을 리턴한다."""
    # ← 아래를 직접 씁니다
    # 4. status 가 400 이상이면 (if)
    if status >= 400:
    # 5.   "실패" 를 리턴한다
        return "실패"
    # 6. 그 밖에는 "성공" 을 리턴한다
    else:
        return "성공"
    


def normalize_web(line):
    """웹 서버 로그 한 줄을 공통 이벤트 딕셔너리로 바꾸고, 깨진 줄이면 None."""
    if line.count('"') < 2:
        return None
    prefix, request_text, suffix = split_request(line)
    method, path = read_request(request_text)
    status = read_status(suffix)
    client_ip = read_client(prefix)
    time_text = read_time_text(prefix)
    time_out = convert_time(time_text)
    result = convert_result(status)
    action = method + " " + path
    raw_text = line.strip()
    event = {
        "time": time_out,
        "source": "web",
        "user": None,
        "ip": client_ip,
        "action": action,
        "result": result,
        "raw": raw_text,
    }
    return event