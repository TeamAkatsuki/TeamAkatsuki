import os


def sale_str(p_dir):
    all_str = ''
    with os.scandir(p_dir) as entries:
        for entry in entries:
            file_name = entry.name
            with open("{}\\{}".format(p_dir, file_name), 'r', encoding='utf8') as file:
                line1 = file.readline()
                line2 = file.readline() + ','
                all_str += line2
    return all_str[:-1]


def sale_dic(p_str):
    p_list = p_str.split(",")
    all_dic = {}
    for i in range(len(p_list)):
        if i % 2 == 0:
            if not p_list[i] in all_dic:
                all_dic[p_list[i]] = int(p_list[i + 1])
            else:
                all_dic[p_list[i]] += int(p_list[i + 1])
    return all_dic


def sale_csv(p_dic):
    with open("sale_file.csv", 'w', encoding='utf8') as sale_file:
        for i in p_dic:
            sale_file.write("{},{}\n".format(i, p_dic[i]))

####################################################################
sale_csv(sale_dic(sale_str("sale_box")))
