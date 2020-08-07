#1. 김씨와 이씨는 각각 몇 명인가요?
print('1. 김씨와 이씨는 각각 몇 명인가요?')
source = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
kim = 0
lee = 0
kim+=source.count("김")
lee+=source.count("이")
print("김씨는 %s명"%kim,"이씨는 %s명"%lee)
print("-"*50)

#2."이재영"이라는 이름이 몇 번 반복되나요?
print('2."이재영"이라는 이름이 몇 번 반복되나요?')
temp2 = 0
temp2+=source.count("이재영")
print("%s번"%temp2)
print("-"*50)

#3. 중복을 제거한 이름을 출력하세요.
print("3. 중복을 제거한 이름을 출력하세요.")
s_list = source.split(",")
set_list = set(s_list)
new_list = list(set_list)
print(new_list)
print("-"*50)

#4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
print("4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.")
new_list.sort()
print(new_list)
