# 퀴즈3 사이트별로 비밀번호를 만들어 주는 프로그램 제작 -- 사이트의 주소를 기반으로 비밀번호를 생성
# 규칙1. http:// 은 제외
# 규칙2. 처음 만나는 . 이후 부분은 제외 
# 규칙3. 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 "e" 개수 + "!" 로 비밀번호를 구성



url = "http://youtube.com"
password = url.replace("http://", "")
password = password[:password.find(".")]
password = password[:3]+str(len(password))+str(password.count("e"))+"!"
print(password)