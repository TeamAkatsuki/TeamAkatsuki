import pygame
import time
import snake,one_to_50,hanoi
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0,0,0)
pad_width = 1040#1024 # 게임판의 크기설정
pad_heith  = 500#490

class Data_base():

    def __init__(self):
        self.snake_score = 0
        self.one_to_50_score = 0
        self.hanoi_score = 0
        self.score_dic = {}
    def save_data(self):
        pass
    def load_data(self):
        pass

def main_display(): # 초기 로고타이틀 출력함수
    global gamepad, main_btn, clock ,main_btn_rect
    main_btn_rect = main_btn.get_rect()
    main_btn_rect.center = (int((pad_width) / 2), int((pad_heith) / 2))  # 해당좌표를 main_btn의 중심좌표로 지정한다
    i = 0
    while i<255:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        i +=10
        main_btn.set_alpha(i)
        gamepad.blit(main_btn, main_btn_rect)
        clock.tick(30)
        pygame.display.update()
        time.sleep(0.1)
    runGame(1)



def runGame(state):
    global gamepad, clock, game_status,text , font ,texts,gamestart_t
    global mainfont
    global y_change,x_change,crashed,menu
    global savefile_o,savefile,alpha
    global background, main_btn
    game_status = state
  #game_status의 숫자를 기준으로 게임의 상태를 구분
    menu = 0
    sub_menu = 0
    while game_status == 1: # 초기메뉴화면
        main_text1 = font.render("게임 시작", True, (255, 255, 255), (100, 100, 100))
        main_text1_1 = font.render("게임 시작", True,(255,255,255))
        main_text2 = font.render("종료 하기", True,(255,255,255),(100,100,100))
        main_text2_1 = font.render("종료 하기", True,(255,255,255))
        gamepad.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if menu < 1:
                        menu = menu + 1
                if event.key == pygame.K_UP:
                    if menu > 0:
                        menu = menu - 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if menu == 0:
                        runGame(2)
                    elif menu == 1:
                        pygame.quit()
        if menu == 0:
            gamepad.blit(main_text1,(40,256))
            gamepad.blit(main_text2_1,(40,280))
        elif menu == 1:
            gamepad.blit(main_text1_1,(40,256))
            gamepad.blit(main_text2,(40,280))

        pygame.display.update()
        clock.tick(60)
    while game_status == 2: # 게임선택화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if sub_menu < 2:
                        sub_menu += 1
                if event.key == pygame.K_LEFT:
                    if sub_menu > 0:
                        sub_menu -= 1
                if event.key == pygame.K_KP_ENTER:
                    if sub_menu == 0 :
                        snake.start_game()
                    elif sub_menu == 1:
                        one_to_50.initgame()
                    elif sub_menu == 2:
                        hanoi.initgame()

        gamepad.fill(BLACK)

        pygame.display.update()
        clock.tick(60)

def initGame(): # 게임 초기설정 초기화
    global gamepad, clock,player2 ,font  ,text,texts
    global mainfont
    global y_change,x_change,game_status,crashed,menu
    global background, main_btn
    global t1,t2
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_heith))
    pygame.display.set_caption("뭘 봐")
    background = pygame.image.load("image\\background.png")
    font = pygame.font.Font('BMJUA_ttf.ttf', 25)
    mainfont = pygame.font.Font('BMJUA_ttf.ttf',110)
    main_btn = pygame.image.load("image\\mainlogo2.png")
    y_change =0
    x_change =0
    game_status = 0
    crashed = False
    menu = 0
    clock = pygame.time.Clock()
    main_display()


initGame()