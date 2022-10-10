# 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 승객별 운행 소요 시간은 5~50분사이의 난수, 소요시간 5~15분 사이의 승객만 매칭해야함

import random

guests = []
count = 0
for i in range(0, 50):
    guests.append(random.randint(5, 50))

for i in range(0, 50):
    if 5 <= guests[i] <= 15:
        print("[O] {} guest (time : {}m".format(i+1, guests[i]))
        count += 1
    else:
        print("[] {} guest (time : {}m".format(i+1, guests[i]))
        
print(count)