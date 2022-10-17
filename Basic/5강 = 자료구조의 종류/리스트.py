# 리스트 [] : 객체의 집합 만들기

# 예시)지하철 칸별로 10명, 20명, 30명 지정
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)


subway = ["유재석", "조세호", "박명수"]
print(subway) #subway는 단순히 상황설정의 변수로 설정

#조세호는 몇 번째 위치 있는가?
print(subway.index("조세호"))

#하하가 다음위체에 추가됨
subway.append("하하") #append는 맨뒤에 객체를 추가
print(subway)

#정형돈을 유재석 / 조세호 사이에 삽입
subway.insert(1, "정형돈") #insert는 리스트 중간에 위치를 지정해서 객체를 삽입
print(subway)

# 값 삭제

#리스트에 있는 객체를 하나씩 꺼냄 - pop() 을 아용함 / 기본적으로는 리스트의 맨 마지막 인덱스 삭제 ()안에 인덱스 번호 지정 가능
#print(subway.pop()) # 꺼내진 객체 출력
subway.pop()
print(subway) # 객체가 꺼내진 이후에 리스트 출력

# del 키워드
# del list_list[index] / []안에 슬라이싱을 사용해서 여러 개의 값을 삭제 가능

# remove 함수 / 값이 x와 같은 첫 번째 요소 제거
# 만약 리스트안에 같은 요소가 두 가지 이상 있다면 그 중 첫번째 값을 제거함
# list_list.remove(x) 

print(subway.pop())
# print(subway)

#같은 이름의 객체가 몇 개 있는지 확인
subway.append("유재석")

print(subway.count("유재석"))

#정렬

num_list = [5,2,4,3,1]
num_list.sort()  # sorting은 정렬하다의 뜻
print(num_list)

#순서 뒤집기

num_list.reverse()
print(num_list)

#내용 지우기

#num_list.clear()
print(num_list)

#다양한 자료형을 함께 리스트생성 가능(숫자형, 문자형, boolean형)

mix_list = ["조세호", 20, False]
print(mix_list)

#리스트확장(더하기)

num_list.extend(mix_list)
print(num_list)

