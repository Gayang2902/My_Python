# 상속 : class의 있는 메소드와 멤버 변수를 '상속'/전달? 해주는 것

# 일반 유닛
class Unit: # 이름과 체력만 있는 기본적 class를 생성한다고 가정
    def __init__(self, name, hp): 
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 부모 class를 자식 class뒤에 괄호를 사용하여 넣어줌.
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


# 메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 25의 공격을 두번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)



