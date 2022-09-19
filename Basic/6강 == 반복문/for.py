# for = 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# 위와 같은 상황에서 for를 사용

# for waiting_num in [1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_num))
# # 위와 아래는 똑같은 결과를 내놓는다.
# for waiting_numa in range(1, 5): # range(1, 5)는 1~4까지의 범위를 의미
#     print("대기번호 : {0}".format(waiting_numa))

# 스타벅스 손님의 예제
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{}님, 커피가 준비되었습니다.".format(customer))

# 이와같이 for는 여러번 반복할때 상황에서 쓰면 좋다.

