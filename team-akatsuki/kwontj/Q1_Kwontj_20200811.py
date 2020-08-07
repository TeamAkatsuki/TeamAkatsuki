'''
[사이냅소프트 면접문제]

주어진 문자열 (공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.


이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌



1. 김씨와 이씨는 각각 명 몇인가요? o
2. "이재영"이라는 이름이 몇 번 반복되나요?
3. 중복을 제거한 이름을 출력하세요.
4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
'''

quest_str = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
count_kim = 0
count_yee = 0
count_jaeyoung = 0
trans_list = quest_str.split(",")
empty_list =[]
for a in range(len(trans_list)):
    if trans_list[a][:1] == "김":
        count_kim += 1
    elif trans_list[a][:1] == "이":
        count_yee += 1

for a in range(len(trans_list)):
    if trans_list[a] == "이재영":
        count_jaeyoung +=1

for a in range(len(trans_list)):
    check = False
    for b in range(len(empty_list)):
        if trans_list[a] == empty_list[b]:
            check = True
            break
    if check:
        pass
    else:
        empty_list.append(trans_list[a])


print("1. 김씨는 :",count_kim,"명 이고 이씨는 :",count_yee,"명 입니다")
print("2. 이재영은 총 ",count_jaeyoung,"번 반복되었습니다")
print("3.",empty_list)
empty_list.sort()
print("4.",empty_list)