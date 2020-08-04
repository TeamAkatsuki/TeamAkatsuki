import os


#################################################################

def sale_sort(param):
    param = param.split(",")
    dic = {}
    for i in range(len(param)):
        if i % 2 == 0:
            if not param[i] in dic:
                dic[param[i]] = int(param[i + 1])
            else:
                dic[param[i]] += int(param[i + 1])
    return dic


################################################################


def sale_trans(param):
    with open(param, 'r', encoding='utf8') as f:
        line1 = f.readline()
        line2 = f.readline()

    return sale_sort(line2)


################################################################


def sale_file(param):
    with open("sale.csv", "w", encoding="utf8") as f:
        for i in param:
            f.write("{},{}\n".format(i, param.get(i)))


################################################################


def sale_finish(param):
    with os.scandir(param) as entries:
        for entry in entries:
            file_name = entry.name
            sale_list = sale_trans("{}\\{}".format(param, file_name))
    return sale_list
################################################################

sale_file(sale_finish("sale_box"))
