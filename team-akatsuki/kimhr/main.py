import random

lotto = [] # 로또 리스트를 만들어주고
lucky = random.randint(1,100) # lucky에 1~100을 랜덤으로 할당
lucky2 = random.randint(1,100)

for i in range(6): # 포문으로 6번 반복
    while lucky in lotto:
        lucky = random.randint(1,100)
    lotto.append(lucky)
"""
while문에서 lucky에 골라진 숫자가 이미 lotto에 있으면 다시한번 뽑고
lotto에 없는 숫자가 뽑히면 while문을 탈출하고 리스트에 추가가 된다
"""
if lucky2 == lotto[0]:
    print("축하합니다 1등에 당첨되셨습니다!!당첨번호",lotto[0])
elif lucky2 in lotto[1:]:
    print("축하합니다 2등에 당첨되셨습니다!!당첨번호",lotto[1:])
else:
    print("아쉽습니다ㅠㅠ 다음을 기약하세요 당첨번호",lotto[0],lotto[1:])

# lucky2 변수를 하나더 만들고 if문으로 로또 인덱스와 비교 한후 출력



