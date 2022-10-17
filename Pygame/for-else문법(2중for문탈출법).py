balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

# balls[x]에 대해서 weapons의 값들과 모두 비교해보고 맞지 않다면 balls[x+1]에 대해 다시 weapons의 값들과 모두 비교해보면서 맞는 것을 찾는 상황
# 예상대로라면 balls[3]과 weapons[3]의 값이 일치하므로 break문을 타서 프로그램이 종료되기를 바라나 2중 for문이기 때문에 그러지 못하는 상황
for ball_index, ball_value in enumerate(balls):
    print("ball : ", ball_value)
    for weapon_index, weapon_value in enumerate(weapons):
        print("weapon : ", weapon_value)
        if ball_value == weapon_value:
            print("공과 무기가 충돌")
            break
    # 해결방안
    else:
        continue
    # 위의 for문에서 break를 걸어야지만 이 구문을 탈 수 있음
    break

# 해당 스킬을 for-else문이라 말함.