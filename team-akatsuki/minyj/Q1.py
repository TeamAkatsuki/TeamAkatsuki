name = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

kim = 0
lee = 0
#Q.1
kim+=name.count("김")
lee+=name.count("이")
print("김 %s명"%kim,"이 %s명"%lee)
#Q.2
ljy = 0
ljy+=name.count("이재영")
print("%s번"%ljy)
#Q.3
del_list =name.split(",")
list_1 = set(del_list)
list_2 = list(list_1)
print(list_2)
#Q.4
list_2.sort()
print(list_2)

