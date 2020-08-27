data = "apple,145,banana,28,apple,49,kiwi,564,apple,75,banana,16,kiwi,92"

index = 0
unit = ''
deci = ''
all_product = ''
all_amount = ''

for i in data:
    #print("i={} / index={} / unit={} / deci={} / all_product={} / all_amount={}".format(i,index,unit,deci,all_product,all_amount))
    if i != ",":
        unit = unit + i
    else:
        index = index +1
        deci = unit
        unit = ''
        if index % 2 == 1:
            all_product = all_product + "{0:<10}".format(deci)
        else:
            all_amount = all_amount + "{0:<10}".format(deci)

all_amount = all_amount + "{0:<10}".format(unit)

print('\n','\n',"Match list","="*300,'\n','\n')

print(all_product)
print(all_amount)


##########################################################################################################

print('\n','\n',"Sum list","="*300,'\n','\n')


