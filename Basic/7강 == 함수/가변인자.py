# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end를 사용하면 아래의 출력문을 붙여서 출력할 수 있다.
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#") # 여기서 더 언어가 늘어난다면?
# prifile("김태호", 25, "Kotlin", "Swift", "", "", "") # 매번 이렇게 하면 귀찮으니까?

# 가변인자를 사용

def profile(name, age, *language): # *매개변수는 가변인자가 된다
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")

