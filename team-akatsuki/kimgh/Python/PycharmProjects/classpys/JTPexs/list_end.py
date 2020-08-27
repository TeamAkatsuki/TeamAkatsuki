import os


def transform_data(sales_data):
    data = []
    temp_list = sales_data.split(",")
    for i in range(int(len(temp_list) / 2)):
        data.append([temp_list[i * 2], int(temp_list[i * 2 + 1])])
    return data


def chk_item_dupl(list, item):
    for i in range(len(list)):
        if list[i][0] == item[0]:
            return True, i
    return False, None


def calc_total(main_list, sub_list):
    for i in range(len(sub_list)):
        item = sub_list[i]
        is_dupl, no_dupl = chk_item_dupl(main_list, item)
        # is_dupl = True, no_dupl = 2
        if is_dupl:
            main_list[no_dupl][1] = item[1] + main_list[no_dupl][1]
        else:
            main_list.append(item)


def read_data(param):
    with open(param, 'r', encoding='utf8') as f:
        # line1은 파일 검증을 위해 사용 - zim의 텍스트 파일 참고
        line1 = f.readline()
        line2 = f.readline()
        return line2


if __name__ == "__main__":
    sales = []
    data2 = []

    with os.scandir('202007') as entries:
        for entry in entries:
            print(entry.name)
            sale = read_data("202007\\%s" % entry.name)
            sales.append(sale)

    for sale in sales:
        list = transform_data(sale)
        calc_total(data2, list)

    print(data2)
