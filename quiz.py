# 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 승객별 운행 소요 시간은 5~50분사이의 난수, 소요시간 5~15분 사이의 승객만 매칭해야함

import random

guests = []
guests.insert(i, (int((random.random() * 10) + 1))) for i in range(0, 50)    