fruits = "apple,145,banana,28,apple,49,kiwi,564,apple,75,banana,16,kiwi,92".split(",")

pairs = []
temp_pairs = []

for i in range(len(fruits)):
    temp_pairs = []
    if i % 2 == 1:
        temp_pairs.append(fruits[i-1])
        temp_pairs.append(int(fruits[i]))
        pairs.append(temp_pairs)

sum_list = []

for i in pairs:
    double = False
    doublepos = None
    for j in range(len(sum_list)):
        if i[0] == sum_list[j][0]:
            double = True
            doublepos = j
    if double:
        sum_list[j][1] = i[1] + sum_list[j][1]
    else:
        sum_list.append(i)

print(sum_list)

