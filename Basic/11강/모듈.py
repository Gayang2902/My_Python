# 모듈 == 필요한 것들이 부품처럼 만들어진 파일? // 확장자는 .py
# 타이어의 교체? / 범퍼의 교체? ex)자동차

# 현금만 받는 극장의 예 / 잔돈을 주지 않는 곳 (현재상황에서는 theater_module을 만들어서 사용중)

import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 떄

import theater_module as mv # 해당 모듈의 별명을 정할 수 있다(호출명 변경)
# theater_module은 이제 mv로 호출이 가능하다.
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
# from random import * 과 비슷한 모듈 불러오기 방식
# 바로바로 모듈내의 모든 것을 사용한다는 의미
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning 
# 모듈에서 불러오고 싶은 함수만 불러올 수 있다.
price(5)
price_morning(6)

from theater_module import price_soldier as price
# 모듈에서 불러오고 싶은 함수만 불러서 별명까지 정해주기 
price(5) # == price_soldier




