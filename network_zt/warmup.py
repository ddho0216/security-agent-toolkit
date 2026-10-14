PORTS = {80: "HTTP", 443: "HTTPS", 53: "DNS"}
print(PORTS[443])
print(PORTS.get(3389, "모름"))