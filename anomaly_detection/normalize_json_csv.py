import csv
import json
from datetime import datetime

SERVER_TIME_FORMAT = "%Y-%m-%dT%H:%M"
COMMON_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
ALLOWED_MAP = {True: "성공", False: "실패"}
RESULT_MAP = {"success": "성공", "failure": "실패"}


def convert_server_time(time_text):
    """판정 서버 시각을 공통 모양으로 바꾼다.
    예: 2026-11-02T09:40 → 2026-11-02 09:40:00
    """
    # ← 아래를 직접 씁니다
    # 1. datetime.strptime(time_text, SERVER_TIME_FORMAT) 의 결과를 parsed 에 담는다
    parsed = datetime.strptime(time_text, SERVER_TIME_FORMAT)
    # 2. parsed.strftime(COMMON_TIME_FORMAT) 의 결과를 time_out 에 담는다
    time_out = parsed.strftime(COMMON_TIME_FORMAT)
    return time_out


def normalize_server(line):
    """판정 서버 로그 한 줄을 공통 이벤트로 바꾼다."""
    item = json.loads(line)
    time_out = convert_server_time(item["time"])
    allowed = item["allowed"]
    # ← 아래를 직접 씁니다
    # 3. ALLOWED_MAP 에서 allowed 에 해당하는 값을 꺼내 result 에 담는다 (ALLOWED_MAP[allowed])
    result = ALLOWED_MAP[allowed]
    raw_text = line.strip()
    event = {
        "time": time_out,
        "source": "server",
        "user": item["user"],
        "ip": None,
        "action": item["permission"],
        "result": result,
        "raw": raw_text,
    }
    return event


def normalize_saas(row):
    """SaaS 로그 한 행을 공통 이벤트로 바꾼다."""
    # ← 아래를 직접 씁니다
    # 4. row["account"] 를 "@" 기준으로 나눠 account_parts 에 담는다 (예: seoyeon@a-corp.example)
    account_parts = row["account"].split("@")
    # 5. account_parts 의 첫 값을 user 에 담는다
    user = account_parts[0]
    outcome = row["outcome"]
    # 6. RESULT_MAP 에서 outcome 에 해당하는 값을 꺼내 result 에 담는다
    result = RESULT_MAP[outcome]
    event = {
        "time": row["time"],
        "source": "saas",
        "user": user,
        "ip": row["ip_address"],
        "action": row["event"],
        "result": result,
        "raw": row,
    }
    return event


def load_server(path):
    events = []
    with open(path, encoding="utf-8") as server_file:
        for line in server_file:
            event = normalize_server(line)
            events.append(event)
    return events


def load_saas(path):
    events = []
    with open(path, encoding="utf-8", newline="") as saas_file:
        reader = csv.DictReader(saas_file)
        for row in reader:
            event = normalize_saas(row)
            events.append(event)
    return events