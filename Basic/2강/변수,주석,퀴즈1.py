#변수
#애완동물의 소개
animal = "고양이"
name = "까망이"
age = 5
hobby = "물어뜯기"
is_adult = age >= 4

print("우리집 " + animal + "의 이름은 " + name + "입니다.")
print(name + "의 나이는 " + str(age) + "살이고, " + hobby + "를 아주 좋아합니다.") #숫자변수는 str()로 삽입시켜준다.
print(name + "는 어른입니까? "  + str(is_adult))
#+대신 ,를 사용하여 변수를 삽입할수도 있는데, 이때는 정수형 변수와 boolean변수를 str로 감싸주지 않아도 된다.
#예시
print(name, "의 나이는 ", age, "살입니다.") 
# ,로 변수를 삽입하게 되면 항상 띄어쓰기가 된다.

#일괄 주석설정(해제)는 문장선택->command+/

#Quiz 1

station1 = "사당"
station2 = "신도림"
station3 = "인천공항"

print(station1+"행 열차가 들어오고 있습니다.")
print(station2+"행 열차가 들어오고 있습니다.")
print(station3+"행 열차가 들어오고 있습니다.")