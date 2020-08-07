import random

추첨 = range(1,101)
print("자동차" , random.sample (추첨 , 1 ))
print("냉장고" , random.sample(추첨 , 5))
# 해결할 문제 추첨한 자동차 당첨 번호와 냉장고 당첨 번호끼리 중복일 경우가 있을수 있음
# 프로그램이라 보기에 힘든것 같음
