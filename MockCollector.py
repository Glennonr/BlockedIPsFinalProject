import time
from redis import Redis

r = Redis()

with open('blockedIPs.txt', 'r') as f:
    r.delete('iphash')
    for line in f:
        attack_date, attack_time, attack_ip, attack_protocol = line.split()
        r.hset('iphash', attack_ip, attack_time)
        ip_dict = r.hgetall('iphash')
        for ip in ip_dict:
            iterated_time = int(ip_dict[ip].decode()[6:])
            time_to_add = int(attack_time[6:])
            print(iterated_time, time_to_add)
            if iterated_time - time_to_add < 0:
                r.hdel('iphash', ip)
                print('deleted', ip)

        time.sleep(0.5)

"""
Make a hash with key ip and value is timestamp
save HGETALL of hash to get a dict of the keys and values Evens would be keys (IP) Odd values (times)
iterate over odds in list and if the time is a minute older than the recent attack_time HDEL the list item before it
"""
