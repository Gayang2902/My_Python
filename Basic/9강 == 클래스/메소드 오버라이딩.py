# 자식 class에서 부모 class에서 정의한 메소드를 쓰고 싶을 때 오버라이딩을 사용한다.

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
        Unit.__init__(self, name, hp, speed) # 이런식으로 다른 class에서 이름과 체력을 상속받음
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
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move함수의 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # 부모class의 함수를 가져다 쓰는 것

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableattackUnit("배틀크루러", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# 이러한 방법의 단점은 매번 이 유닛이 지상유닛인지 공중유닛인지 확인해야 한다는 것이다!
# 이럴 때 메소드 오버라이딩을 쓰는 것 ==> 똑같이 move함수만으로 지상은 지상이동, 공중유닛은 날아가게 설정 할 수 있다.

vulture.move("11시")
battlecruiser.move("9시") # 이미 함수 내에서 self.name으로 이름을 가지고 있으므로 방향정보만 넣어도 된다.








