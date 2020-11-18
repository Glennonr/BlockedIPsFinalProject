import time
from redis import Redis

r = Redis()

with open('blockedIPs.txt', 'r') as f:
    r.delete('iplist')
    for line in f:
        attack_date, attack_time, attack_ip, attack_protocol = line.split()
        print(attack_ip)
        if r.llen("iplist") > 98:
            r.ltrim('iplist', 0, 98)
        r.lpush("iplist", attack_ip)
        time.sleep(0.5)
