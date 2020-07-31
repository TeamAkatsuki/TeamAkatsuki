# 1. 스트링을 페어리스트로 만드는 함수를 먼저 만든다. 본체를 먼저 만들고 통로를 만든다.

a = 'a,1,b,1,a,3,b,4,c,5,zxc,312'  # 2. 임의의 str을 부여한다, 파일 연결 전.


def pairwise(param):  # 3. pairwise는 str를 받아서 pair.list로 만드는 함수 (arg - str, return - 2차원 리스트)
    param = param.split(",")  # 4. 스트링에서 쉼표를 기준으로 나눈다. param을 리스트로 만든다.
    pair_list = []  # 5. 페어들을 저장하는 2차원 리스트를 준비한다.
    for pi in range(len(param)):  # 6. param의 len으로 인덱스를 활용한다
        temp_pair = []  # 7. 페어들을 반복 append 직전에 초기화한다.
        if pi % 2 == 0:  # 8. 짝수 번째 자리일 때, (인덱스)
            temp_pair.append(param[pi])  # 9. 임시리스트에 짝수 번째 인덱스 : 상품명 추가
            temp_pair.append(int(param[pi + 1]))  # 10. 임시리스트에 짝수 번째 바로 다음 요소 정수형 수량을 추가
            pair_list.append(temp_pair)  # 11. 진짜 리스트에 2개 씩 묶인 temp_pair 리스트를 append 한다.
    return pair_list  # 12. pairwise 함수 완성 (arg - str, return - 2차원 리스트)


def sumwise(param):  # 13. 중복을 고려해서 합산하는 함수를 만든다. (arg - 2차원 리스트, return - 합산 완료 리스트)
    sum_list = []  # 14. 최종 결과를 담을 리스트를 만든다.
    for pi in param:  # 15. 2차원 리스트에서 요소 하나를 뽑는다.
        dbcheck = False  # 16. 중복 판독기를 설정한다.
        dbpos = None  # 17. 중복 발생 위치를 설정한다.
        for pj in range(len(sum_list)):  # 18. sum_list의 인덱스를 돈다
            if pi[0] == sum_list[pj][0]:  # 19. 중복이 발생하면
                dbcheck = True  # 20. 중복 판독기 on
                dbpos = pj  # 21. 중복 발생 위치 인덱스 저장
        if dbcheck:
            sum_list[pj][1] = pi[1] + sum_list[pj][1]
        else:
            sum_list.append(pi)
    return sum_list

print(sumwise(pairwise(a)))



sumwise(pairwise(a))