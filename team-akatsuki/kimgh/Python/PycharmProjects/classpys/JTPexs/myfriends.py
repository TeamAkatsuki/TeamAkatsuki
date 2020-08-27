dic = {'서울' : 'a,b', '대전' : 'c,b,e', '대구' : 'a,d,f'}

my_set = set()

for i in dic.values():
    di_li = i.split(',')
    di_li_se = set(di_li)
    my_set = my_set | di_li_se

my_number = len(list(my_set))
print("친구는 총 {}명!\n" .format(my_number))
print('my_set =',my_set)
print('dic.keys() =',dic.keys())


text = ''
for k in my_set:
    temp = ''
    for j in dic.keys():
        if k in dic[j]:
            temp = temp + ',' + j
    text = text + "{} = {}\n".format(k,temp)
print(text)