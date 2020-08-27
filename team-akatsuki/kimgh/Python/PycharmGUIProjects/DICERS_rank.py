import pygame, DICERS_rankcal
from pygame.locals import *


def rank():
    pygame.init()
    SURFACE = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('D   I   C   E   R   S')

    BLACK = (0, 0, 0)
    GRAY = (180, 180, 180)
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    PALEBLUE = (120, 120, 240)

    GOLD = (150, 130, 35)
    SILVER = (162, 162, 162)

    DICERSFONT = 'material//NEXONFootballGothicL.ttf'
    MAINFONT = pygame.font.Font(DICERSFONT, 25)
    MIDDLEFONT = pygame.font.Font(DICERSFONT, 50)

    BOX_RICH = (30, 30, 226, 510)
    BOX_RICH_2 = (40, 40, 206, 50)
    BOX_RICH_TITLE = MIDDLEFONT.render('RICH', True, BLACK)
    BOX_RICH_TITLE_RECT = BOX_RICH_TITLE.get_rect(center = [140, 68])
    BOX_RICH_TEXT = MAINFONT.render('포인트 순', True, BLACK)
    BOX_RICH_TEXT_RECT = BOX_RICH_TEXT.get_rect(center = [140, 110])

    BOX_RICH_1ST = MIDDLEFONT.render('1st', True, GOLD)
    BOX_RICH_1ST_RECT = BOX_RICH_1ST.get_rect(center = [140, 160])
    BOX_RICH_1ST_NAME = MAINFONT.render(str(DICERS_rankcal.r_sort()[0]), True, BLACK)
    BOX_RICH_1ST_NAME_RECT = BOX_RICH_1ST_NAME.get_rect(center = [140, 210])
    BOX_RICH_1ST_VALUE = MAINFONT.render((str(DICERS_rankcal.r_sort()[1]) + ' $'), True, BLACK)
    BOX_RICH_1ST_VALUE_RECT = BOX_RICH_1ST_VALUE.get_rect(center = [140, 240])

    BOX_RICH_2ND = MIDDLEFONT.render('2nd', True, SILVER)
    BOX_RICH_2ND_RECT = BOX_RICH_2ND.get_rect(center = [140, 300])
    BOX_RICH_2ND_NAME = MAINFONT.render(str(DICERS_rankcal.r_sort()[2]), True, BLACK)
    BOX_RICH_2ND_NAME_RECT = BOX_RICH_2ND_NAME.get_rect(center = [140, 350])
    BOX_RICH_2ND_VALUE = MAINFONT.render((str(DICERS_rankcal.r_sort()[3]) + ' $'), True, BLACK)
    BOX_RICH_2ND_VALUE_RECT = BOX_RICH_2ND_VALUE.get_rect(center = [140, 380])

    BOX_RICH_3RD = MIDDLEFONT.render('3rd', True, PALEBLUE)
    BOX_RICH_3RD_RECT = BOX_RICH_3RD.get_rect(center = [140, 440])
    BOX_RICH_3RD_NAME = MAINFONT.render(str(DICERS_rankcal.r_sort()[4]), True, BLACK)
    BOX_RICH_3RD_NAME_RECT = BOX_RICH_3RD_NAME.get_rect(center = [140, 490])
    BOX_RICH_3RD_VALUE = MAINFONT.render((str(DICERS_rankcal.r_sort()[5]) + ' $'), True, BLACK)
    BOX_RICH_3RD_VALUE_RECT = BOX_RICH_3RD_VALUE.get_rect(center = [140, 520])

    #

    BOX_CLEV = (286, 30, 226, 510)
    BOX_CLEV_2 = (296, 40, 206, 50)
    BOX_CLEV_TITLE = MIDDLEFONT.render('CLEVER', True, BLACK)
    BOX_CLEV_TITLE_RECT = BOX_CLEV_TITLE.get_rect(center = [396, 68])
    BOX_CLEV_TEXT = MAINFONT.render('포인트 / 라운드 순', True, BLACK)
    BOX_CLEV_TEXT_RECT = BOX_CLEV_TEXT.get_rect(center = [396, 110])

    BOX_CLEV_1ST = MIDDLEFONT.render('1st', True, GOLD)
    BOX_CLEV_1ST_RECT = BOX_CLEV_1ST.get_rect(center=[396, 160])
    BOX_CLEV_1ST_NAME = MAINFONT.render(str(DICERS_rankcal.c_sort()[0]), True, BLACK)
    BOX_CLEV_1ST_NAME_RECT = BOX_CLEV_1ST_NAME.get_rect(center=[396, 210])
    BOX_CLEV_1ST_VALUE = MAINFONT.render((str(int(DICERS_rankcal.c_sort()[1]))), True, BLACK)
    BOX_CLEV_1ST_VALUE_RECT = BOX_CLEV_1ST_VALUE.get_rect(center=[396, 240])

    BOX_CLEV_2ND = MIDDLEFONT.render('2nd', True, SILVER)
    BOX_CLEV_2ND_RECT = BOX_CLEV_2ND.get_rect(center=[396, 300])
    BOX_CLEV_2ND_NAME = MAINFONT.render(str(DICERS_rankcal.c_sort()[2]), True, BLACK)
    BOX_CLEV_2ND_NAME_RECT = BOX_CLEV_2ND_NAME.get_rect(center=[396, 350])
    BOX_CLEV_2ND_VALUE = MAINFONT.render((str(int(DICERS_rankcal.c_sort()[3]))), True, BLACK)
    BOX_CLEV_2ND_VALUE_RECT = BOX_CLEV_2ND_VALUE.get_rect(center=[396, 380])

    BOX_CLEV_3RD = MIDDLEFONT.render('3rd', True, PALEBLUE)
    BOX_CLEV_3RD_RECT = BOX_CLEV_3RD.get_rect(center=[396, 440])
    BOX_CLEV_3RD_NAME = MAINFONT.render(str(DICERS_rankcal.c_sort()[4]), True, BLACK)
    BOX_CLEV_3RD_NAME_RECT = BOX_CLEV_3RD_NAME.get_rect(center=[396, 490])
    BOX_CLEV_3RD_VALUE = MAINFONT.render((str(int(DICERS_rankcal.c_sort()[5]))), True, BLACK)
    BOX_CLEV_3RD_VALUE_RECT = BOX_CLEV_3RD_VALUE.get_rect(center=[396, 520])

    #

    BOX_LONG = (542, 30, 226, 510)
    BOX_LONG_2 = (552, 40, 206, 50)
    BOX_LONG_TITLE = MIDDLEFONT.render('LONG', True, BLACK)
    BOX_LONG_TITLE_RECT = BOX_LONG_TITLE.get_rect(center = [652, 68])
    BOX_LONG_TEXT = MAINFONT.render('라운드 순', True, BLACK)
    BOX_LONG_TEXT_RECT = BOX_LONG_TEXT.get_rect(center = [652, 110])

    BOX_LONG_1ST = MIDDLEFONT.render('1st', True, GOLD)
    BOX_LONG_1ST_RECT = BOX_LONG_1ST.get_rect(center=[652, 160])
    BOX_LONG_1ST_NAME = MAINFONT.render(str(DICERS_rankcal.l_sort()[0]), True, BLACK)
    BOX_LONG_1ST_NAME_RECT = BOX_LONG_1ST_NAME.get_rect(center=[652, 210])
    BOX_LONG_1ST_VALUE = MAINFONT.render((str(DICERS_rankcal.l_sort()[1])), True, BLACK)
    BOX_LONG_1ST_VALUE_RECT = BOX_LONG_1ST_VALUE.get_rect(center=[652, 240])

    BOX_LONG_2ND = MIDDLEFONT.render('2nd', True, SILVER)
    BOX_LONG_2ND_RECT = BOX_LONG_2ND.get_rect(center=[652, 300])
    BOX_LONG_2ND_NAME = MAINFONT.render(str(DICERS_rankcal.l_sort()[2]), True, BLACK)
    BOX_LONG_2ND_NAME_RECT = BOX_LONG_2ND_NAME.get_rect(center=[652, 350])
    BOX_LONG_2ND_VALUE = MAINFONT.render((str(DICERS_rankcal.l_sort()[3])), True, BLACK)
    BOX_LONG_2ND_VALUE_RECT = BOX_LONG_2ND_VALUE.get_rect(center=[652, 380])

    BOX_LONG_3RD = MIDDLEFONT.render('3rd', True, PALEBLUE)
    BOX_LONG_3RD_RECT = BOX_LONG_3RD.get_rect(center=[652, 440])
    BOX_LONG_3RD_NAME = MAINFONT.render(str(DICERS_rankcal.l_sort()[4]), True, BLACK)
    BOX_LONG_3RD_NAME_RECT = BOX_LONG_3RD_NAME.get_rect(center=[652, 490])
    BOX_LONG_3RD_VALUE = MAINFONT.render((str(DICERS_rankcal.l_sort()[5])), True, BLACK)
    BOX_LONG_3RD_VALUE_RECT = BOX_LONG_3RD_VALUE.get_rect(center=[652, 520])

    DICERSFONT = 'material//NEXONFootballGothicL.ttf'
    MAINFONT = pygame.font.Font(DICERSFONT, 25)

    # 종료 텍스트




    # 메인 루프

    while True:
        SURFACE.fill(WHITE)
        # RICH SECTION
        RST_SURFACE = MAINFONT.render('rank reset', True, GRAY)
        RST_RECT = RST_SURFACE.get_rect(center=[143, 565])

        PLAY_SURFACE = MAINFONT.render('play game', True, GRAY)
        PLAY_RECT = PLAY_SURFACE.get_rect(center=[399, 565])

        BTM_SURFACE = MAINFONT.render('back to menu', True, GRAY)
        BTM_RECT = BTM_SURFACE.get_rect(center=[655, 565])
        #
        pygame.draw.rect(SURFACE, BLACK, BOX_RICH, 5)
        pygame.draw.rect(SURFACE, BLACK, BOX_RICH_2, 5)
        SURFACE.blit(BOX_RICH_TITLE, BOX_RICH_TITLE_RECT)
        SURFACE.blit(BOX_RICH_TEXT, BOX_RICH_TEXT_RECT)
        SURFACE.blit(BOX_RICH_1ST, BOX_RICH_1ST_RECT)
        SURFACE.blit(BOX_RICH_1ST_NAME, BOX_RICH_1ST_NAME_RECT)
        SURFACE.blit(BOX_RICH_1ST_VALUE, BOX_RICH_1ST_VALUE_RECT)
        SURFACE.blit(BOX_RICH_2ND, BOX_RICH_2ND_RECT)
        SURFACE.blit(BOX_RICH_2ND_NAME, BOX_RICH_2ND_NAME_RECT)
        SURFACE.blit(BOX_RICH_2ND_VALUE, BOX_RICH_2ND_VALUE_RECT)
        SURFACE.blit(BOX_RICH_3RD, BOX_RICH_3RD_RECT)
        SURFACE.blit(BOX_RICH_3RD_NAME, BOX_RICH_3RD_NAME_RECT)
        SURFACE.blit(BOX_RICH_3RD_VALUE, BOX_RICH_3RD_VALUE_RECT)



        pygame.draw.rect(SURFACE, BLACK, BOX_CLEV, 5)
        pygame.draw.rect(SURFACE, BLACK, BOX_CLEV_2, 5)
        SURFACE.blit(BOX_CLEV_TITLE, BOX_CLEV_TITLE_RECT)
        SURFACE.blit(BOX_CLEV_TEXT, BOX_CLEV_TEXT_RECT)
        SURFACE.blit(BOX_CLEV_1ST, BOX_CLEV_1ST_RECT)
        SURFACE.blit(BOX_CLEV_1ST_NAME, BOX_CLEV_1ST_NAME_RECT)
        SURFACE.blit(BOX_CLEV_1ST_VALUE, BOX_CLEV_1ST_VALUE_RECT)
        SURFACE.blit(BOX_CLEV_2ND, BOX_CLEV_2ND_RECT)
        SURFACE.blit(BOX_CLEV_2ND_NAME, BOX_CLEV_2ND_NAME_RECT)
        SURFACE.blit(BOX_CLEV_2ND_VALUE, BOX_CLEV_2ND_VALUE_RECT)
        SURFACE.blit(BOX_CLEV_3RD, BOX_CLEV_3RD_RECT)
        SURFACE.blit(BOX_CLEV_3RD_NAME, BOX_CLEV_3RD_NAME_RECT)
        SURFACE.blit(BOX_CLEV_3RD_VALUE, BOX_CLEV_3RD_VALUE_RECT)

        pygame.draw.rect(SURFACE, BLACK, BOX_LONG, 5)
        pygame.draw.rect(SURFACE, BLACK, BOX_LONG_2, 5)
        SURFACE.blit(BOX_LONG_TITLE, BOX_LONG_TITLE_RECT)
        SURFACE.blit(BOX_LONG_TEXT, BOX_LONG_TEXT_RECT)
        SURFACE.blit(BOX_LONG_1ST, BOX_LONG_1ST_RECT)
        SURFACE.blit(BOX_LONG_1ST_NAME, BOX_LONG_1ST_NAME_RECT)
        SURFACE.blit(BOX_LONG_1ST_VALUE, BOX_LONG_1ST_VALUE_RECT)
        SURFACE.blit(BOX_LONG_2ND, BOX_LONG_2ND_RECT)
        SURFACE.blit(BOX_LONG_2ND_NAME, BOX_LONG_2ND_NAME_RECT)
        SURFACE.blit(BOX_LONG_2ND_VALUE, BOX_LONG_2ND_VALUE_RECT)
        SURFACE.blit(BOX_LONG_3RD, BOX_LONG_3RD_RECT)
        SURFACE.blit(BOX_LONG_3RD_NAME, BOX_LONG_3RD_NAME_RECT)
        SURFACE.blit(BOX_LONG_3RD_VALUE, BOX_LONG_3RD_VALUE_RECT)

        SURFACE.blit(BTM_SURFACE, BTM_RECT)
        SURFACE.blit(RST_SURFACE, RST_RECT)
        SURFACE.blit(PLAY_SURFACE, PLAY_RECT)




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RST_RECT.collidepoint(event.pos):
                    with open('ranks/rich.txt', 'w', encoding='utf-8') as rsr:
                        rsr.write('default1,1,default2,1,default3,1,')
                    with open('ranks/clever.txt', 'w', encoding='utf-8') as rsc:
                        rsc.write('default1,1,default2,1,default3,1,')
                    with open('ranks/long.txt', 'w', encoding='utf-8') as rsl:
                        rsl.write('default1,1,default2,1,default3,1,')
                    rank()

                if PLAY_RECT.collidepoint(event.pos):
                    import DICERS_game
                    DICERS_game.game()


                if BTM_RECT.collidepoint(event.pos):
                    import DICERS_main
                    DICERS_main.main()


            if event.type == pygame.MOUSEMOTION:

                if RST_RECT.collidepoint(event.pos):
                    RST_SURFACE = MAINFONT.render('$ rank reset $', True, RED)
                    RST_RECT = RST_SURFACE.get_rect(center=[143, 565])
                    SURFACE.blit(RST_SURFACE, RST_RECT)

                if PLAY_RECT.collidepoint(event.pos):
                    PLAY_SURFACE = MAINFONT.render('$ play game $', True, RED)
                    PLAY_RECT = PLAY_SURFACE.get_rect(center=[399, 565])
                    SURFACE.blit(PLAY_SURFACE, PLAY_RECT)

                if BTM_RECT.collidepoint(event.pos):
                    BTM_SURFACE = MAINFONT.render('$ back to menu $', True, RED)
                    BTM_RECT = BTM_SURFACE.get_rect(center=[655, 565])
                    SURFACE.blit(BTM_SURFACE, BTM_RECT)
            pygame.display.update()