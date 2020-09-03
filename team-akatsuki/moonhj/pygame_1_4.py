import random
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((500, 650))
pygame.display.set_caption('RANDOM LUNCH')

PINK = (255, 103, 129)
PINK2 = (255, 192, 203)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR_1 = [(255, 103, 129),(255, 103, 129),(255, 103, 129),
           (255, 103, 129),(255, 103, 129)]
COLOR_FONT = (0,0,0)


font = pygame.font.Font('NanumPen.ttf', 25)
font2 = pygame.font.Font('NanumPen.ttf', 60)
font3 = pygame.font.Font('NanumPen.ttf', 22)

select_m = ['한식', '일식', '중식', '양식', '기타']
k_food = ['비빔밥', '제육덮밥', '김치찌개', '된장찌개', '냉면', '돼지불백', '칼국수', '수제비', '부대찌개', '고등어조림', '보쌈',
          '뼈해장국', '순대국']
j_food = ['초밥', '우동', '스끼야끼', '냉모밀', '냉우동', '도미조림', '규동', '가츠동', '오니기리', '라멘', '오야꼬동']
c_food = ['짜장면', '짬뽕', '탕수육', '마파두부', '깐풍기', '라조기', '마라탕', '마라샹궈', '고추잡채', '볶음밥', '양장피', '텐동']
w_food = ['오믈렛', '오므라이스', '스테이크', '햄버거', '치킨커틀릿', '포크커틀릿', '까르보나라', '비프스튜', '토마토파스타', '바베큐폭립']
etc_food = ['순대', '떡볶이', '김밥', '라면', '쌀국수', '분짜', '인도커리', '팟타이', '슈바인학센', '다이어트는 어때...?', '삼각김밥',
            '편의점 도시락']


def RandLunch(i):
    ko = random.sample(k_food, 5)
    ja = random.sample(j_food, 5)
    ch = random.sample(c_food, 5)
    we = random.sample(w_food, 5)
    etc = random.sample(etc_food, 5)

    if i == 1:
        return ko
    elif i == 2:
        return ja
    elif i == 3:
        return ch
    elif i == 4:
        return we
    elif i == 5:
        return etc

def ReTry():
    while True:
        retry = input('******************************************************************\n'
                      '다시 뽑으시겠습니까? 예/아니오 : ')
        if '예' == retry:
            RandLunch()
        elif '아니오' == retry:
            print("프로그램을 종료합니다.")
            break
        else:
            print('잘못 입력하셨습니다. 다시 입력해 주세요')

RandLunch(0)
# ReTry()
def sub():
    global KOREAN_BOX, KOREAN_TEXT, JAPANESE_BOX, JAPANESE_TEXT, CHINESE_BOX, CHINESE_TEXT
    global WESTERN_BOX, WESTERN_TEXT, ETC_BOX, ETC_TEXT, RANDOM_SURFACE, RANDOM_RECT
    global MAINTEXT_SURFACE, MAINTEXT_RECT, SUBTEXT_SURFACE, SUBTEXT_RECT, PUSHTEXT_SURFACE, PUSHTEXT_RECT
    global KOREAN_SURFACE, JAPANESE_SURFACE, CHINESE_SURFACE, WESTERN_SURFACE, ETC_SURFACE
    global KOREAN_RECT

    RANDOM_SURFACE = font.render('Random', True, PINK)
    RANDOM_RECT = RANDOM_SURFACE.get_rect(center=(100, 55))

    MAINTEXT_SURFACE = font2.render('점심 메뉴 뽑기!', True, BLACK)
    MAINTEXT_RECT = MAINTEXT_SURFACE.get_rect(center=(250, 90))

    SUBTEXT_SURFACE = font3.render('아래의 메뉴 중', True, BLACK)
    SUBTEXT_RECT = SUBTEXT_SURFACE.get_rect(center=(250, 145))

    PUSHTEXT_SURFACE = font3.render('하나를 눌러주세요', True, BLACK)
    PUSHTEXT_RECT = PUSHTEXT_SURFACE.get_rect(center=(250, 175))

    KOREAN_SURFACE = font.render('한식', True, WHITE)
    KOREAN_TEXT = KOREAN_SURFACE.get_rect(center=(250, 250))

    JAPANESE_SURFACE = font.render("일식", True, WHITE)
    JAPANESE_TEXT = JAPANESE_SURFACE.get_rect(center=(250, 320))

    CHINESE_SURFACE = font.render('중식', True, WHITE)
    CHINESE_TEXT = CHINESE_SURFACE.get_rect(center=(250, 390))

    WESTERN_SURFACE = font.render('양식', True, WHITE)
    WESTERN_TEXT = WESTERN_SURFACE.get_rect(center=(250, 460))

    ETC_SURFACE = font.render('기타', True, WHITE)
    ETC_TEXT = ETC_SURFACE.get_rect(center=(250, 530))


