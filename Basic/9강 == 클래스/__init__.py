# __init__ == 파이썬에서 사용되는 '생성자'

class Unit:
    def __init__(self, name, hp, damage): # __init__에서 정의된 객체의 갯수만큼을 무조건 클래스사용시 사용해야함.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # self를 제외한 3개의 객체를 모두 사용
marine2 = Unit("마린", 40, 5)

