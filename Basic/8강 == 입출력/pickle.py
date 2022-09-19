# pickle = 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해주는 것

import pickle
# profile_file = open("profile.pickle", "wb") # b는 바이너리를 의미,피클은 무조건 바이너리 타입을 정의해줘야함,피클은 인코딩설정필요x
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장해주는 것
# profile_file.close()

# 파일에서 데이터 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 프로필에 불러오기
print(profile)
profile_file.close()

