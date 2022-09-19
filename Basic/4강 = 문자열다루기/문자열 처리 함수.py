#문자열 처리 함수

python = "Python is Amazing"
print(python) 
print(python.lower()) #모두 소문자로
print(python.upper()) #모두 대문자로
print(python[0].islower()) #해당 위치가 소문자인지 확인 False
print(len(python)) #변수길이확인
print(python.replace("Python", "Java")) #변수 내 문자변경

index = python.index("n") #해당글자가 몇번째 위치에 있는지 확인
print(index)
index = python.index("n", index + 1) #해당글자 이후의 위치에 있는 글자 위치 확인
print(index)

print(python.find("n")) #index와 비슷하지만 좀 다르다.

#_index와 find의 차이
print(python.find("Java")) #해당 문자열에 글자가 없지만 -1을 반환하고 코드를 계속 진행시킨다.
#print(python.index("Java")) #해당 문자열에 글자가 없다면, 오류를 내면서 코드를 중단시킨다. (둘의 차이 유념)

print(python.count("n")) #해당 글자의 갯수 확인