# 당첨자 발표문 출력하기

# 출력예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 -- 

# 댓글 작성자는 20명 아이디는 숫자로 1~20
# 무작위 추첨, 중복 불가
# random모듈, shuffle, sample 들을 활용

from random import * # 줄바꿈은 \n

id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #목록의 기본값은 리스트


chicken = sample(id_list, 1) #목록에서 하나 꺼냄
print(chicken)


set_list = set(id_list) #세트인 목록
list_list = list(id_list) #리스트인 목록
# 목록에서 치킨당첨자를 뺴야된다.


shuffle(list_list)
list_list[:3]





# print("커피 당첨자 : " + id_list)
# print("-- 축하합니다 --")





