# 한줄로 끝내는 for문..
# 출석번호가 1 2 3 4...인데 앞에 100을 붙이기로 함 -> 101 102 103 104...
# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "Groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)
