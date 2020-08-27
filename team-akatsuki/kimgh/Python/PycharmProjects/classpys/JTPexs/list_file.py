input_data = []


# kvstr(Key Value String)
def kvstr_to_list(param):
    result = []
    list = param.split(",")
    for i in range(int(len(list)/2)):
        tmp_list = [list[i*2], list[i*2+1]]
        result.append(tmp_list)
    return result




while True:
    kvs = input("상품과 수량을 입력하세요. 예) a,2,b,4 > ")
    new_list = kvstr_to_list(kvs)
    print("{}가 입력되었습니다.".format(new_list))
    input_data = input_data + new_list
    if kvs == 'q':
        break


print(input_data)
