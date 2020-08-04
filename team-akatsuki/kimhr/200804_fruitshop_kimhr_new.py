import os

report_data = []

def death_list(ramram_string):
    with os.scandir(ramram_string) as entries:
        for entry in entries:
            file_name = entry.name
            print(file_name)
            t_list = transformer_data("{0}\\{1}".format(ramram_string,file_name))
            make_report(t_list)

def transformer_data(ramram):
    data_list = []
    with open(ramram, 'r', encoding='utf8') as f:
        line1 = f.readline()
        line2 = f.readline()
        print(line2)
        black_list = line2.split(",")
        length = len(black_list)
        length = int(length / 2)
        for i in range(length):
            data_list.append([black_list[i * 2],int(black_list[i * 2 + 1])])
    print(data_list)
    return data_list

def check_dupl(item_list):
    for i in range(len(report_data)):
        if report_data[1][0] == item_list[0]:
            return True, i
    return False, None

def make_report(ramram_list):
    for i in ramram_list:
        is_dupl, idx_dupl = check_dupl(i)
        if is_dupl:
            report_data[idx_dupl][1] = i[1] + report_data[idx_dupl][1]
        else:
            report_data.append(i)


    with open('202007.csv', 'w', encoding='utf8') as f:
        for i in report_data:
            f.write("{0},{1}\n".format(i[0],i[1]))

death_list('202007')
