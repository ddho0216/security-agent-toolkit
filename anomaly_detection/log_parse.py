def split_request(line):
    """로그 한 줄을 큰따옴표 기준으로 앞 · 요청 · 뒤 세 조각으로 나눈다."""
    # ← 아래를 직접 씁니다
    # 1. line 을 큰따옴표(")로 두 번만 나눠 prefix, request_text, suffix 세 이름에 담는다 (line.split('"', 2))
    prefix, request_text, suffix = line.split('"', 2)
    return prefix, request_text, suffix


def read_request(request_text):
    """요청 조각에서 방법(method)과 경로(path)를 꺼낸다."""
    # ← 아래를 직접 씁니다
    # 2. request_text 를 공백 기준으로 나눠 method, path, protocol 세 이름에 담는다 (request_text.split())
    method,path,protocol = request_text.split()
    return method, path


def read_status(suffix):
    """요청 뒤 조각에서 상태 코드를 꺼내 정수로 리턴한다."""
    # ← 아래를 직접 씁니다
    # 3. suffix 를 공백 기준으로 나눠 parts 에 담는다 (suffix.split())
    parts = suffix.split()
    # 4. parts 의 첫 값을 status_text 에 담는다 (parts[0])
    status_text = parts[0]
    # 5. status_text 를 int 로 바꿔 status 에 담는다
    status = int(status_text)
    return status


def read_client(prefix):
    """요청 앞 조각에서 접속자 주소를 꺼낸다."""
    # ← 아래를 직접 씁니다
    # 6. prefix 를 공백 기준으로 나눠 parts 에 담는다 (prefix.split())
    parts = prefix.split()
    # 7. parts 의 첫 값을 client_ip 에 담는다 (parts[0])
    client_ip = parts[0] 
    return client_ip


def parse_line(line):
    """로그 한 줄을 ip · method · path · status 딕셔너리로  바꾼다. 깨진 줄이면 None."""
    # ← 아래를 직접 씁니다
    # 8. 큰따옴표가 두 개보다 적으면 (if line.count('"') < 2:)
    if line.count('"') < 2:
        return None
    prefix, request_text, suffix = split_request(line)
    method, path = read_request(request_text)
    status = read_status(suffix)
    client_ip = read_client(prefix)
    entry = {
        "ip": client_ip,
        "method": method,
        "path": path,
        "status": status,
    }
    return entry