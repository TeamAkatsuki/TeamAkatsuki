import random

def choice(ci):
    while True:
        choice = range(1, ci+1)
        car = random.sample(choice, 1)
        fridge = random.sample(choice, 5)
        if car[0] not in fridge:
            print('자동차 당첨번호', car)
            print('냉장고 당첨번호', fridge)
        else:
            continue
        break

choice(6)