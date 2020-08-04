import os

report_data = []

def dir_list(pram_string):
    with os.scandir(paaram_string) as entries:
        for entry in entries:
            file_name = entry.name
            print(file_name)
            t_list = transform_data("{0}\\{1}".format(param_string, file_name))
def dir_list(pram_string):                                                      #이 부분 설명 해줄 분 구합니다
    with os.scandir(param_string) as entries:                                   #이 부분 설명 해줄 분 구합니다
        for entry in entries:                                                   #이 부분 설명 해줄 분 구합니다
            file_name = entry.name                                              #이 부분 설명 해줄 분 구합니다
            print(file_name)                                                    #이 부분 설명 해줄 분 구합니다
            t_list = transform_data("{0}\\{1}".format(param_string, file_name)) #이 부분 설명 해줄 분 구합니다

def transform_data(param):
    data_list = []
    with open(param, 'r', encoding='utf8') as f: #이 부분 설명 해줄 분 구합니다
        line1 = f.readline()  #한줄씩 추가
        line2 = f.readline()  #한줄씩 추가
        print(line2) #s1_20200729_1 => a,1,d,2,s,3,c,4,s,5,d,3
                     #s1_20200729_2 => a,2,d,3,d,4,v,3,s,2,a,1,s,2
                     #s2_20200729_1 => a,2,d,2,s,4,c,4,s,5,d,3
                     #s2_20200729_2 => a,1,d,3,d,6,v,3,s,1,a,2,s,2
        temp_list = line2.split(",")
        length = len(temp_list)
        length = int(length / 2)
        for i in range(length):
            data_list.append([temp_list[i*2], int(temp_list[i*2+1])])
        print(data_list)    #[['a', 1], ['d', 2], ['s', 3], ['c', 4], ['s', 5], ['d', 3]]
                            #[['a', 2], ['d', 3], ['d', 4], ['v', 3], ['s', 2], ['a', 1], ['s', 2]]
                            #[['a', 2], ['d', 2], ['s', 4], ['c', 4], ['s', 5], ['d', 3]]
                            #[['a', 1], ['d', 3], ['d', 6], ['v', 3], ['s', 1], ['a', 2], ['s', 2]]
        return data_list
        print("%s를 처리합니다." % param) #이거 프린트 하는데도 안뜨는 이유 좀 알려주실분? 선생님걸로도 안떠요.

def check_joongbok(item_list):
    for i in range(len(report_data)):
        if report_data[i][0] == item_list[0]:
            return True, i #여기에 쓰이는 i는 왜 써야하는지 설명 부탁드립니다.
    return False, None

def make_report(param_list):
    for i in param_list:
        is_joongbok, no_joongbok = check_joongbok(i)
        if is_joongbok:
            report_data[no_joongbok][1] = i[1] + report_data[no_joongbok][1]

        else:
            report_data.append(i)

    print(report_data)  #[['a', 1], ['d', 5], ['s', 8], ['c', 4]]
                        #[['a', 4], ['d', 12], ['s', 12], ['c', 4], ['v', 3]]
                        #[['a', 6], ['d', 17], ['s', 21], ['c', 8], ['v', 3]]
                        #[['a', 9], ['d', 26], ['s', 24], ['c', 8], ['v', 6]]

    with open('202007_2.txt', 'w', encoding = 'utf8') as f:
        for i in report_data:
            f.write("{0},{1}\n").format(i[0],i[0])

dir_list('202007')
