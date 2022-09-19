# print("Python", "Java") # 출력문 : Python Java
# print("Python" + "Java") # 출력문 : PythonJava
# # sep = "" ""사이에 구문을 넣어 띄어쓰기 사이에 무엇을 넣을지 지정해줄 수 있다!
# print("Python", "Java", "Javascript", sep = " vs ") # 출력문 : Python vs Java vs Javascript
# print("Python", "Java", "Javascript", sep = ",") # 출력문 : Python,Java,Javascript
# sep는 seperate의 약자


# # 줄바꿈을 하지 않게 해주는 end를 응용하면..
# print("Python", "Java", sep = ",", end = "?")
# print("무엇이 더 재밌을까요?") # 출력문 : Python,Java?무엇이 더 재밌을까요?

# import sys
# print("Python", "Java", file = sys.stdout) # 표준 출력으로 문장이 찍힘
# print("Python", "Java", file = sys.stderr) # 표준 에러로 문장이 찍힘

# 시험성적 표기의 예
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items(): # key와 value를 쌍으로 tuple로 보내준다.
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")
#     # ljust(숫자) : 숫자만큼의 공간을 확보하고 왼쪽정렬, rjust(숫자) : 숫자만큼의 공간을 확보하고 오른쪽정렬


# # 은행 대기순번표의 예 : 001, 002, 003, 004....이런식으로 표기되기를 원함
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # zerofill : 0으로 채우다, 숫자만큼의 공간을 확보하고 나머지를 0으로 채워줌.

# == 여기까지 표준 출력 ==

answer = input("아무 값이나 입력하세요. : ") # input으로 저장된 변수는 무조건 str(문자열)의 타입을 가지게 된다.
print("입력하신 값은 " + answer + "입니다.")















