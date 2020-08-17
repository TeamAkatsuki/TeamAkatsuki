import random

france = ["돈까스", "짜장면", "햄버거", "냉면", "덮밥", "초밥", "삼겹살", "라면"]
random.shuffle(france)

f = []

def ideal_type():
    if len(a)%2 == 0:
        loop = len(a) // 2
        for i in range(0, loop):
            while True:
                if loop == 1:
                    print("<<결승>>\n")
                else:
                    print("<<제 %d강>>\n" %(2*loop))
                print("%s vs %s" %(a[i], a[i+1]))
                print("왼쪽음식이 끌리면 1번,오른쪽음식이 끌리면 2번을 선택")
                print("\n 입력:", end= ' ')
                temp = int(input())
                print()
                if temp == 1:
                    a.remove(a[i+1])
                    break
                elif temp == 2:
                    a.remove(a[i])
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print()

    elif len(a)%2 != 0: #홀수명이면 한 명 부전승
        workover = a[-1]  #부전승
        a.remove(a[-1])
        loop = len(a) // 2
        for i in range(0, loop): #대결 팀 배정
            while True:
                if loop == 1:
                    print("<<결승>>\n")
                else:
                    print("<< 제 %d강 >>\n " %(2*loop))
                print("%s vs %s" %(a[i], a[i+1]))
                print("왼쪽음식이 끌리면 1번,오른쪽음식이 끌리면 2번을 선택")
                print("\n 입력:", end = ' ')
                temp = int(input())
                print()
                if temp == 1:
                    a.remove(a[i+1])
                    break
                elif temp == 2:
                    a.remove(a[i])
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print()
        a.append(workover)

while True:
    print("실행하려면 1번 종료하려면 2번을 입력하세요.")
    print("\n 입력:", end= '')
    c = int(input())
    print()
    if c == 1:
        a = france[:]
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")


while len(a) != 1:
    ideal_type()

print("당신의 오늘 점심은", a[0], "입니다.")