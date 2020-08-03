import os


def sale_scan(param):
    with os.scandir(param) as entries:
        for entry in entries:
            sale_file = entry.name
            sale_list = sale_dic("{}\\{}".format(param,sale_file))
    return sale_file

def sale_dic(param):
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        line2 = f.readline()
        line2 = line2.split(",")
        dic = {}
        for i in range(len(line2)):
            if i % 2 == 0:
                if not line2[i] in dic:
                    dic[line2[i]] = int(line2[i + 1])
                else:
                    dic[line2[i]] += int(line2[i + 1])
        return dic

def make_file(param):
    with open('sale_list.csv','w',encoding='utf8') as f:
        for i in dic:
            f.write("{},{}\n".format(i[0],i[1]))

sale_dic(sale_scan("sale_list\\"))
