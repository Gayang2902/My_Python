from random import *
users = range(1, 21) # range = 숫자의 범위 *부터*직전까지의 수
# range를 사용하면 type이 range로 처리되서 원하는 type의 함수를 쓸때는 type을 바꿔주어야 한다.
users = list(users) # 이런식으로..

shuffle(users) # 목록을 한번 섞어준다.

# 당첨자가 중복되면 안되므로 한번에 4명을 뽑아준다.
winners = sample(users, 4) # 4명 중 한명은 치킨, 세명은 커피

# 포맷팅을 사용
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하합니다 -- ")



