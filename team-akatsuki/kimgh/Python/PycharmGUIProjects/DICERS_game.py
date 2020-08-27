import pygame
from random import randint
from pygame.locals import *

def game():
    global DICERS_main
    pygame.init()

    SURFACE = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('D   I   C   E   R   S')

    BLACK = (50, 50, 50)
    WHITE = (255, 255, 255)
    PALEBLUE = (100, 100, 200)
    BLUE = (0, 0, 255)
    PALERED = (200, 100, 100)
    RED = (200, 0, 0)
    GOLD = (150, 130, 35)
    GRAY = (180, 180, 180)


    point_status = 100  # start point
    point_bet = 0 # bet pot
    round = 1 # start round

    DICERSFONT = 'material//NEXONFootballGothicL.ttf'
    MAINFONT = pygame.font.Font(DICERSFONT, 25)
    MIDDLEFONT = pygame.font.Font(DICERSFONT, 50)
    BIGFONT = pygame.font.Font(DICERSFONT, 75)





    while True: # MAIN GAME LOOP START

        SURFACE.fill(WHITE)


        #
        SLOTBOX = (30, 80, 535, 330)
        DICEBOX1 = (50, 100, 145, 145)
        DICEBOX2 = (225, 100, 145, 145)
        DICEBOX3 = (400, 100, 145, 145)
        SLOTINBOX = (50, 265, 495, 125)
        BPBOX = (30, 425, 535, 90)

        BTNBOX = (585, 80, 185, 435)



        pygame.draw.rect(SURFACE, GRAY, SLOTBOX, 3)
        pygame.draw.rect(SURFACE, GRAY, DICEBOX1, 3)
        pygame.draw.rect(SURFACE, GRAY, DICEBOX2, 3)
        pygame.draw.rect(SURFACE, GRAY, DICEBOX3, 3)
        pygame.draw.rect(SURFACE, GRAY, SLOTINBOX, 3)
        pygame.draw.rect(SURFACE, GRAY, BPBOX, 3)
        pygame.draw.rect(SURFACE, GRAY, BTNBOX, 3)

        POINT_SURFACE = MAINFONT.render("보유 포인트 - " + str(point_status) + ' $', True, PALEBLUE)
        POINT_RECT = POINT_SURFACE.get_rect(topleft = [50, 440])

        BET_SURFACE = MAINFONT.render("베팅 포인트 - " + str(point_bet) + ' $', True, PALERED)
        BET_RECT = BET_SURFACE.get_rect(topleft = [50, 480])

        #
        CLEARBOX = (600, 100, 155, 50)
        CLEAR_SURFACE = MAINFONT.render("C L E A R", True, WHITE)
        CLEAR_RECT = CLEAR_SURFACE.get_rect(center = [677, 127])
        pygame.draw.rect(SURFACE, BLACK, CLEARBOX)
        SURFACE.blit(CLEAR_SURFACE, CLEAR_RECT)

        ALLINBOX = (600, 160, 155, 50)
        ALLIN_SURFACE = MAINFONT.render("A L L - I N", True, WHITE)
        ALLIN_RECT = ALLIN_SURFACE.get_rect(center = [677, 187])
        pygame.draw.rect(SURFACE, BLACK, ALLINBOX)
        SURFACE.blit(ALLIN_SURFACE, ALLIN_RECT)

        #

        BETPLUS20BOX = (600, 220, 75, 50)
        pygame.draw.rect(SURFACE, PALEBLUE, BETPLUS20BOX)
        BETPLUS20_SURFACE = MAINFONT.render("+20", True, WHITE)
        BETPLUS20_RECT = BETPLUS20_SURFACE.get_rect(center = [635, 247])
        SURFACE.blit(BETPLUS20_SURFACE, BETPLUS20_RECT)

        BETPLUS5BOX = (600, 275, 75, 50)
        BETPLUS5_SURFACE = MAINFONT.render("+5", True, WHITE)
        BETPLUS5_RECT = BETPLUS5_SURFACE.get_rect(center = [635, 302])
        pygame.draw.rect(SURFACE, PALEBLUE, BETPLUS5BOX)
        SURFACE.blit(BETPLUS5_SURFACE, BETPLUS5_RECT)

        BETPLUS1BOX = (600, 330, 75, 50)
        BETPLUS1_SURFACE = MAINFONT.render("+1", True, WHITE)
        BETPLUS1_RECT = BETPLUS1_SURFACE.get_rect(center = [635, 357])
        pygame.draw.rect(SURFACE, PALEBLUE, BETPLUS1BOX)
        SURFACE.blit(BETPLUS1_SURFACE, BETPLUS1_RECT)



        #

        BETMINUS20BOX = (680, 220, 75, 50)
        BETMINUS20_SURFACE = MAINFONT.render("-20", True, WHITE)
        BETMINUS20_RECT = BETMINUS20_SURFACE.get_rect(center=[715, 247])
        pygame.draw.rect(SURFACE, PALERED, BETMINUS20BOX)
        SURFACE.blit(BETMINUS20_SURFACE, BETMINUS20_RECT)

        BETMINUS5BOX = (680, 275, 75, 50)
        BETMINUS5_SURFACE = MAINFONT.render("-5", True, WHITE)
        BETMINUS5_RECT = BETMINUS5_SURFACE.get_rect(center = [715, 302])
        pygame.draw.rect(SURFACE, PALERED, BETMINUS5BOX)
        SURFACE.blit(BETMINUS5_SURFACE, BETMINUS5_RECT)

        BETMINUS1BOX = (680, 330, 75, 50)
        BETMINUS1_SURFACE = MAINFONT.render("-1", True, WHITE)
        BETMINUS1_RECT = BETMINUS1_SURFACE.get_rect(center=[715, 357])
        pygame.draw.rect(SURFACE, PALERED, BETMINUS1BOX)
        SURFACE.blit(BETMINUS1_SURFACE, BETMINUS1_RECT)

        #

        ROLL_BOX = (600, 390, 155, 105)
        ROLL_SURFACE = MIDDLEFONT.render("ROLL", True, GOLD)
        ROLL_RECT = ROLL_SURFACE.get_rect(center=[677, 445])
        pygame.draw.rect(SURFACE, BLACK, ROLL_BOX)
        SURFACE.blit(ROLL_SURFACE, ROLL_RECT)
        #
        ROUND_SURFACE = MIDDLEFONT.render("ROUND {}".format(round), True, GOLD)
        ROUND_RECT = ROUND_SURFACE.get_rect(topleft=[27, 30])
        #
        YMBF_SURFACE = MIDDLEFONT.render("베팅 먼저 하세요!", True, PALERED, BLACK)
        YMBF_RECT = YMBF_SURFACE.get_rect(center = [400, 300])
        #
        RETRY_SURFACE = MAINFONT.render("RETRY(GO TO MAIN)", True, GRAY)
        RETRY_RECT = RETRY_SURFACE.get_rect(center=[165, 550])

        SAVE_SURFACE = MAINFONT.render("SAVE TO RANK", True, GRAY)
        SAVE_RECT = SAVE_SURFACE.get_rect(center=[665, 550])

        #

        SURFACE.blit(RETRY_SURFACE, RETRY_RECT)
        SURFACE.blit(ROLL_SURFACE, ROLL_RECT)
        SURFACE.blit(POINT_SURFACE, POINT_RECT)
        SURFACE.blit(BET_SURFACE, BET_RECT)
        SURFACE.blit(ROUND_SURFACE, ROUND_RECT)
        SURFACE.blit(SAVE_SURFACE, SAVE_RECT)

        # ANIME

        def anime(pi):

            colors = (PALERED, PALEBLUE, GOLD, GRAY)

            DICE1NUM = BIGFONT.render(str(randint(1, 6)), True, colors[randint(0,3)])
            DICE1_RECT = DICE1NUM.get_rect(center=[125, 175])
            SURFACE.blit(DICE1NUM, DICE1_RECT)
            pygame.time.delay(pi)

            DICE2NUM = BIGFONT.render(str(randint(1, 6)), True, colors[randint(0,3)])
            DICE2_RECT = DICE2NUM.get_rect(center=[300, 175])
            SURFACE.blit(DICE2NUM, DICE2_RECT)
            pygame.time.delay(pi)

            DICE3NUM = BIGFONT.render(str(randint(1, 6)), True, colors[randint(0,3)])
            DICE3_RECT = DICE3NUM.get_rect(center=[475, 175])
            SURFACE.blit(DICE3NUM, DICE3_RECT)
            pygame.display.update()
            pygame.time.delay(pi)
        ANIMESPEED = 20
        anime(ANIMESPEED)

        # GET EVENTS

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if BETPLUS20_RECT.collidepoint(event.pos):
                    if point_status >= 20:
                        point_bet += 20
                        point_status -= 20

                if BETPLUS5_RECT.collidepoint(event.pos):
                    if point_status >= 5:
                        point_bet += 5
                        point_status -= 5

                if BETPLUS1_RECT.collidepoint(event.pos):
                    if point_status > 0:
                        point_bet += 1
                        point_status -= 1

                if ALLIN_RECT.collidepoint(event.pos):
                    if point_status > 0:
                        point_bet += point_status
                        point_status = 0

                if BETMINUS20_RECT.collidepoint(event.pos):
                    if point_bet >= 20:
                        point_bet -= 20
                        point_status += 20

                if BETMINUS5_RECT.collidepoint(event.pos):
                    if point_bet >= 5:
                        point_bet -= 5
                        point_status += 5

                if BETMINUS1_RECT.collidepoint(event.pos):
                    if point_bet > 0:
                        point_bet -= 1
                        point_status += 1

                if CLEAR_RECT.collidepoint(event.pos):
                    if point_bet > 0:
                        point_status += point_bet
                        point_bet = 0

                if RETRY_RECT.collidepoint(event.pos):
                    import DICERS_main
                    DICERS_main.main()

                if ROLL_RECT.collidepoint(event.pos):
                    result_midleft = [60, 330]

                    if point_bet != 0:
                        round += 1

                        temp_lucklist = []
                        for i in range(3):
                            temp_lucklist.append(randint(1,6))


                        DICE1NUM = BIGFONT.render(str(temp_lucklist[0]), True, WHITE)
                        pygame.draw.rect(SURFACE, BLACK, DICEBOX1)
                        DICE1_RECT = DICE1NUM.get_rect(center = [125,175])
                        SURFACE.blit(DICE1NUM, DICE1_RECT)
                        pygame.display.update()
                        pygame.time.delay(650)

                        DICE2NUM = BIGFONT.render(str(temp_lucklist[1]), True, WHITE)
                        pygame.draw.rect(SURFACE, BLACK, DICEBOX2)
                        DICE2_RECT = DICE2NUM.get_rect(center = [300, 175])
                        SURFACE.blit(DICE2NUM, DICE2_RECT)
                        pygame.display.update()
                        pygame.time.delay(800)

                        DICE3NUM = BIGFONT.render(str(temp_lucklist[2]), True, WHITE)
                        pygame.draw.rect(SURFACE, BLACK, DICEBOX3)
                        DICE3_RECT = DICE3NUM.get_rect(center=[475, 175])
                        SURFACE.blit(DICE3NUM, DICE3_RECT)
                        pygame.display.update()
                        pygame.time.delay(600)

                        #

                        luckset = set(temp_lucklist)
                        luck_list = list(luckset)


                        if len(luck_list) == 1:

                            if luck_list[0] == 1: #111
                                point_status += point_bet * 10

                                RESULT_111_SURFACE = MAINFONT.render('1 1 1 (+10배) (+' + str(10 * point_bet) +'$)', True, GOLD)
                                RESULT_111_RECT = RESULT_111_SURFACE.get_rect(midleft = result_midleft)
                                SURFACE.blit(RESULT_111_SURFACE, RESULT_111_RECT)

                                point_bet = 0

                                SURFACE.blit(POINT_SURFACE, POINT_RECT)
                                SURFACE.blit(BET_SURFACE, BET_RECT)
                                pygame.display.update()
                                pygame.time.delay(1500)



                            else: # 222, 333, 444, 555, 666
                                point_status += point_bet * 5

                                RESULT_TRIPLE_SURFACE = MAINFONT.render('트리플 (+5배) (+' + str(5 * point_bet) +'$)', True, BLACK, GRAY)
                                RESULT_TRIPLE_RECT = RESULT_TRIPLE_SURFACE.get_rect(midleft = result_midleft)
                                SURFACE.blit(RESULT_TRIPLE_SURFACE, RESULT_TRIPLE_RECT)

                                point_bet = 0

                                SURFACE.blit(POINT_SURFACE, POINT_RECT)
                                SURFACE.blit(BET_SURFACE, BET_RECT)
                                pygame.display.update()
                                pygame.time.delay(1500)


                        elif len(luck_list) == 2: # 같은 수 2개
                            point_status += point_bet * 1

                            RESULT_PAIR_SURFACE = MAINFONT.render('페어 (+1배) (+' + str(point_bet) +'$)',True, PALEBLUE)
                            RESULT_PAIR_RECT = RESULT_PAIR_SURFACE.get_rect(midleft = result_midleft)
                            SURFACE.blit(RESULT_PAIR_SURFACE, RESULT_PAIR_RECT)

                            point_bet = 0

                            SURFACE.blit(POINT_SURFACE, POINT_RECT)
                            SURFACE.blit(BET_SURFACE, BET_RECT)

                            pygame.display.update()
                            pygame.time.delay(1500)



                        else: # 다 다른 수
                            if luck_list[0] + luck_list[1] + luck_list[2] == 6: # 123
                                point_status -= point_bet * 3
                                SURFACE.blit(POINT_SURFACE, POINT_RECT)
                                SURFACE.blit(BET_SURFACE, BET_RECT)
                                RESULT_123_SURFACE = MAINFONT.render('1 2 3 (-3배) (-' + str(3*point_bet) +'$)', True, RED)
                                RESULT_123_RECT = RESULT_123_SURFACE.get_rect(midleft = result_midleft)
                                SURFACE.blit(RESULT_123_SURFACE, RESULT_123_RECT)
                                pygame.display.update()
                                pygame.time.delay(1500)

                                
                                if point_status <= 0:
                                    SURFACE.fill(BLACK)
                                    GAME_OVER_SURFACE = BIGFONT.render("GAME OVER", True, RED, BLACK)
                                    GAME_OVER_RECT = GAME_OVER_SURFACE.get_rect(center = [400, 300])
                                    SURFACE.blit(GAME_OVER_SURFACE, GAME_OVER_RECT)
                                    pygame.display.update()
                                    pygame.time.delay(1500)

                                    import DICERS_main
                                    DICERS_main.main()


                                point_bet = 0

                                pygame.display.update()
                                pygame.time.delay(2000)


                            elif luck_list[0] + luck_list[1] + luck_list [2] == 15: # 456
                                SURFACE.blit(POINT_SURFACE, POINT_RECT)
                                SURFACE.blit(BET_SURFACE, BET_RECT)
                                RESULT_SURFACE = MAINFONT.render('4 5 6 (+3배)(+' + str(3*point_bet) +'$)', True, BLUE)
                                RESULT_RECT = RESULT_SURFACE.get_rect(midleft = result_midleft)
                                point_status += point_bet * 3
                                point_bet = 0
                                SURFACE.blit(RESULT_SURFACE, RESULT_RECT)
                                pygame.display.update()
                                pygame.time.delay(1500)

                            else: # 족보 없음

                                SURFACE.blit(POINT_SURFACE, POINT_RECT)
                                SURFACE.blit(BET_SURFACE, BET_RECT)

                                RESULT_NOSET_SURFACE = MAINFONT.render("족보 없음 (-1배)(-"+ str(point_bet) +'$)', True, PALERED)
                                RESULT_NOSET_RECT = RESULT_NOSET_SURFACE.get_rect(midleft = result_midleft)
                                SURFACE.blit(RESULT_NOSET_SURFACE, RESULT_NOSET_RECT)
                                pygame.display.update()
                                pygame.time.delay(1500)


                                if point_status <= 0:
                                    SURFACE.fill(BLACK)
                                    GAME_OVER_SURFACE = BIGFONT.render("GAME OVER", True, RED, BLACK)
                                    GAME_OVER_RECT = GAME_OVER_SURFACE.get_rect(center=[400, 300])
                                    SURFACE.blit(GAME_OVER_SURFACE, GAME_OVER_RECT)
                                    pygame.display.update()
                                    pygame.time.delay(1500)

                                    import DICERS_main
                                    DICERS_main.main()

                                point_bet = 0
                                pygame.display.update()
                                pygame.time.delay(1500)

                        pygame.display.update()

                    else:
                        SURFACE.blit(YMBF_SURFACE, YMBF_RECT)
                        pygame.display.update()
                        pygame.time.delay(800)

                if SAVE_RECT.collidepoint(event.pos):
                    SURFACE.fill(BLACK)
                    REGI_SURFACE = BIGFONT.render("새 입력창을 확인하세요.", True, GRAY)
                    REGI_RECT = REGI_SURFACE.get_rect(center = [400, 300])
                    SURFACE.blit(REGI_SURFACE, REGI_RECT)
                    pygame.display.update()

                    import sys
                    from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog)

                    class Register(QWidget):

                        def __init__(self):
                            super().__init__()
                            self.setWindowTitle('RANK')
                            self.setGeometry(1200, 500, 200, 100)
                            self.input()


                        def input(self):
                            text, ok = QInputDialog.getText(self, 'RANK', '이름을 입력하세요.')

                            playername = (str(text))

                            if ok:
                                import DICERS_rankcal
                                info = [playername, point_status, round]
                                with open('ranks/rich.txt', 'a', encoding='utf-8') as rich:
                                    rich.write(str(info[0]) + "," + str(info[1]) + ",")
                                DICERS_rankcal.r_sort()
                                with open('ranks/clever.txt', 'a', encoding='utf-8') as clever:
                                    clever.write(str(info[0]) + "," + str((info[1] / info[2])) + ",")
                                DICERS_rankcal.c_sort()
                                with open('ranks/long.txt', 'a', encoding='utf-8') as long:
                                    long.write(str(info[0]) + "," + str(info[2]) + ",")
                                DICERS_rankcal.l_sort()

                            import DICERS_main
                            DICERS_main.main()


                    app = QApplication(sys.argv)
                    ex = Register()
                    sys.exit(app.exec_())

            if event.type == pygame.MOUSEMOTION:

                if BETPLUS20_RECT.collidepoint(event.pos):
                    pygame.draw.rect(SURFACE, BLUE, BETPLUS20BOX)
                    SURFACE.blit(BETPLUS20_SURFACE, BETPLUS20_RECT)

                elif BETPLUS5_RECT.collidepoint(event.pos):
                    pygame.draw.rect(SURFACE, BLUE, BETPLUS5BOX)
                    SURFACE.blit(BETPLUS5_SURFACE, BETPLUS5_RECT)

                elif BETPLUS1_RECT.collidepoint(event.pos):
                    pygame.draw.rect(SURFACE, BLUE, BETPLUS1BOX)
                    SURFACE.blit(BETPLUS1_SURFACE, BETPLUS1_RECT)

                elif ALLIN_RECT.collidepoint(event.pos):
                    ALLIN_SURFACE = MAINFONT.render("A L L - I N", True, BLACK)
                    pygame.draw.rect(SURFACE, WHITE, ALLINBOX)
                    SURFACE.blit(ALLIN_SURFACE, ALLIN_RECT)

                elif BETMINUS20_RECT.collidepoint(event.pos):
                    pygame.draw.rect(SURFACE, RED, BETMINUS20BOX)
                    SURFACE.blit(BETMINUS20_SURFACE, BETMINUS20_RECT)

                elif BETMINUS5_RECT.collidepoint(event.pos):
                    pygame.draw.rect(SURFACE, RED, BETMINUS5BOX)
                    SURFACE.blit(BETMINUS5_SURFACE, BETMINUS5_RECT)

                elif BETMINUS1_RECT.collidepoint(event.pos):
                    pygame.draw.rect(SURFACE, RED, BETMINUS1BOX)
                    SURFACE.blit(BETMINUS1_SURFACE, BETMINUS1_RECT)

                elif CLEAR_RECT.collidepoint(event.pos):
                    CLEAR_SURFACE = MAINFONT.render("C L E A R", True, BLACK)
                    pygame.draw.rect(SURFACE, WHITE, CLEARBOX)
                    SURFACE.blit(CLEAR_SURFACE, CLEAR_RECT)

                elif RETRY_RECT.collidepoint(event.pos):
                    RETRY_SURFACE = MAINFONT.render("$ RETRY(GO TO MAIN) $", True, RED)
                    RETRY_RECT = RETRY_SURFACE.get_rect(center=[165, 550])
                    SURFACE.blit(RETRY_SURFACE, RETRY_RECT)

                elif SAVE_RECT.collidepoint(event.pos):
                    SAVE_SURFACE = MAINFONT.render("$ SAVE TO RANK $", True, RED)
                    SAVE_RECT = SAVE_SURFACE.get_rect(center=[665, 550])
                    SURFACE.blit(SAVE_SURFACE, SAVE_RECT)

                elif ROLL_RECT.collidepoint(event.pos):
                    ROLL_SURFACE = MIDDLEFONT.render("ROLL", True, RED)
                    pygame.draw.rect(SURFACE, BLACK, ROLL_BOX)
                    SURFACE.blit(ROLL_SURFACE, ROLL_RECT)

            pygame.display.update()
        pygame.display.update()

