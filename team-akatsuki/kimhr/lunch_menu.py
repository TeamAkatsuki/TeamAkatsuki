import random

menus = ['예가돈까스', '백제 김치찌개', 'KFC', '왕돈까스 왕냉면', '할매순대국', '홍콩반점', 'EGG DROP', 'SUBWAY', '아비꼬', '국수나무', '꽝(음료수쏘기)']
prices = [10500, 7000, 9000, 7000, 6000, 5000, 5000, 5000, 9000, 7000, 7000]



i = random.randint(0, len(menus) - 1)
print('추천 메뉴:', menus[i])
print('메뉴 가격:', prices[i])