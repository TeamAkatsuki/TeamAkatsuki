f = open("gugudan.txt", "w")

i = 1

while i < 9:
    i = i + 1

    f.write('='*5)
    f.write('%d단'%i)
    f.write('='*5)
    f.write('\n')


    for j in range(1,10):
        data ="{} 곱하기 {} = {}\n".format(i, j, i * j)
        f.write(data)

f.close()
