'''
[ 앞뒤가 같은 수 ]
앞뒤가 같은 수는 바로 쓴 값과 거꾸로 쓴 값이 같은 수이다. 다음과 같은 예를 들 수 있다.
1
44
101
2002
8972798
111111111111
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ......
과 같이 0 이상의 앞 뒤가 같은 수를 크기 순으로 나열할 때, n 번째 수를 계산하는 프로그램을 작성하라.
n은 1부터 시작하며, 크기에는 제한이 없다.
for instance
n -> f(n)
1 -> 0
4 -> 3
30 -> 202
100 -> 909
30000 -> 200000002
1000000 -> 90000000009
'''

def main_count(list,data):
    _a = list[data]
    ",".join(_a)
    _a = _a.replace(",","")

    return int(_a)

count = 0
empty_list = []
for a in range(0,10000):
    a = str(a)
    a = ",".join(a)
    a = a.split(",")
    b = a.copy()
    a.reverse()
    print(a,b)
    if len(a) % 2 == 0:
        if a == b:
            empty_list.append(",".join(b))
    elif len(a) % 2 == 1:
        count2 = int(len(a)/2)
        if a[count2-1] == b[count2-1]:
            empty_list.append(",".join(b))


print(empty_list)
print(main_count(empty_list,20))
while True:
    select = input("x번째 수를 입력하세요\n종료하실려면 q를 입력하세요")
    if select == "q":
        break

    print(main_count(empty_list,int(select)-1))
