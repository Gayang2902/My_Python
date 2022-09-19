# while = 또다른 반복문(어떠한 '조건'을 만족할떄 까지 반복)

# # 스타벅스에서 다섯번 손님을 불렀는데 손님이 나타나지 않을 경우 커피를 버리는 정책을 만들었다고 치자.
# customer = "토르"
# call = 5
# while call >= 1:
#     print("{0}님, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, call))
#     call -= 1
#     if call == 0:
#         print("커피는 폐기처분되었습니다.")

# 다른 커피점에서 손님이 나올 때까지 계속 부른다고 가정하자. (무한루프의 상황)
# customer = "아이언맨"
# call = 1
# while True:
#     print("{0}님, 커피가 준비 되었습니다. 호출횟수 {1}회".format(customer, call))
#     call += 1
# 위의 코드는 call변수에 계속해서 +1 되므로 '무한루프'에 빠진다. 
# 무한루프정지는 ctrl+c를 눌러 강제종료로 해결하자.

# 커피가 준비된 손님을 부르고 누군가 왔을떄 그 손님이 맞는지 확인하고 아닌경우 올떄까지 다시 부르는 경우
customer = "토르"
person = "Unknown"

while person != customer : # person = customer 일때 까지 반복된다.
    print("{0}님, 커피가 준비 되었습니다!".format(customer))
    person = input("이름이 어떻게 되세요? ") 









