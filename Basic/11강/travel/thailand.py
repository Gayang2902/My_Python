class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__": # 모듈이 직접적으로 실행됐는지를 확인 할 수 있는 구문
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 떄만 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()

else: 
    print("Thailand 외부에서 모듈 호출")

