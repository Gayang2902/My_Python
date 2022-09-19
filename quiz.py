from random import *

users = list(range(1, 21))

shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하합니다 -- ")


#asdasdasdadasda