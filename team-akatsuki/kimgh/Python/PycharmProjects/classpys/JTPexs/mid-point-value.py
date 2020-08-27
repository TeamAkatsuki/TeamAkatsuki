a = "5,7,4,9,6,3,1,15"

def median(i):
    list_i = i.split(",")
    list_int = []

    for j in range(len(list_i)):
        list_int.append(int(list_i[j]))
    list_int.sort()

    if len(list_int) % 2 == 1:
        md_i = list_int[int(len(list_int)/2-0.5)]
    else:
        md_i = (list_int[int(len(list_int)/2)] + list_int[int(len(list_int)/2-1)])/2
    return print(md_i)

median(a)
