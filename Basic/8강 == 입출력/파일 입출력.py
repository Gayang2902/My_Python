score_file = open("score.txt", "w", encoding = "utf8") # w는 쓰기용도(덮어쓰기)
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()
# 파일을 열었으면 파일을 다시 닫아줘야 한다.

score_file = open("score.txt", "a", encoding = "utf8") # a는 이어쓰기
score_file.write("과학 : 80") 
score_file.write("\n코딩 : 100") # write로 파일을 작성하게 되면 줄바꿈이 되지 않으므로 따로 줄바꿈처리를 해줘야 한다.
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read()) # 이 방식은 파일내부를 모두 읽는것
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#파일내부가 몇줄 인지 모를때 위와같이 하는 방법1 (반복문을 이용)
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

#파일내부가 몇줄 인지 모를떄 위와같이 하는 방법2
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line)
score_file.close()

