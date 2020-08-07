# n명 추첨 1등 자동차 1명 2등 냉장고 5명 나머지 꽝
import random


def all_zebi(members):
    zebis = []
    for i in range(1,members+1):
        zebis.append(i)
        random.shuffle(zebis)
    return zebis

def pick_zebi(all_zebi):
    for j in all_zebi:
        input("\n준비가 되면 엔터를 눌러주세요!\n")
        print("""==============================
    당신의 제비는 {}번입니다!
==============================\n""".format(j))
        input("결과는?\n")
        if j == 1:
            print("""******************************
**********1등 자동차!**********
******************************\n""")
        elif j in [2,3,4,5,6]:
            print("""******************************
**********2등 자동차!*********
******************************\n""")
        else:
            print("""******************************
**********  꽝 ㅠㅠ **********
******************************\n""")

############################################
while True:
    try:
        a = input("\n********몇 명이 제비를 뽑을까요?*********\n")
        pick_zebi(all_zebi(int(a)))
    except ValueError:
        print("\n다시 입력하세요!\n")
