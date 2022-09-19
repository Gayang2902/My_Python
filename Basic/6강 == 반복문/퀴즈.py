# 50명의 승객과 매칭 기회
# 조건1 : 승객별 운행소요시간은 5분~50분의 난수
# 조건2 : 운행소요시간 5분~15분 사이의 승객만 받아야함

from random import *
call = 1
final_guest = 0
for guest in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(guest, time))
        final_guest += 1
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(guest, time))

print("총 탑승 승객 : {} 분".format(final_guest))
    
    
    





