import json
from normalize_web import normalize_web
from normalize_json_csv import load_server, load_saas

EVENTS_PATH = "normalized_events.json"


def load_web(path):
    events = []
    with open(path, encoding="utf-8") as web_file:
        for line in web_file:
            event = normalize_web(line)
            if event is not None:
                events.append(event)
    return events


def get_time(event):
    return event["time"]


def merge_events(web, server, saas):
    """이벤트 리스트 세 개를 하나로 이어 붙이고 시간순으로 정렬한다."""
    # ← 아래를 직접 씁니다
    # 1. web, server, saas 를 + 로 이어 붙여 events 에 담는다
    events = web + server + saas
    # 2. events.sort(key=get_time) 로 time 이 이른 것부터(오름차순) 정렬한다 
    # (sort 는 events 자체를 바꾸고 아무것도 리턴하지 않는다)
    events.sort(key=get_time)
    return events


def count_by_source(events):
    """소스별 이벤트 수를 {소스: 개수} 딕셔너리로 센다."""
    counts = {}
    for event in events:
        # ← 아래를 직접 씁니다
        # 3. event 의 "source" 값을 source 에 담는다
        source = event["source"]
        # 4. counts 에서 source 의 현재 횟수(없으면 0)에 1 을 더해 counts[source] 에 담는다 (counts.get)
        counts[source] = counts.get(source, 0) +1
    return counts


def count_missing(events, key):
    missing = 0
    for event in events:
        if event[key] is None:
            missing = missing + 1
    return missing


def save_events(events, path):
    """이벤트 리스트를 JSON 파일로 저장한다."""
    with open(path, "w", encoding="utf-8") as events_file:
        # ← 아래를 직접 씁니다
        # 5. json.dump(events, events_file, ensure_ascii=False, indent=2) 로 events 를 
        # events_file 에 저장한다
        json.dump(events, events_file, ensure_ascii=False, indent=2)