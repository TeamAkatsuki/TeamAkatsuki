import pygame, sys
from pygame.locals import *


def main():
    pygame.init()

    # SURFACE 객체
    SURFACE = pygame.display.set_mode((800, 600), 0, 0, 32)
    pygame.display.set_caption('D   I   C   E   R   S')

    # 변수 설정
    GRAY = (180, 180, 180)
    WHITE = (250, 250, 250)
    RED = (200, 0, 0)
    DICERSFONT = 'material\\NEXONFootballGothicL.ttf'


    # 메인프레임
    UPPERBOX = (30, 30, 740, 300)
    LOWERBOX = (30, 400, 740, 150)

    # 폰트
    TITLEFONT = pygame.font.Font(DICERSFONT, 75)
    MAINFONT = pygame.font.Font(DICERSFONT, 25)

    # 타이틀 텍스트
    TITLE_SURFACE = TITLEFONT.render('D    I    C    E    R    $', True, RED)
    TITLE_RECT = TITLE_SURFACE.get_rect(topleft = [80, 150])


    # 시작 텍스트
    START_SURFACE = MAINFONT.render('start', True, GRAY)
    START_RECT = START_SURFACE.get_rect(center=[400, 430])

    # 랭크 텍스트

    RANK_SURFACE = MAINFONT.render('ranking', True, GRAY)
    RANK_RECT = RANK_SURFACE.get_rect(center=[400, 475])

    # 종료 텍스트
    EXIT_SURFACE = MAINFONT.render('exit', True, GRAY)
    EXIT_RECT = EXIT_SURFACE.get_rect(center=[400, 520])


    # 메인 루프

    while True:
        SURFACE.fill(WHITE)
        pygame.draw.rect(SURFACE, GRAY, UPPERBOX, 5)
        pygame.draw.rect(SURFACE, GRAY, LOWERBOX, 5)

        SURFACE.blit(START_SURFACE, START_RECT)

        SURFACE.blit(TITLE_SURFACE, TITLE_RECT)

        SURFACE.blit(RANK_SURFACE, RANK_RECT)
        SURFACE.blit(EXIT_SURFACE, EXIT_RECT)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:

                if START_RECT.collidepoint(event.pos):
                    START_SURFACE = MAINFONT.render('$ start $', True, RED)
                    START_RECT = START_SURFACE.get_rect(center = [400, 430])
                    SURFACE.blit(START_SURFACE, START_RECT)

                elif RANK_RECT.collidepoint(event.pos):
                    RANK_SURFACE = MAINFONT.render('$ ranking $', True, RED)
                    RANK_RECT = RANK_SURFACE.get_rect(center = [400, 475])
                    SURFACE.blit(RANK_SURFACE, RANK_RECT)

                elif EXIT_RECT.collidepoint(event.pos):
                    EXIT_SURFACE = MAINFONT.render('$ exit $', True, RED)
                    EXIT_RECT = EXIT_SURFACE.get_rect(center = [400, 520])
                    SURFACE.blit(EXIT_SURFACE, EXIT_RECT)

                else:
                    main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_RECT.collidepoint(event.pos):
                    import DICERS_rule
                    DICERS_rule.game_1()
                if RANK_RECT.collidepoint(event.pos):
                    import DICERS_rank
                    DICERS_rank.rank()
                if EXIT_RECT.collidepoint(event.pos):
                    pygame.quit()
                else:
                    continue

        pygame.display.update()


if __name__ == '__main__':
    main()
