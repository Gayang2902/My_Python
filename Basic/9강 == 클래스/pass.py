

# 일반 유닛 + 지상 유닛이므로 걸어다니는 속도 추가
class Unit: 
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛 + Unit을 상속받았으므로 똑같이 speed 정보 추가
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed) 
        self.damage = damage
    
    # 공격 상황
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    # 공격 받은 상황
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수동. 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".\
            format(name, location, self.flying_speed))
    
# 공중 공격 유닛 클래스
class FlyableattackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) 
        Flyable.__init__(self, flying_speed)

    def move(self, location): 
        print("[공중 유닛 이동]")
        self.fly(self.name, location) 

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # pass = 아무것도 안하고 일단은 넘어가는 것

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛 수용
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

    











