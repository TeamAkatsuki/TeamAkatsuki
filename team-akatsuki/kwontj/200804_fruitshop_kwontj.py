import os

savelist =[]
fg = ""
filelist = []

thirdlist = []
def trans(file):
    e_list = []
    file = file.split(",")
    for a in range(int(len(file)/2)):
            e_list.append([file[a*2],int(file[a*2+1])])

    return e_list

def joongbok(file,ex_list):
    for a in range(len(file)):
        no_dupl = False
        for b in range(len(ex_list)):
            if file[a][0] == ex_list[b][0]:
                no_dupl = True
                break
        if no_dupl:
            ex_list[b][1] = file[a][1] + ex_list[b][1]
        else:
            ex_list.append(file[a])

    return ex_list
def reading(file):

    with open(file,"r") as f:
        line1 = f.readline()
        line2 = f.readline()
        if line1 == "testprogram\n":
            return line2
        else:
            print("""
=============================
지원하지 않는 파일입니다
============================="""
            )
            return 0
while True:
    secondlist = []
    savelist = []
    select =input(
"""=============================
1. 상품등록하기
2. 상품파일불러오기
3. 현재상품목록
4. 저장하기 
5. 나가기
=============================""")

    if select == "1":
        first_str = input("""
등록하실 상품명을 입력해주세요 : [상품이름,갯수] 양식으로 입력하세요
=============================""")
        first_str = trans(first_str)
        filelist = joongbok(first_str,filelist)
        print("상품 추가완료 :",filelist)
    elif select == "2":
        with os.scandir("kwontj") as entries:
            t = 0



            for entry in entries:
                t= t+1
                print("%d.%s"%(t,entry.name))
                savelist.append(entry.name)
            select2 = input()
            select2 = int(select2)
            if t == 0:
                continue
            if select2:
                g = reading("kwontj\\%s"%savelist[select2-1])
                print(savelist[select2-1],"불러오기 성공")
                if g != 0:
                    g = trans(g)
                    g = joongbok(g,secondlist)
                    print(g)
                    subselect = input("""
1. 저장하기
2. 취소 """)
                else:
                    subselect = "3"
                if subselect == "1":
                    filelist = joongbok(g,filelist)
                elif subselect == "2":
                    secondlist = []
                elif subselect == "3":
                    continue
    elif select == "3":
        print("현재 상품 목록")
        if filelist == []:
            print("상품목록이 비어 있습니다")
        else:
            print(filelist)

    elif select == "4":
        if filelist == []:
            print("저장할 상품이 없습니다")
        else:
            select3 = input(
            """저장하실 파일이름을 적어주세요
============================="""
            )
            select4 = input("""
저장하실 파일의 형식을 선택해주세요
1. 텍스트 파일 (TXT)
2. 엑셀 파일 (CSV)
=============================""")
            if select4 == "1":
                f = open("kwontj\\%s.txt"%select3, "w")
            elif select4 == "2":
                f = open("kwontj\\%s.csv"%select3, "w")
            else:
                print("입력값이 잘못되었습니다")
                continue

            for a in range(len(filelist)):
                filelist[a][1] = str(filelist[a][1])
                #for b in range()
                thirdlist.append(filelist[a][0])
                thirdlist.append(filelist[a][1])


            fg = ",".join(thirdlist)
            filelist = []
            f.write("testprogram\n")
            f.write(fg)
            print(
            """저장 성공 현재상품목록을 초기화합니다
=============================""")
            f.close()
    elif select == "5":
        print("종료합니다")
        break
    else:
        print("다시 선택해주세요")
        continue


