#1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

num_str = ''
for i in range(1,10001):
    num_str += str(i)
print(num_str.count('8'))