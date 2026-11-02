from log_parse import parse_line                    # 방금 만든 로그 한 줄 읽기 함수를 불러온다

LOG_PATH = "access_sample.log"                      # 읽을 샘플 로그 파일 이름
entries = []                                        # 읽은 요청을 모을 리스트
fail_count = 0                                      # 읽기 실패한 줄 수를 0 으로 시작한다
total = 0                                           # 전체 줄 수를 0 으로 시작한다
with open(LOG_PATH, encoding="utf-8") as log_file:  # 로그 파일을 연다
    for line in log_file:                           # 파일에서 한 줄씩 꺼낸다
        total = total + 1                           # 전체 줄 수를 1 늘린다
        entry = parse_line(line)                    # 한 줄을 읽어 딕셔너리로 바꾼다
        if entry is None:                           # 깨진 줄이라 읽지 못했으면
            fail_count = fail_count + 1             # 읽기 실패한 줄 수를 1 늘린다
        else:                                       # 읽었으면
            entries.append(entry)                   # 요청 리스트에 추가한다

success_count = len(entries)                        # 읽기 성공한 줄 수를 센다
print("--- 단계 1: 로그 파일 읽기 - 전체", total, "줄")
print("읽기 성공", success_count, "줄 · 읽기 실패", fail_count, "줄")
print("--- 단계 2: 로그 첫 3줄을 읽은 결과")
print(entries[0])
print(entries[1])
print(entries[2])
print("--- 단계 3: 값이 덧붙은 요청 (경로에 ? 포함)")
for entry in entries:
    if "?" in entry["path"]:
        print(entry["ip"], entry["path"])