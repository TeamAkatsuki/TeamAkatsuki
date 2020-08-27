import pygame
import random
import time

_py_x = 1000 # 창의 크기
_py_y = 500
galaxy = [(250,250),(750,250)] # 사진의 좌표

pygame.init()
font = pygame.font.Font("TmonMonsori.ttf.ttf", 50)
main_font = font.render("시작 하실려면 아무키나 눌러주세요",True,(0,0,0))
main_rect = main_font.get_rect(center=(500,250))
bo = pygame.image.load("image\\bo.png")
jja = pygame.image.load("image\\jja.png")
kimchi = pygame.image.load("image\\kimchi.png")
pi = pygame.image.load("image\\pi.png")
chi = pygame.image.load("image\\chi.png")
ca = pygame.image.load("image\\ca.png")
udong = pygame.image.load("image\\udong.png")
pa = pygame.image.load("image\\pa.png")
la = pygame.image.load("image\\la.png")
deop = pygame.image.load("image\\deop.png")
sam = pygame.image.load("image\\sam.png")
cho = pygame.image.load("image\\cho.png")
nang = pygame.image.load("image\\nang.png")
ham = pygame.image.load("image\\ham.png")
don = pygame.image.load("image\\don.png")
gug = pygame.image.load("image\\gug.png")
sixteen = [bo,jja,kimchi,pi,chi,ca,udong,pa,la,deop,sam,cho,nang,ham,don,gug] # 16강 리스트
random.shuffle(sixteen) # 랜덤
eight = [] # 8강 리스트
four = [] # 4강 리스트
final = [] # 결승 리스트
gamepad = pygame.display.set_mode((_py_x,_py_y)) # 창띄우는 코드
page = 0 # 게임상태 분류
first_pic = [] # 왼쪽에 있는 사진을 보여주는 리스트 랜덤으로 들어간다.
second_pic = [] # 오른쪽에 있는 사진을 보여주는 리스트 랜덤으로 들어간다.
sixteen_font = font.render("16강", True, (0, 0, 0)) # 16강 부터 우승의 폰트
eight_font = font.render("8강", True, (0, 0, 0))
four_font = font.render("4강", True, (0, 0, 0))
final_font = font.render("결승", True, (0, 0, 0))
win_font = font.render("우승", True, (0, 0, 0))

