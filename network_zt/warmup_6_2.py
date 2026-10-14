import ipaddress

routes = [("192.168.10.0/24", "직접 연결 VLAN 10"),
          ("192.168.20.0/24", "직접 연결 VLAN 20"),
          ("192.168.30.0/24", "직접 연결 VLAN 30")]

dest = ipaddress.ip_address("192.168.30.5")
found = False

for net, hop in routes:
    if dest in ipaddress.ip_network(net):
        print("맞는 줄:", net, "→", hop)
        found = True

if found == False:
    print("회사 망 줄에 없음 → 기본 경로 0.0.0.0/0 (인터넷 쪽 라우터)")