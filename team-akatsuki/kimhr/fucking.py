import os # 오예스

report_data = [] # 리포트 데이타 공간을 만들어줌
# 데이터 저장

def dir_list(param_string): # dir_list에 매개변수 파람을 넣어줌
    with os.scandir(param_string) as entries:
        for entry in entries: # 엔트리s만큼 for문을 돌린다
            file_name = entry.name # 엔트리이름을 파일에 대입 (a b)
            t_list = transform_data("{0}\\{1}".format(param_string,file_name))
            make_report(t_list)

def transform_data(param):
    data_list = []
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline() #
        line2 = f.readline()
        temp_list = line2.split(",") # 라인2를 리스트로 만들고 템프리스트에 대입
        length = len(temp_list) # 템프리스트 길이를 렝스에 대입
        length = int(length / 2) # 대입한걸 정수로 바꾸고 2로 나눔
        for i in range(length): # 나눈걸 전자렌지에 돌림
            data_list.append([temp_list[i * 2], int(temp_list[i * 2 + 1])]) # 템프에 리스트를 2차원으로 만들어줌
    return data_list #

def check_dupl(item_list):
    # 중복여부, 중복인덱스
    for i in range(len(report_data)): # 리포트 데이타 길이만큼 돌린다
        if report_data[i][0] == item_list[0]: # 레포트 i의 0번인덱스가 아이템의 0번인덱스가 같으면 트루
            return True, i
    return False, None                   # 아니면 폴스를 반환

def make_report(param_list):
    # [['a', 1], ['b', 1], ['a', 1], ['c', 1]]
    for i in param_list: # 파람 리스트를 포문으로 돌림
        # ['a', 1]
        is_dupl, idx_dupl  = check_dupl(i) # 체크를 이즈랑 아이디엑스에 각각대입
        if is_dupl: # 그리고 돌림
            report_data[idx_dupl][1] = i[1] + report_data[idx_dupl][1] # i의 1번인덱스 레포트 idx의 1번인덱스를 합치고 리포트에 대입
        else: #아니면
            report_data.append(i) # 레포트에 i를 추가가

   # csv 출력 형식으로 파일을 저장한다.
    with open('200804.csv', 'w', encoding='utf8') as f:
        for i in report_data:
            f.write("{0},{1}\n".format(i[0],i[1]))

dir_list('200804')