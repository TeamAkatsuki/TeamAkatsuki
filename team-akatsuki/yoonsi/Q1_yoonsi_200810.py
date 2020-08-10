name = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
namelist = name.split(",")

# 1
print("1. 김씨와 이씨는 각각 명 몇인가요?")
print('김씨는?', name.count('김'),'명')
print('이씨는?', name.count('이'),'명')
print()
# 2
print("2. \"이재영\"이라는 이름이 몇 번 반복되나요?")
print('이재영은', name.count('이재영'), '번 반복됨')
print()
# 3
print("3. 중복을 제거한 이름을 출력하세요.")
no = set(namelist)
print(no)
print()
# 4
print("4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.")
yes = sorted(no)
print(yes)

