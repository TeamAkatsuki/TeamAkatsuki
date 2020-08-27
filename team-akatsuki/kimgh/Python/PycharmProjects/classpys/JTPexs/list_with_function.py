s = "1,2,3,4"
i = "2"

def find_item(pl,pi):
    temp = False
    for i in pl:
        if i == pi:
            temp = True
    return temp

def doubchk(ps,pi):
    temp = False
    data = ps.split(",")
    if find_item(data,pi):
        temp = True

    return temp

r = doubchk(s,i)
print(r)
