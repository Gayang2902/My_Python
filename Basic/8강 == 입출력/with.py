# with를 쓰면 좀더 편하게 파일입출력이 가능하다.

# pickle의 경우(읽기)
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # 이렇게 하면 close가 필요없다.


# 일반적인 파일의 경우(쓰기)
with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있습니다.")


# 일반적인 파일의 경우(읽기)
with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())

# with는 매번 close를 해줄 필요가 없고 문장의 길이를 줄일수있는 장점이 있다.

