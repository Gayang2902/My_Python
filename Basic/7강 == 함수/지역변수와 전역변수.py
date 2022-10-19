# 지역변수 = 함수내에서만 사용가능, # 전역변수는 프로그램 내 어디서나 사용가능
gun = 10 # 전역변수

def checkpoint(soldiers): # 경계근무 나가는 군인
    global gun # 전역 공간에 있는 함수를 사용할때는 global을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

# 위에 방법은 권장되지 않는다.
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun # 반환을 해줌으로써 전역공간에 던져주는것 



print("전체 총 : {}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2) # 이런식으로 하는게 권장됨


print("남은 총 : {}".format(gun))