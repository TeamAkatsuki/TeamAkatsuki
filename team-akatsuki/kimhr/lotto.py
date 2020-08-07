from random import randint

a = 1
b = [2,3,4,5,6]



while True:
    c = randint(1, 101)
    select = input("""
1.뽑기
2.나가기""")

    if select == "1":

        if a == c:
            print("1등 당첨되셨습니다!! 경품은 자동차입니다.")

        elif c in b:
            print("2등 입니다! 경품은 냉장고입니다.")

        else:
            print("꽝입니다.다음에 또 이용해주세요~")
    elif select == "2":
        print("종료합니다.")
        break