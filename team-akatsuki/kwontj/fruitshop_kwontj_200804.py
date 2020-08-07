import os     # os 모듈을 불러온다
import
savelist =[]    # 사용할 변수들 초기화
fg = ""
filelist = []
thirdlist = []
def trans(file): # 인수로 받은 문자열을 이중 리스트로 변환해주는 함수
    e_list = []  # e_list 변수를 초기화
    file = file.split(",")  #인수로 받은 file을 ,기준으로 리스트로 만든후 file에 저장
    if len(file) % 2 == 1:   # 인수로받은 file의 길이가 홀수라면
        print(         # 해당 문자열 출력
"""
입력값이 잘못되었습니다 [상품이름,갯수] 양식으로 입력하세요
=============================""")
        return 0 # 0을 반환한다
    for a in range(int(len(file)/2)): #인수로 받은 file의 길이를 2로 나눈후 정수로 변환한뒤에 a에 하나씩 넣고 코드블럭의 코드를 실행한다
            e_list.append([file[a*2],int(file[a*2+1])])  # e_list에 file의 값을 추가한다
    return e_list # e_list를 반환한다

def joongbok(file,ex_list):   # 두개의 리스트를 받아 중복값을 더한뒤 반환하는 함수
    for a in range(len(file)): # 인수로 받은 file의 길이만큼 range로 차례대로 a에 대입한뒤 코드블럭의 코드 실행
        no_dupl = False # no_dupl변수를 False로 초기화
        for b in range(len(ex_list)):  # //
            if file[a][0] == ex_list[b][0]: # file의 a번째 인덱스의 0번째 값과 ex_list의 b번째 인덱스의 0번째값이 일치하다면
                no_dupl = True # no_dupl 은 True가 되고
                break # for문을 빠져나온다
        if no_dupl: # no_dupl의 값이 참이라면
            ex_list[b][1] = file[a][1] + ex_list[b][1] # ex_list의 b번쨰 인덱스의 첫번째값과 file의 a번쨰 인덱스의 1번째값을 더한뒤 ex_list의 b번째 값의 1번째에 저장한다
        else:# no_dupl의 값이 참이아닐경우
            ex_list.append(file[a]) #ex_list에 file의 a번째 값을 추가한다

    return ex_list # ex_list값을 반환한다

def reading(file):  # 지정된 폴더의 파일을 모두 가져온다

    with open(file,"r") as f: #지정된 경로의 파일을 읽기모드로 연다
        line1 = f.readline() # 불러온파일을 한줄읽은뒤 line1 에 저장
        line2 = f.readline() # 불러온파일을 한줄읽은뒤 line2 에 저장
        if line1 == "testprogram\n": # line1 의 값이 "testprogram"인경우
            return line2 # line2를 반환한다
        else: # line1의 값이 "testprogram"이 아닐경우
            print(""" 
=============================
지원하지 않는 파일입니다
============================="""
            )                             # 해당문자열을 출력한다
            return 0 # 0을 반환한다
