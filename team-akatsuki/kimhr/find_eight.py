# 1부터 10000까지 8 숫자가 몇번 나오는가?
pal = 0
for i in range(1,10001):
    pal = pal + str(i).count("8")
print(pal)