import random
import pygame, sys
from pygame.locals import *


def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((500, 650))
    pygame.display.set_caption('RANDOM LUNCH')

    PINK = (255, 103, 129)
    PINK2 = (255, 192, 203)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.Font('NanumPen.ttf', 25)
    font2 = pygame.font.Font('NanumPen.ttf', 55)
    font3 = pygame.font.Font('NanumPen.ttf', 20)
    font4 = pygame.font.Font('NanumPen.ttf',50)

    DISPLAY.fill(WHITE)
    pygame.draw.rect(DISPLAY, PINK, (42, 5, 415, 600), 3)

    MAINTEXT2_SURFACE = font2.render('이 메뉴들을', True, BLACK)
    MAINTEXT2_RECT = MAINTEXT2_SURFACE.get_rect(center=(250, 45))

    MAINTEXT3_SURFACE = font2.render('추천드립니다:)', True, BLACK)
    MAINTEXT3_RECT = MAINTEXT3_SURFACE.get_rect(center=(250,97))

    SUBTEXT_SURFACE = font3.render('마음에 들지 않으세요?', True, PINK)
    SUBTEXT_RECT = SUBTEXT_SURFACE.get_rect(center=(250, 155))

    PUSHTEXT_SURFACE = font3.render('RETRY 버튼을 눌러주세요!', True, PINK)
    PUSHTEXT_RECT = PUSHTEXT_SURFACE.get_rect(center=(250, 177))

    pygame.draw.rect(DISPLAY, PINK2, (75, 230, 350, 40))
    pygame.draw.rect(DISPLAY, PINK,(75, 230, 350, 40),2)
    # pygame.draw.rect(DISPLAY, PINK, (80, 234, 340, 31), 2)
    FIRST_SURFACE = font.render('미트볼이 들어간 로제파스타',True,BLACK)
    FIRST_TEXT = FIRST_SURFACE.get_rect(center=(250,250))
    DISPLAY.blit(FIRST_SURFACE, FIRST_TEXT)

    pygame.draw.rect(DISPLAY, PINK2, (75, 300, 350, 40))
    pygame.draw.rect(DISPLAY, PINK, (75, 300, 350, 40),2)
    SECOND_SURFACE = font.render("강원도 횡성산 꽃등심 600g",True,BLACK)
    SECOND_TEXT = SECOND_SURFACE.get_rect(center=(250,320))
    DISPLAY.blit(SECOND_SURFACE, SECOND_TEXT)

    pygame.draw.rect(DISPLAY, PINK2, (75, 370, 350, 40))
    pygame.draw.rect(DISPLAY, PINK,(75, 370, 350, 40),2)
    THIRD_SURFACE = font.render('고베규 스테이크',True,BLACK)
    THIRD_TEXT = THIRD_SURFACE.get_rect(center=(250,390))
    DISPLAY.blit(THIRD_SURFACE, THIRD_TEXT)

    pygame.draw.rect(DISPLAY, PINK2, (75, 440, 350, 40))
    pygame.draw.rect(DISPLAY, PINK, (75, 440, 350, 40),2)
    FOURTH_SURFACE = font.render('트러플 오일 파스타',True,BLACK)
    FOURTH_TEXT = FOURTH_SURFACE.get_rect(center=(250,460))
    DISPLAY.blit(FOURTH_SURFACE, FOURTH_TEXT)

    pygame.draw.rect(DISPLAY, PINK2, (75, 510, 350, 40))
    pygame.draw.rect(DISPLAY, PINK, (75, 510, 350, 40),2)
    FIFTH_SURFACE = font.render('신라면', True, BLACK)
    FIFTH_TEXT = FIFTH_SURFACE.get_rect(center=(250,530))
    DISPLAY.blit(FIFTH_SURFACE, FIFTH_TEXT)

    RETRY_BOX = pygame.draw.rect(DISPLAY, PINK2, (140, 570, 220, 65))
    RETRY_SURFACE = font4.render('-RETRY-', True, PINK)
    RETRY_TEXT = RETRY_SURFACE.get_rect(center=(250, 605))
    DISPLAY.blit(RETRY_SURFACE, RETRY_TEXT)

    DISPLAY.blit(MAINTEXT2_SURFACE, MAINTEXT2_RECT)
    DISPLAY.blit(MAINTEXT3_SURFACE,MAINTEXT3_RECT)
    DISPLAY.blit(SUBTEXT_SURFACE, SUBTEXT_RECT)
    DISPLAY.blit(PUSHTEXT_SURFACE, PUSHTEXT_RECT)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                if RETRY_BOX.collidepoint(event.pos):
                    pygame.draw.rect(DISPLAY, PINK, RETRY_BOX)
                    pygame.draw.rect(DISPLAY, WHITE, (147, 576, 206, 52))
                    RETRY_SURFACE = font4.render('-RETRY-', True, (50,50,50))

                else:
                    pygame.draw.rect(DISPLAY, PINK2, RETRY_BOX)
                    RETRY_SURFACE = font4.render('-RETRY-', True, PINK)

                DISPLAY.blit(RETRY_SURFACE, RETRY_TEXT)
                pygame.draw.rect(DISPLAY, WHITE, (147, 576, 206, 52), 2)

        pygame.display.update()

if __name__ == '__main__':
    main()