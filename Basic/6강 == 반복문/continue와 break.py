# 반복문내에서 contine와 break가 사용된다.

# 선생님이 교실내에서 출석번호를 호명하며 책을 읽으라고 시키는 상황
absent = [2, 5] # 결석자
no_book = [7] # 책이 없는사람
for student in range(1, 11): # 출석번호는 1부터 10까지...
    if student in absent:
        continue # 여기까지 진행되고 다음 반복으로 넘어감
    elif student in no_book:
        print("오늘 수업은 여기까지 진행하겠습니다. {0}번은 교무실로 오십시오.".format(student))
        break # 여기까지 진행되고 반복문을 탈출함
    print("{0}번, 책을 읽어주세요.".format(student)) # 결석자인 2와 5번을 제외하고 문장이 실행된다.


