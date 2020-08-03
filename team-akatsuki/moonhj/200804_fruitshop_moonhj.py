import os

report_data = []
# 데이터 저장

def dir_list(param_string):
    with os.scandir(param_string) as entries:
        for entry in entries:
            file_name = entry.name
            print(file_name)
            t_list = transform_data("{0}\\{1}".format(param_string,file_name))
            make_report(t_list)

def transform_data(param):
    data_list = []
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        line2 = f.readline()
        print(line2)
        temp_list = line2.split(",")
        length = len(temp_list)
        length = int(length / 2)
        for i in range(length):
            data_list.append([temp_list[i * 2], int(temp_list[i * 2 + 1])])
    print(data_list)
    return data_list
    print("%s를 처리합니다." % param)

def check_dupl(item_list):
    # 중복여부, 중복인덱스
    for i in range(len(report_data)):
        if report_data[i][0] == item_list[0]:
            return True, i
    return False, None

def make_report(param_list):
    # [['a', 1], ['b', 1], ['a', 1], ['c', 1]]
    for i in param_list:
        # ['a', 1]
        is_dupl, no_dupl  = check_dupl(i)
        if is_dupl:
            report_data[no_dupl][1] = i[1] + report_data[no_dupl][1]
        else:
            report_data.append(i)

    with open('202007.csv', 'w', encoding='utf8') as f:
        for i in report_data:
            f.write("{0},{1}\n".format(i[0], i[1]))

dir_list('202007')
