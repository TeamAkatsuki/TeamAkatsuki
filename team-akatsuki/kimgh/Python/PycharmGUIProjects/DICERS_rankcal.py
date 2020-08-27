import operator

def r_sort():
    with open('ranks/rich.txt', 'r', encoding='utf-8') as f:
        r_list = f.readline()[:-1].split(",")
        if len(r_list) > 22:
            del r_list[23:]
        r_dict = {}

        for i in range(0, len(r_list), 2):

            if not r_list[i] in r_dict:
                r_dict[r_list[i]] = int(r_list[i+1])

            if r_list[i] in r_dict:
                if int(r_dict[r_list[i]]) >= int(r_list[i+1]):
                    pass

                elif int(r_dict[r_list[i]]) < int(r_list[i+1]):
                    r_dict[r_list[i]] = int(r_list[i+1])

        sorted_r = sorted(r_dict.items(), reverse= True, key= operator.itemgetter(1))
        with open('ranks/rich.txt', 'w', encoding='utf-8') as f2:
            for i in sorted_r:
                for j in range(2):
                    f2.write(str(i[j]))
                    f2.write(',')
    return sorted_r[0][0], sorted_r[0][1], sorted_r[1][0], sorted_r[1][1], sorted_r[2][0], sorted_r[2][1]


def l_sort():
    with open('ranks/long.txt', 'r', encoding='utf-8') as f:
        l_list = f.readline()[:-1].split(",")
        if len(l_list) > 22:
            del l_list[23:]

        l_dict = {}

        for i in range(0, len(l_list), 2):

            if not l_list[i] in l_dict:
                l_dict[l_list[i]] = int(l_list[i + 1])

            if l_list[i] in l_dict:
                if int(l_dict[l_list[i]]) >= int(l_list[i + 1]):
                    pass

                elif int(l_dict[l_list[i]]) < int(l_list[i + 1]):
                    l_dict[l_list[i]] = int(l_list[i + 1])
        sorted_l = sorted(l_dict.items(), reverse=True, key=operator.itemgetter(1))
        with open('ranks/long.txt', 'w', encoding='utf-8') as f2:
            for i in sorted_l:
                for j in range(2):
                    f2.write(str(i[j]))
                    f2.write(',')
    return sorted_l[0][0], sorted_l[0][1], sorted_l[1][0], sorted_l[1][1], sorted_l[2][0], sorted_l[2][1]

def c_sort():
    with open('ranks/clever.txt', 'r', encoding='utf-8') as f:
        c_list = f.readline()[:-1].split(",")
        if len(c_list) > 22:
            del c_list[23:]
        c_dict = {}

        for i in range(0, len(c_list), 2):

            if not c_list[i] in c_dict:
                c_dict[c_list[i]] = float(c_list[i+1])

            if c_list[i] in c_dict:
                if float(c_dict[c_list[i]]) >= float(c_list[i+1]):
                    pass

                elif float(c_dict[c_list[i]]) < float(c_list[i + 1]):
                    c_dict[c_list[i]] = float(c_list[i + 1])

        sorted_c = sorted(c_dict.items(), reverse = True, key = operator.itemgetter(1))
        with open('ranks/clever.txt', 'w', encoding='utf-8') as f2:
            for i in sorted_c:
                for j in range(2):
                    f2.write(str(i[j]))
                    f2.write(',')

    return sorted_c[0][0], sorted_c[0][1], sorted_c[1][0], sorted_c[1][1], sorted_c[2][0], sorted_c[2][1]

try:
    r_sort()
    l_sort()
    c_sort()

except IndexError:
    pass