import pygame, sys
from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((500,650))
pygame.display.set_caption('RANDOM LUNCH')

PINK = (255, 103, 129)
PINK2 = (255, 192, 203)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font('NanumSquareRoundB.ttf',20)
font2 = pygame.font.Font('NanumSquareRoundB.ttf',50)
font3 = pygame.font.Font('NanumSquareRoundB.ttf',22)

text =[font.render('한식',True,(255,255,255)),font.render("일식",True,(255,255,255)),
       font.render('중식',True,(255,255,255)),font.render('양식',True,(255,255,255)),
       font.render('기타',True,(255,255,255))]

text_2 = [font.render('Random',True,(255,103,129)),font2.render('점심 메뉴 뽑기!',True,(0,0,0)),
          font3.render('아래의 메뉴 중',True,(0,0,0)),font3.render('하나를 눌러주세요',True,(0,0,0))]

textmenu_rect = [text[0].get_rect(center=(250,250)),text[0].get_rect(center=(250,320)),
             text[0].get_rect(center=(250,390)),text[0].get_rect(center=(250,460)),
             text[0].get_rect(center=(250,530))]

textmain_rect = [text[0].get_rect(center=(70,40)),text[0].get_rect(center=(110,65)),
                 text[0].get_rect(center=(200,135)),text[0].get_rect(center=(185,165))]


DISPLAY.fill((255,255,255))
DISPLAY.blit(text_2[0],textmain_rect[0])
DISPLAY.blit(text_2[1],textmain_rect[1])
DISPLAY.blit(text_2[2],textmain_rect[2])
DISPLAY.blit(text_2[3],textmain_rect[3])

btn1 = pygame.draw.rect(DISPLAY,PINK,(75, 230, 350,40))
DISPLAY.blit(text[0],textmenu_rect[0])

btn2 = pygame.draw.rect(DISPLAY,PINK,(75, 300, 350,40))
DISPLAY.blit(text[1],textmenu_rect[1])

btn3 = pygame.draw.rect(DISPLAY,PINK,(75, 370, 350, 40))
DISPLAY.blit(text[2],textmenu_rect[2])

btn4 = pygame.draw.rect(DISPLAY,PINK,(75, 440, 350,40))
DISPLAY.blit(text[3],textmenu_rect[3])

btn5 = pygame.draw.rect(DISPLAY,PINK,(75, 510, 350,40))
DISPLAY.blit(text[4],textmenu_rect[4])

pygame.draw.rect(DISPLAY, (255, 103, 129), (42, 5, 415, 600), 3)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if btn1.collidepoint(event.pos):
                print('배고파')

            if btn2.collidepoint(event.pos):
                pass
            if btn3.collidepoint(event.pos):
                pass
            if btn4.collidepoint(event.pos):
                pass
            if btn5.collidepoint(event.pos):
                pass

        if event.type == pygame.MOUSEMOTION:
            if btn1.collidepoint(event.pos):
                btn_1 = pygame.draw.rect(DISPLAY, PINK2, (75, 230, 350, 40))
                DISPLAY.blit(text[0], textmenu_rect[0])
                pygame.display.update()
            else:
                 btn1 = pygame.draw.rect(DISPLAY, PINK, (75, 230, 350, 40))
                 DISPLAY.blit(text[0], textmenu_rect[0])

        if event.type == pygame.MOUSEMOTION:
            if btn2.collidepoint(event.pos):
                btn_2 = pygame.draw.rect(DISPLAY, PINK2, (75, 300, 350, 40))
                DISPLAY.blit(text[1], textmenu_rect[1])
                pygame.display.update()
            else:
                btn2 = pygame.draw.rect(DISPLAY, PINK, (75, 300, 350, 40))
                DISPLAY.blit(text[1], textmenu_rect[1])

        if event.type == pygame.MOUSEMOTION:
            if btn3.collidepoint(event.pos):
                btn_3 = pygame.draw.rect(DISPLAY, PINK2, (75, 370, 350, 40))
                DISPLAY.blit(text[2], textmenu_rect[2])
                pygame.display.update()
            else:
                btn3 = pygame.draw.rect(DISPLAY, PINK, (75, 370, 350, 40))
                DISPLAY.blit(text[2], textmenu_rect[2])

        if event.type == pygame.MOUSEMOTION:
            if btn4.collidepoint(event.pos):
                btn_4 = pygame.draw.rect(DISPLAY, PINK2, (75, 440, 350, 40))
                DISPLAY.blit(text[3], textmenu_rect[3])
                pygame.display.update()
            else:
                btn4 = pygame.draw.rect(DISPLAY, PINK, (75, 440, 350, 40))
                DISPLAY.blit(text[3], textmenu_rect[3])

        if event.type == pygame.MOUSEMOTION:
            if btn5.collidepoint(event.pos):
                btn_5 = pygame.draw.rect(DISPLAY, PINK2, (75, 510, 350, 40))
                DISPLAY.blit(text[4], textmenu_rect[4])
                pygame.display.update()
            else:
                btn5 = pygame.draw.rect(DISPLAY, PINK, (75, 510, 350, 40))
                DISPLAY.blit(text[4], textmenu_rect[4])