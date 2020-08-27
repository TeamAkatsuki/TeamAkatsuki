source = "a,1,b,2,c,3,a,1,d,2,c,3"
source = source.split(",")
data = []

# for i in source:
# len(source)는 12
# source가 12개 이므로 range(len(source))
# 0,1,2 ... , 10,11을 만든다
# for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
for i in range(len(source)):
    sub_list = []
    if i%2 == 1:
        sub_list.append(source[i-1])
        sub_list.append(int(source[i]))
        data.append(sub_list)

print(data)

data2 = []

for i in range(len(data)):
    # 반복문으로 중복인지만 판다
    double = False
    doublevalue = None
    print(i, double, doublevalue, data, data2)
    for j in range(len(data2)):
        if data2[j][0] == data[i][0]:
            double = True
            doublevalue = j
    if double:
        # 값을 더한다.
        sum = data[i][1] + data2[doublevalue][1]
        data2[doublevalue][1] = sum
    else:
        data2.append(data[i])

print(data2)
