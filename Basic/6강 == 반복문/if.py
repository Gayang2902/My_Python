# if = 분기

# if 조건:
# #실행명령문

# if는 만약 ~이면, elif는 그렇지 않고 ~이면, else는 그밖에
# weather = "비"
# weather = "미세먼지"
# weather = "맑음"
weather = input("오늘 날씨는 어떤가요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("챙길 것이 없습니다.")
# else는 if와 elif의 조건외에 모든상황에 대해 실행명령문을 실행한다.
 
temp = int(input("기온은 어때요? ")) # input은 항상 문자열로 값을 받기 때문에 이때는 int로 감싸준다.
# str은 정수 -> 문자 / int은 문자 -> 정수?
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp < 30: # 조건이 두가지 이상일경우 and 또는 or을 사용
    print("괜찮은 날씨입니다.")
elif 0 <= temp and temp < 10: # 범위이므로 and를 쓰거나 범위를 아예 적거나 편한대로..
    print("외투를 챙기세요")
else: # 기온이 0도 아래
    print("너무 추워요. 나가지 마세요.")







