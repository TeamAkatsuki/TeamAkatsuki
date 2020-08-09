# 김씨와 이씨는 각각 몇명인가요?
# "이재영"이라는 이름이 몇 번 반복되나요?
#  중복을 제거한 이름을 출력하세요.
#  중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

source = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

kim = source.count('김')
lee = source.count('이')
print(kim,lee)

jy = 0
s = source.split(",")
for i in range(len(s)):
    if s[i] == "이재영":
        jy = jy + 1
print(jy)

tal_ju = []
for i in range(len(s)):
    del_jy = False
    for j in range(len(tal_ju)):
        if s[i] == tal_ju[j]:
            del_jy = True
            break
    if del_jy:
        pass
    else:
        tal_ju.append(s[i])

print(tal_ju)

tal_ju.sort()
print(tal_ju)




