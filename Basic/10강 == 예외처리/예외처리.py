# 에러가 발생하였을 때 그에 대해 처리를 해주는 것

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) 
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1])) 실수로 이 부분을 리스트에 넣지 않았다고 가정 --> 오류발생 --> 예외처리
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# 이렇게 하면 num1과 num2에 숫자가 아닌 다른 것을 넣으면 에러가 뜬다.
except ValueError: # try내부에 있는 문장을 실행하다가 에러 발생 시 except에서 정의된 에러이면 이렇게 하라는 뜻
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 0으로 나눠서 에러가 떴을 때의 경우(이 상황은 에러문구 그 자체를 표시하라는 뜻)
    print(err)
except: # 따로 적어주지 않은 모든 에러에 대한 상황
    print("알 수 없는 에러가 발생하였습니다.")




