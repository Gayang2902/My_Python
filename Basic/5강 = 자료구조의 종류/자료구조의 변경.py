# 커피숍으로 예를 들어 진행
menu = {"커피", "우유", "쥬스"} # == set
# type은 클래스의 종류를 알려줌

print(menu, type(menu)) # == class 'set'
# set는 {}

menu = list(menu) 
print(type(menu)) # == class 'list'
# list는 []

menu = tuple(menu)
print(type(menu)) # == class 'tuple'
# tuple은 ()

# 자료구조를 자료의 형태로 감싸주면 해당 자료구조가 된다.

menu = set(menu)


