import random

추첨 = range(1,101)
print("자동차" , random.sample (추첨 , 1 ))
print("냉장고" , random.sample(추첨 , 5))
# 해결할 문제 추첨한 자동차 당첨 번호와 냉장고 당첨 번호끼리 중복일 경우가 있을수 있음
# 프로그램이라 보기에 힘든것 같음

#############################################################################


import random


def choice(pi):
    while True:
        choice = range(1, pi+1)
        car = random.sample(choice, 1)
        fridge = random.sample(choice, 5)
        if car[0] not in fridge:
            print('자동차 당첨', car)
            print('냉장고 당첨', fridge)
        else:
            continue
        break

choice(6)
