import random


class Set():
    def __init__(self):
        self.prizelist = []   # 전체 상품리스트
        self.secondprize = [] # 2등 추첨번호를 담을 리스트
        for length in range(1,101):
            self.prizelist.append(length) # 상품리스트에 1에서 100까지 요소 추가

        self.firstprize = self.prizelist.pop(random.randint(0,99)) # 전체상품리스트에서 랜덤자리의 인덱스를 빼와서 firstprize변수에 대입
        for a in range(5): # 5번 반복
            self.secondprize.append(self.prizelist.pop(random.randint(0,len(self.prizelist)-1))) # 전체상품리스트에서 랜덤자리의 인덱스 5개를 빼와서 2등리스트에 요소로 추가한다
        self.prizelist.append(self.firstprize) # 전체상품리스트에서 빼왓던 firstprize의값을 전체상품리스트에 다시 넣는다

        for _add in self.secondprize: # 2등 리스트의 각 요소들을  _add에 담고 코드블럭의 코드 실행
            self.prizelist.append(_add) #  _add의 값을 전체상품리스트에 다시 넣는다

    def bbobgi(self):
        pass

prize = Set()

while True:
    select = input(
"""
=====================
1. 뽑기
2. 나가기
=====================
""")
    if select == "1":
        me_pick = prize.prizelist.pop(random.randint(0,len(prize.prizelist)))
        print("뽑으신 추첨번호는 {}번 입니다".format(me_pick))
        select = input("""결과를확인하시려면 아무키나 눌러주세요""")
        if  select:
            if me_pick == prize.firstprize:
                print("축하합니다 1등 자동차에 당첨되셨습니다")
            elif me_pick in prize.secondprize:
                print("축하합니다 2등 냉장고에 당첨되셨습니다")
            else:
                print(
"""
=====================
당첨되지 않았습니다. 뽑으신  추첨번호는 [{2}]번 입니다
당첨 번호는 1등 [{0}]번 2등  {1}번입니다
=====================
""".format(prize.firstprize,prize.secondprize,me_pick)
)
    elif select == "2":
        print("종료합니다")
        break
    select = input(
"""
=====================
1.다시뽑기
2.초기화하기
=====================
""")
    if select  ==  "1":
        print("남아있는 추첨권은 {}개 입니다".format(len(prize.prizelist)))
        continue
    elif select  ==  "2":
        prize = Set()
        print("뽑기가 초기화 되었습니다")
        continue




