   # day05 경보 판단

   ## 이상한 줄
   - 줄 번호(여러 개면 모두):2번 3번
   
   - 이유: DB는 INSIDE에 있어서 인터넷에 바로 닿으면 안 되는데, 
   인터넷 192.0.2.7 IP가 WEB을 거치지 않고 바로 DB에 닿았고 permit됐다 

   ## 고친 구성도
```
   (여기에 ASCII 구성도)
```
INTERNET ──── FW ──┬── DMZ    WEB *443 open
                   └── INSIDE DB *3306 from WEB only 