sub()

def main():
    global KOREAN_BOX, KOREAN_TEXT, JAPANESE_BOX, JAPANESE_TEXT, CHINESE_BOX, CHINESE_TEXT
    global WESTERN_BOX, WESTERN_TEXT, ETC_BOX, ETC_TEXT, RANDOM_SURFACE, RANDOM_RECT
    global MAINTEXT_SURFACE, MAINTEXT_RECT, SUBTEXT_SURFACE, SUBTEXT_RECT, PUSHTEXT_SURFACE, PUSHTEXT_RECT
    global KOREAN_SURFACE, JAPANESE_SURFACE, CHINESE_SURFACE, WESTERN_SURFACE, ETC_SURFACE
    global KOREAN_RECT

    while True:
        events = pygame.event.get()
        DISPLAY.fill(WHITE)
        KOREAN_BOX = pygame.draw.rect(DISPLAY, COLOR_1[0], (75, 230, 350, 40))
        JAPANESE_BOX = pygame.draw.rect(DISPLAY, COLOR_1[1], (75, 300, 350, 40))
        CHINESE_BOX = pygame.draw.rect(DISPLAY, COLOR_1[2], (75, 370, 350, 40))
        WESTERN_BOX = pygame.draw.rect(DISPLAY, COLOR_1[3], (75, 440, 350, 40))
        ETC_BOX = pygame.draw.rect(DISPLAY, COLOR_1[4], (75, 510, 350, 40))

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                if KOREAN_BOX.collidepoint(event.pos):
                    COLOR_1[0] = PINK2
                    KOREAN_SURFACE = font.render('한식', True, BLACK)

                else:
                    COLOR_1[0] = PINK
                    KOREAN_SURFACE = font.render('한식', True, WHITE)


                if JAPANESE_BOX.collidepoint(event.pos):
                    COLOR_1[1] = PINK2
                    JAPANESE_SURFACE = font.render('일식', True, BLACK)
                else:
                    COLOR_1[1] = PINK
                    JAPANESE_SURFACE = font.render('일식', True, WHITE)

                if CHINESE_BOX.collidepoint(event.pos):
                    COLOR_1[2] = PINK2
                    CHINESE_SURFACE = font.render('중식', True, BLACK)
                else:
                    COLOR_1[2] = PINK
                    CHINESE_SURFACE = font.render('중식', True, WHITE)

                if WESTERN_BOX.collidepoint(event.pos):
                    COLOR_1[3] = PINK2
                    WESTERN_SURFACE = font.render('양식', True, BLACK)
                else:
                    COLOR_1[3] = PINK
                    WESTERN_SURFACE = font.render('양식', True, WHITE)

                if ETC_BOX.collidepoint(event.pos):
                    COLOR_1[4] = PINK2
                    ETC_SURFACE = font.render('기타', True, BLACK)
                else:
                    COLOR_1[4] = PINK
                    ETC_SURFACE = font.render('기타', True, WHITE)


            if event.type == pygame.MOUSEBUTTONUP:

                if KOREAN_BOX.collidepoint(event.pos): #함수로 빼놓을 것들
                    save_list = RandLunch(1)
                    KOREAN_SURFACE = font.render('%s' % save_list[0], True, BLACK)
                    KOREAN_TEXT = KOREAN_SURFACE.get_rect(center=(250, 250))

                    JAPANESE_SURFACE = font.render("%s" % save_list[1], True, BLACK)
                    JAPANESE_TEXT = JAPANESE_SURFACE.get_rect(center=(250, 320))

                    CHINESE_SURFACE = font.render('%s' % save_list[2], True, BLACK)
                    CHINESE_TEXT = CHINESE_SURFACE.get_rect(center=(250, 390))

                    WESTERN_SURFACE = font.render('%s' % save_list[3], True, BLACK)
                    WESTERN_TEXT = WESTERN_SURFACE.get_rect(center=(250, 460))

                    ETC_SURFACE = font.render('%s' % save_list[4], True, BLACK)
                    ETC_TEXT = ETC_SURFACE.get_rect(center=(250, 530))


                elif JAPANESE_BOX.collidepoint(event.pos):
                    save_list = RandLunch(2)
                    KOREAN_SURFACE = font.render('%s' % save_list[0], True,BLACK)
                    KOREAN_TEXT = KOREAN_SURFACE.get_rect(center=(250, 250))

                    JAPANESE_SURFACE = font.render("%s" % save_list[1], True, BLACK)
                    JAPANESE_TEXT = JAPANESE_SURFACE.get_rect(center=(250, 320))

                    CHINESE_SURFACE = font.render('%s' % save_list[2], True, BLACK)
                    CHINESE_TEXT = CHINESE_SURFACE.get_rect(center=(250, 390))

                    WESTERN_SURFACE = font.render('%s' % save_list[3], True, BLACK)
                    WESTERN_TEXT = WESTERN_SURFACE.get_rect(center=(250, 460))

                    ETC_SURFACE = font.render('%s' % save_list[4], True, WHITE)
                    ETC_TEXT = ETC_SURFACE.get_rect(center=(250, 530))

                elif CHINESE_BOX.collidepoint(event.pos):
                    save_list = RandLunch(3)
                    KOREAN_SURFACE = font.render('%s' % save_list[0], True, BLACK)
                    KOREAN_TEXT = KOREAN_SURFACE.get_rect(center=(250, 250))

                    JAPANESE_SURFACE = font.render("%s" % save_list[1], True, BLACK)
                    JAPANESE_TEXT = JAPANESE_SURFACE.get_rect(center=(250, 320))

                    CHINESE_SURFACE = font.render('%s' % save_list[2], True, BLACK)
                    CHINESE_TEXT = CHINESE_SURFACE.get_rect(center=(250, 390))

                    WESTERN_SURFACE = font.render('%s' % save_list[3], True, BLACK)
                    WESTERN_TEXT = WESTERN_SURFACE.get_rect(center=(250, 460))

                    ETC_SURFACE = font.render('%s' % save_list[4], True,BLACK)
                    ETC_TEXT = ETC_SURFACE.get_rect(center=(250, 530))

                elif WESTERN_BOX.collidepoint(event.pos):
                    save_list = RandLunch(4)
                    KOREAN_SURFACE = font.render('%s' % save_list[0], True, BLACK)
                    KOREAN_TEXT = KOREAN_SURFACE.get_rect(center=(250, 250))

                    JAPANESE_SURFACE = font.render("%s" % save_list[1], True, BLACK)
                    JAPANESE_TEXT = JAPANESE_SURFACE.get_rect(center=(250, 320))

                    CHINESE_SURFACE = font.render('%s' % save_list[2], True, BLACK)
                    CHINESE_TEXT = CHINESE_SURFACE.get_rect(center=(250, 390))

                    WESTERN_SURFACE = font.render('%s' % save_list[3], True, BLACK)
                    WESTERN_TEXT = WESTERN_SURFACE.get_rect(center=(250, 460))

                    ETC_SURFACE = font.render('%s' % save_list[4], True, BLACK)
                    ETC_TEXT = ETC_SURFACE.get_rect(center=(250, 530))

                elif ETC_BOX.collidepoint(event.pos):
                    save_list = RandLunch(5)
                    KOREAN_SURFACE = font.render('%s' % save_list[0], True, BLACK)
                    KOREAN_TEXT = KOREAN_SURFACE.get_rect(center=(250, 250))

                    JAPANESE_SURFACE = font.render("%s" % save_list[1], True, BLACK)
                    JAPANESE_TEXT = JAPANESE_SURFACE.get_rect(center=(250, 320))

                    CHINESE_SURFACE = font.render('%s' % save_list[2], True, BLACK)
                    CHINESE_TEXT = CHINESE_SURFACE.get_rect(center=(250, 390))

                    WESTERN_SURFACE = font.render('%s' % save_list[3], True, BLACK)
                    WESTERN_TEXT = WESTERN_SURFACE.get_rect(center=(250, 460))

                    ETC_SURFACE = font.render('%s' % save_list[4], True, BLACK)
                    ETC_TEXT = ETC_SURFACE.get_rect(center=(250, 530))

        DISPLAY.blit(KOREAN_SURFACE, KOREAN_TEXT)
        DISPLAY.blit(JAPANESE_SURFACE, JAPANESE_TEXT)
        DISPLAY.blit(CHINESE_SURFACE, CHINESE_TEXT)
        DISPLAY.blit(WESTERN_SURFACE, WESTERN_TEXT)
        DISPLAY.blit(ETC_SURFACE, ETC_TEXT)

        DISPLAY.blit(RANDOM_SURFACE, RANDOM_RECT)  # 메인 화면 텍스트(Random)
        DISPLAY.blit(MAINTEXT_SURFACE, MAINTEXT_RECT)  # 메인 화면 텍스트(점심 메뉴 뽑기!)
        DISPLAY.blit(SUBTEXT_SURFACE, SUBTEXT_RECT)  # 메인 화면 텍스트(아래의 메뉴 중)
        DISPLAY.blit(PUSHTEXT_SURFACE, PUSHTEXT_RECT)  # 메인 화면 텍스트(하나를 눌러주세요)
        pygame.draw.rect(DISPLAY, PINK, (42, 5, 415, 600), 3)  # 메인화면 프레임

        pygame.display.update()

if __name__ == '__main__':
    main()