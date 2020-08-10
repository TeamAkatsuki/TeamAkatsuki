
a = 0
for i in range(1,10001):
    i = str(i)
    a = a + i.count("8")
print("8의 총 갯수는?")
print(a,"개")