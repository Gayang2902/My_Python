# 상속해주는 class = 부모 class / 상속받는 class = 자식 class

# 일반 유닛
class Unit: # 이름과 체력만 있는 기본적 class를 생성한다고 가정
    def __init__(self, name, hp): 
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp) # 이런식으로 다른 class에서 이름과 체력을 상속받음
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
class FlyableattackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일을 발사.
valkyrie = FlyableattackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") # Flyable class에 있는 fly함수를 호출, Flyable class에서는 
# 이름이 정의되지 않으므로 윗줄의 valkyrie에 할당된 이름을 valkyrie.name으로 불러왔다.







