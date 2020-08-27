def calc(ip,op):
    result = None
    if ip[0] == "+":
        result = op + int(ip[1:])
    elif ip[0] == "-":
        result = op - int(ip[1:])
    elif ip[0] == "*":
        result = op * int(ip[1:])
    elif ip[0] == "/":
        result = op / int(ip[1:])
    else:
        print("형식에 맞게 입력해주세요! ex)+2 *4 /6 -12")
    return result


sum = None
sum = int(input("첫 값을 입력하세요.\n"))

while True:
    num_now = input("기호와 숫자를 입력하세요. -> +2 *4 /6 -12 \n'q'를 입력하면 종료됩니다.\n")
    if num_now == 'q':
        break
    sum = calc(num_now,sum)
    print(sum)

