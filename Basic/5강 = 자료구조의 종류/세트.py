# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3} # 사전(dict)처럼 {}을 쓰지만 여기서는 그냥 값만 {}안에 집어넣음
print(my_set) # 중복되는 값은 무시하고 출력됨

# 개발자의 집합을 예를 들어 진행
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # set로 리스트를 감싸줌 윗줄과 비슷한 집합구조

# 교집합 (java와 python을 모두 할 수 있는 개발자)을 출력 하는 방법들
print(java & python)
print(java.intersection(python)) # 교집합 = intersection
 
# 합집합 (java혹은, python 둘 중 하나라도 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # 합집합 = union

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자 -- java집합-교집합)
print(java - python)
print(java.difference(python)) # 차집합 = difference

# 세트에 객체추가
python.add("김태호")
print(python)

# 세트에서 객체삭제
python.remove("김태호")
print(python)





