def approve_request(request, approver):
    """검토 중인 요청서만 승인한다.
    (성공 여부, 이유)를 리턴한다."""
    # ← 아래를 직접 씁니다
    # 1. status 가 "reviewing" 이 아니면
    #    False, "검토 중이 아님" 을 리턴한다
    if request["status"] != "reviewing":
        return False, "검토 중이 아님"
    # 2. request["user"] 가 approver 와 같으면
    #    False, "본인 요청은 처리할 수 없음"
    #    을 리턴한다
    if request["user"] == approver:
        return False, "본인 요청은 처리할 수 없음"
    # 3. request["status"] 를 "approved" 로 바꾼다
    request["status"] = "approved"
    # 4. request["approver"] 를 approver 로 정한다
    request["approver"] = approver
    # 5. True, "승인" 을 리턴한다
    return True, "승인"

def reject_request(request, approver):
    """검토 중인 요청서만 반려한다.
    (성공 여부, 이유)를 리턴한다."""
    # 검토 중이 아니면(이미 처리됐으면)
    if request["status"] != "reviewing":
        return False, "검토 중이 아님"
    # 요청한 사람이 스스로 처리하려고 하면
    if request["user"] == approver:
        return False, "본인 요청은 처리할 수 없음"
    # ← 아래를 직접 씁니다
    # 1. request["status"] 를 "rejected" 로 바꾼다
    request["status"] = "rejected"
    # 2. request["approver"] 를 approver 로 정한다
    request["approver"] = approver
    # 3. True, "반려" 를 리턴한다
    return True, "반려"