# 사전 (dictionary) 자료형

# 열쇠 -> 방 과 같은 구성을 가짐  -- key:value // 열쇠는 value값을 불러내는 역할

cabinet = {3:"유재석", 100:"김태호"} 
 
print(cabinet[3]) #[]안에는 key값을 넣는다.
print(cabinet[100])

print(cabinet.get(3)) # []을 통해 value값을 가져오는 것과 동일한 결과를 출력함
 
# 주의할점. []을 통해 할당되지 않은 값을 가져올 경우에는 에러와 함께 프로그램이
# 종료되지만, get을 통해 할당되지 않은 값을 가져올 경우에는 None을 출력하고 프로그램이 계속 진행된다.

print(cabinet.get(5, "임의의 값")) #키가 할당되어 있지 않았어도 할당시켜 출력이 가능하다.
 
#사전자료형 안에 키가 있는지 확인하는 방법
print(3 in cabinet) # key in dict 을 사용 -- True
print(5 in cabinet) # False

# key의 지정은 문자형에도 적용이 가능하다.

# 새로운 키 지정 (이미 지정된 키에 새롭게 지정할경우 값이 업데이트된다.)
cabinet[7] = "조세호"
print(cabinet[7])
print(cabinet.get(7))

# 키 삭제
del cabinet[7]

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key와 value를 쌍으로 출력 (, )
print(cabinet.items())

# 모든 값 제거
cabinet.clear()
print(cabinet)








