# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요")
# print("{}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir()) # ()안에 아무것도 없으면 전체 구문내의 가지고 있는 변수 / 함수를 표시
import random # 외장 함수
print(dir())    

print(dir(random))

lst = [1,2,3]
print(dir(lst))

name = "Kim"
print(dir(name))

# 참고할만한 사이트 == 구글 : list of python builtins

