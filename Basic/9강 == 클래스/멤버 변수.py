# 멤버 변수 == class내에서 정의된 변수

class Unit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5) 
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 멤버 변수를 class외부에서 사용하기
# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # .을 통해 멤버변수에 접근가능

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit("빼앗긴 레이스", 80, 5)
wraith2.clocking = True # 레이스2에는 클로킹을 줬지만 레이스1에는 클로킹이 없다!
# class외부에서 원하는 변수에 대해 확장을 할 수 있다.
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