def startgame():
    global page, first_pic, second_pic # 이 함수안에서 쓸수있게 해주는 함수
    while True:
        while page == 0:  #초기화면
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #break
                if event.type == pygame.KEYDOWN:
                    page = 1
                    gamepad.fill((255, 255, 255))
                    gamepad.blit(sixteen_font, (450, 220))
                    pygame.display.update()
                    time.sleep(1.3)
                    startgame()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    page = 1
                    gamepad.fill((255,255,255))
                    gamepad.blit(sixteen_font,(450,220))
                    pygame.display.update()
                    time.sleep(1.3)
                    startgame()
            gamepad.fill((255,255,255))
            gamepad.blit(main_font,main_rect)
            pygame.display.update()


        while page == 1:
            events = pygame.event.get()
            for event in events: # 프로그램을 처리해주는 함수
                if event.type == pygame.QUIT:
                    pygame.quit() # X를 눌렀을때 파이게임을 종료한다
                    break
                if event.type == pygame.MOUSEBUTTONDOWN: # 클릭을 했을때
                    for _mouse_pos in galaxy:
                        if first_rect.collidepoint(event.pos) and len(first_pic) > 0: # 사진을 클릭했을때 first_pic은 길이가 1이되고 0보다 길이가커지면
                            eight.append(first_pic.pop(-1)) # 8강 리스트의 클릭한 사진을 추가
                            first_pic = [] # 다시 리스트를 비워주고 다음 사진 보이게 한다
                            second_pic = []
                        if second_rect.collidepoint(event.pos) and len(second_pic) > 0:
                            eight.append(second_pic.pop(-1))
                            first_pic = []
                            second_pic = []
            if len(eight) == 8:
                gamepad.fill((255,255,255))
                gamepad.blit(eight_font,(450,220))
                pygame.display.update()
                time.sleep(1.3)
                page = 2
                startgame()

            if len(first_pic) == 0 and len(second_pic) == 0:
                first_pic.append(sixteen.pop(0))
                first_rect = first_pic[0].get_rect(center=galaxy[0])
                second_pic.append(sixteen.pop(0))
                second_rect = second_pic[0].get_rect(center=galaxy[1])
            gamepad.fill((255,255,255))
            gamepad.blit(first_pic[0],first_rect) # 그릴 이미지 , 그릴 위치 [300,200]
            gamepad.blit(second_pic[0],second_rect)
            pygame.display.update()

        while page == 2:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for _mouse_pos in galaxy:
                        if first_rect.collidepoint(event.pos) and len(first_pic) > 0:
                            four.append(first_pic.pop(-1))
                            first_pic = []
                            second_pic = []
                        if second_rect.collidepoint(event.pos) and len(second_pic) > 0:
                            four.append(second_pic.pop(-1))
                            first_pic = []
                            second_pic = []
                if len(four) == 4:
                    gamepad.fill((255, 255, 255))
                    gamepad.blit(four_font,(450,220))
                    pygame.display.update()
                    time.sleep(1.3)
                    page = 3
                    startgame()

            if len(first_pic) == 0 and len(second_pic) == 0:
                first_pic.append(eight.pop(0))
                first_rect = first_pic[0].get_rect(center=galaxy[0])
                second_pic.append(eight.pop(0))
                second_rect = second_pic[0].get_rect(center=galaxy[1])
            gamepad.fill((255, 255, 255))
            gamepad.blit(first_pic[0], first_rect)  # 그릴 이미지 , 그릴 위치 [300,200]
            gamepad.blit(second_pic[0], second_rect)
            pygame.display.update()


        while page == 3:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for _mouse_pos in galaxy:
                        if first_rect.collidepoint(event.pos) and len(first_pic) > 0:
                            final.append(first_pic.pop(-1))
                            first_pic = []
                            second_pic = []
                        if second_rect.collidepoint(event.pos) and len(second_pic) > 0:
                            final.append(second_pic.pop(-1))
                            first_pic = []
                            second_pic = []
            if len(final) == 2:
                page = 4
                gamepad.fill((255, 255, 255))
                gamepad.blit(final_font,(450,220))
                pygame.display.update()
                time.sleep(1.3)
                startgame()

            if len(first_pic) == 0 and len(second_pic) == 0:
                first_pic.append(four.pop(0))
                first_rect = first_pic[0].get_rect(center=galaxy[0])
                second_pic.append(four.pop(0))
                second_rect = second_pic[0].get_rect(center=galaxy[1])
            gamepad.fill((255, 255, 255))
            gamepad.blit(first_pic[0], first_rect)  # 그릴 이미지 , 그릴 위치 [300,200]
            gamepad.blit(second_pic[0], second_rect)
            pygame.display.update()

        while page == 4:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for _mouse_pos in galaxy:
                        if first_rect.collidepoint(event.pos) and len(first_pic) > 0:
                            second_pic = []
                            page = 5
                            startgame()
                        if second_rect.collidepoint(event.pos) and len(second_pic) > 0:
                            page =5
                            first_pic = []
                            gamepad.fill((255, 255, 255))
                            gamepad.blit(win_font,(450,220))
                            pygame.display.update()
                            time.sleep(1.3)
                            startgame()




            if len(first_pic) == 0 and len(second_pic) == 0:
                first_pic.append(final.pop(0))
                first_rect = first_pic[0].get_rect(center=galaxy[0])
                second_pic.append(final.pop(0))
                second_rect = second_pic[0].get_rect(center=galaxy[1])
            gamepad.fill((255, 255, 255))
            gamepad.blit(first_pic[0], first_rect)  # 그릴 이미지 , 그릴 위치 [300,200]
            gamepad.blit(second_pic[0], second_rect)
            pygame.display.update()


        while page == 5:
            center_rect = jja.get_rect(center=(500, 250)) # 짜장면의 크기를 가져오고 우승사진 중심좌표 맞춘다
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            gamepad.fill((255,255,255))
            if len(first_pic) == 1:
                gamepad.blit(first_pic[0],center_rect)
            else:
                gamepad.blit(second_pic[0],center_rect)
            pygame.display.update()


        pygame.display.update()



startgame()