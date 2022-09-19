# 계좌입금의 예

def deposit(balance, money):  # balance == 잔액, money == 입금액
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

# 계좌출금의 예

def withdraw(balance, money): 
    if balance >= money: # 잔액이 출금보다 많을때
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else: # 잔액이 출금보다 적을때
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance

# 저녁출금에는 수수료가 붙는 상황

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    if balance >= money + commission:
        print("출금이 완료되었습니다. 잔액은 {0} 원이고, 수수료는 {1} 원입니다.".format(balance - money - commission, commission))
        return commission, balance - money - commission # 수수료와 잔액을 같이 반환해줘야 한다.
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return commission, balance



balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000) 출금불가
balance = withdraw_night(balance, 500)



