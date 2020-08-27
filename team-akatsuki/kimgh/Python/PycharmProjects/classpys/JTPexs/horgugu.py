f = open("horgugu.txt","w")

for i in [2,5,8] :
    if i == 8:
        f.write("====%d단====  ====%d단====" % (i, i + 1))
        f.write('\n')
        for j in range(1, 10):
            f.write("%d x %d = %2d   %d x %d = %2d"
                  % (i, j, i * j, (i + 1), j, (i + 1) * j))
            f.write('\n')

    else:
        f.write("====%d단====  ====%d단====  ====%d단====" % (i, i + 1, i + 2))
        f.write('\n')
        for j in range(1,10):

            f.write("%d x %d = %2d   %d x %d = %2d   %d x %d = %2d"
                  %(i,j,i*j,(i+1),j,(i+1)*j,(i+2),j,(i+2)*j))
            f.write('\n')

f.close()

