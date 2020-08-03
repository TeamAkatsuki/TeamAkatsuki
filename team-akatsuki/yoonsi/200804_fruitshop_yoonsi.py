# input "a,1,b,2,a,3"
sales = "a,1,b,2,a,3"
list = sales.split(",")         #문자열 파일을 리스트로 변환
data = []
data2 = []
#print(list)
# list = ['a',1,'b',2,'a',3]

length = len(list)    # 6회 ex) 0,1,2,3,4,5
for i in range(length):
    if i % 2 == 1: # 2로 나눠서 나머지가 1이 되면 data에넣어라
        data.append([list[i-1],int(list[i])])
print(data)
# data = [['a',1],['b',2],['a',3]]


#j 0 ['a',1] 을 돌려서 없기 때문에 data2 ['a',1] 값을 넣음
#j 1 ['b',2] 을 돌려서 없기 때문에 data2 ['a',1]['b',2]
#j 2 ['a',3] 을 돌릴때 if에 걸리기 때문에 data2 ['a',4]['b',2]

for j in data:        #j에다 data['a',1],['b',2],['a',3]를 넣어라
    is_dupl = False   #            0        1       2
    no_dupl = None
    for k in range(len(data2)):     #k에다가 data2의 인덱스 값을 순서대로
        if data2[k][0] == j[0]:     #만약 range(len(data2)) 값을 도는 도중에 중복을 만나면
            is_dupl = True
            no_dupl = k
    if is_dupl:
        data2[no_dupl][1] = j[1] + data2[no_dupl][1]
    else:
        data2.append(j)
print("="*30)
print(data2)


