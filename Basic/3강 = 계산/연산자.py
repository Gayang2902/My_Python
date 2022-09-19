#연산자
print(1+1) #덧셈
print(3-1) #뺄셈
print(5*2) #곱셈
print(6/3) #나눗셈

print(2**3) #밑의 몇제곱
print(5%3) #나눈뒤의 나머지
print(10//3) #몫 구하기

print(10 > 3) #비교연산 True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #앞과 뒤의 값이 같은지를 확인 True
print(4 == 2) #False
print(3 + 4 == 7) #True

print(1 != 3) #앞과 뒤의 값이 다른지를 확인 True
print(not(1 != 3)) #boolean+연산자 False

print((3 > 0) and (3 < 5)) #앞과 뒤의 항이 모두 만족하는가? True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 > 5)) #앞과 뒤의 항 둘중 하나가 만족하는가? True
print((3 > 0) | (3 > 5)) #True

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False