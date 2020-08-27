#############
f = open('9.file.txt','w')

for i in range(1,10):
    txt = "파일 쓰기를 %d번 실행하자!\n"%i
    f.write(txt)
f.close()






#############
f = open('9.file.txt','r')
data=f.read()
print(data)
f.close()
#############