while True: # 조건이참일경우 무한반복
    secondlist = [] # 변수 초기화
    savelist = []
    select =input(    # 문자열을 입력받아 select에 저장
"""=============================
1. 상품등록하기
2. 상품파일불러오기
3. 현재상품목록
4. 저장하기 
5. 나가기
=============================""")

    if select == "1": # select가 문자열 1이라면
        first_str = input(""" 
등록하실 상품명을 입력해주세요 : [상품이름,갯수] 양식으로 입력하세요
=============================""") #   문자열을 입력받아 first_str에 저장한다
        first_str = trans(first_str)  # first_str의값을 trans함수의 인수로 보낸뒤 값을반환받아 first_str에 저장한다
        if first_str == 0:   # first_str 의 값이 0이라면
            continue # while문의 맨처음으로 돌아간다
        filelist = joongbok(first_str,filelist) # first_str과 filelist 를 joongbok함수의 인수로 보낸뒤에 반환받은 값을 filelist에 저장한다
        print("상품 추가완료 :",filelist)  # 문자열과 filelist의값을 출력한다
    elif select == "2":  # select값이 2라면
        with os.scandir("kwontj") as entries: #경로의 파일목록을 가져와 entries에 저장한다
            t = 0 # 변수 t초기화
            for entry in entries: # 저장된 파일목록을 한개씩 entry에 대입한뒤 코드블럭의 코드 실행
                t= t+1  # t에 1을 더한뒤 t에 저장한다
                print("%d.%s"%(t,entry.name)) # t의값과 entry에 저장한 파일의 정보에서 파일의 이름만가져온뒤 출력한다
                savelist.append(entry.name) # savelist 리스트에 파일이름을 추가한다
            print("불러오실 파일을 선택해주세요 : ") # 해당 문자열 출력
            select2 = input() # 문자열을 입력받은뒤 select2에 저장한다
            select2 = int(select2) # select2 의 값을 정수형으로 바꿔준뒤 select2에 다시 저장한다
            if t == 0:  #만약 t의 값이 0 이라면
                continue #while 문의 처음으로 돌아간다
            if select2: # select2의 값이 참이라면
                g = reading("kwontj\\%s"%savelist[select2-1]) # savelist의 인덱스 값이 파일이름을 대입한뒤 파일을 읽어오고 g에 저장한다
                if g != 0: # g가 0이 아니라면
                    print(savelist[select2 - 1], "불러오기 성공") # savelist의 파일이름을 가져오고 문자열을 출력한다
                    g = trans(g) # g의값을 trans함수의 인수로 보낸뒤 반환값을 g에 저장한다
                    g = joongbok(g,secondlist) # g의 값과 secondlist를 joongbok함수의 인수로 보낸뒤 반환값을 g에 저장한다
                    print(g)  # g의 값을 출력
                    subselect = input("""
1. 저장하기
2. 취소 """)                  # 문자열을 입력받고 subselect에 저장한다
                else: # 조건이 거짓이라면
                    subselect = "3"   # subselect의값은 3이다
                if subselect == "1": # subselect 의값이 1이라면
                    filelist = joongbok(g,filelist) # g와 filelist를 joongbok함수의 인수로 보낸뒤에 반환값을 filelist의 값에 저장한다
                elif subselect == "2":  # subselect의 값이 2라면
                    secondlist = []  # subselect를 빈리스트로 초기화한다
                elif subselect == "3": # subselect의값이 3이라면
                    continue # while문의 처음으로 돌아간다
    elif select == "3": # select의 값이 3이라면
        print("현재 상품 목록")  # 해당문자열 출력
        if filelist == []:  # filelist가 빈리스트라면 코드블럭의 코드 실행
            print("상품목록이 비어 있습니다")   # 해당문자열 출력
        else: # 조건이 거짓이라면
            print(filelist) #filelist를 출력한다

    elif select == "4":  # select의 값이 4라면
        if filelist == []: # filelist가 빈리스트라면
            print("저장할 상품이 없습니다") # 해당문자열 출력
        else: # 거짓이라면
            select3 = input(
            """저장하실 파일이름을 적어주세요
============================="""
            ) # 문자열을 입력받고 select3에 저장한다
            select4 = input("""
저장하실 파일의 형식을 선택해주세요
1. 텍스트 파일 (TXT)
2. 엑셀 파일 (CSV)
=============================""") # 문자열을 입력받고 select4에 저장한다
            if select4 == "1": # select4의 값이 1이라면
                f = open("kwontj\\%s.txt"%select3, "w") # 경로상의 파일을 쓰기모드로 오픈 파일이 없다면 파일생성
            elif select4 == "2": # select4의 값이 2라면
                f = open("kwontj\\%s.csv"%select3, "w") # 경로상의 파일을 쓰기모드로 오픈 파일이 없다면 파일생성
            else: # 조건이 거짓이라면
                print("입력값이 잘못되었습니다") # 해당 문자열 출력
                continue # while문의 처음으로 돌아간다

            for a in range(len(filelist)): # filelist의 길이만큼 range에 넣은뒤 a에 차례대로 대입후 코드블럭의 코드 실행
                filelist[a][1] = str(filelist[a][1]) # filelist의 a번째 인덱스의 첫번째값을 문자열로 변환한뒤 저장
                #for b in range()
                thirdlist.append(filelist[a][0]) # thirdlist에
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


