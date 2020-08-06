import os

def sibal():
    f = open('202020\\soso1.txt','r')
    yogo = f.readline()
    return yogo

def ramram(fruits):
    dick = fruits.split(",")# [kiwi,1,....kiwi,9]
    sexy = []
    for i in range(int(len(dick)/2)):
        sexy.append([dick[i*2],int(dick[i*2+1])]) # [kiwi,5]
    return sexy

def lol(b_b):
    volvo = []
    for i in range(len(b_b)):
        is_dupl = False
        for j in range(len(volvo)):
            if b_b[i][0] == volvo[j][0]:
                is_dupl = True
                break
        if is_dupl:
            volvo[j][1] = int(b_b[i][1]) + int(volvo[j][1])
        else:
            volvo.append(b_b[i])


    return volvo










a = sibal()
b = ramram(a)
print(b)
print(lol(b))







