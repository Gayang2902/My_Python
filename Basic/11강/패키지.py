# 패키지 = 모듈들의 집합 = 하나의 디렉토리에 여러 모듈들을 갖다 넣은 것 (현재상황은 travel파일이 패키지임)
import travel.thailand # (import구문에서의 패키지사용법)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam # (from ~ import ~ 구문에서의 패키지사용법)
trip_to = vietnam.VietnamPackage()
trip_to.detail()