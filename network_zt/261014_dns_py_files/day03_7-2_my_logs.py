LOG = [("dinner.dailyrice.com", "NOERROR", "정상"), ("shop-green-market.xyz", "NOERROR", "정상"),
       ("old-team-board.top", "NXDOMAIN", "정상"), ("mq8zt3vx.net", "NXDOMAIN", "의심"),
       ("kv2x9qzr7w4.com", "NXDOMAIN", "의심"), ("my-safe-bank-login.net", "NOERROR", "의심")]
for name, rcode, truth in LOG:
    parts = name.split(".")
    score = 0
    if len(parts[-2]) >= 10:
        score = score + 1
    if parts[-1] in ["top", "xyz", "tk"]:
        score = score + 1
    if rcode == "NXDOMAIN":
        score = score + 2
    print(name, score, score >= 3, "실제:", truth)