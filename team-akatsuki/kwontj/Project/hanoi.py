import pygame
import time
import random



pad_width = 1040#1024 # 게임판의 크기설정
pad_heith  = 500#490
'''이미지 로드'''
hanoi_1 = pygame.image.load("image\\Hanoi_image\\Hanoi_1.png")
hanoi_2 = pygame.image.load("image\\Hanoi_image\\Hanoi_2.png")
hanoi_3 = pygame.image.load("image\\Hanoi_image\\Hanoi_3.png")
hanoi_4 = pygame.image.load("image\\Hanoi_image\\Hanoi_4.png")
hanoi_5 = pygame.image.load("image\\Hanoi_image\\Hanoi_5.png")
hanoi_6 = pygame.image.load("image\\Hanoi_image\\Hanoi_6.png")
hanoi_7 = pygame.image.load("image\\Hanoi_image\\Hanoi_7.png")
hanoi_pad = pygame.image.load("image\\Hanoi_image\\hanoi_pad.png")
'''기타 세팅'''
pos = [0,0]
class Hanoi():
    global gamepad
    def __init__(self):
        self.first_hanoi = [7,6,5,4,3,2,1]
        self.second_hanoi = []
        self.third_hanoi = []
        self.rect_list = [(190,455),(190,435),(190,415),(190,395),(190,375),(190,355),(190,335)]
        self.rect_list2 = [(490,455),(490,435),(490,415),(490,395),(490,375),(490,355),(490,335)]
        self.rect_list3 = [(790,455),(790,435),(790,415),(790,395),(790,375),(790,355),(790,335)]
        self.image_list1 = []
        self.image_list2 = []
        self.image_list3 = []
        self.mouse_traking = []
        self.first_click = False
        self.second_click = False
        self.third_click = False

    def draw_hanoi_pad(self):
        gamepad.blit(hanoi_pad,(80,200))
        gamepad.blit(hanoi_pad,(380,200))
        gamepad.blit(hanoi_pad,(680,200))
    def draw_hanoi(self):
        if len(self.first_hanoi) > 0:
            for c_hanoi in self.first_hanoi:
                index_num = self.first_hanoi.index(c_hanoi)
                if c_hanoi == 7:
                    save_rect = self.rect_list[index_num]
                    con_rect = hanoi_7.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_7,con_rect)
                elif c_hanoi == 6:
                    save_rect = self.rect_list[index_num]
                    con_rect = hanoi_6.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_6,con_rect)
                elif c_hanoi == 5:
                    save_rect = self.rect_list[index_num]
                    con_rect = hanoi_5.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_5,con_rect)
                elif c_hanoi == 4:
                    save_rect = self.rect_list[index_num]
                    con_rect = hanoi_4.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_4,con_rect)
                elif c_hanoi == 3:
                    save_rect = self.rect_list[index_num]
                    con_rect = hanoi_3.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_3,con_rect)
                elif c_hanoi == 2:
                    save_rect =self.rect_list[index_num]
                    con_rect = hanoi_2.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_2,con_rect)
                elif c_hanoi == 1:
                    save_rect =self.rect_list[index_num]
                    con_rect = hanoi_1.get_rect(center=save_rect)
                    self.image_list1.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_1,con_rect)
        if len(self.second_hanoi) > 0:
            for c_hanoi in self.second_hanoi:
                index_num = self.second_hanoi.index(c_hanoi)
                if c_hanoi == 7:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_7.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_7, con_rect)
                elif c_hanoi == 6:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_6.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_6, con_rect)
                elif c_hanoi == 5:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_5.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_5, con_rect)
                elif c_hanoi == 4:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_4.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_4, con_rect)
                elif c_hanoi == 3:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_3.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_3, con_rect)
                elif c_hanoi == 2:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_2.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_2, con_rect)
                elif c_hanoi == 1:
                    save_rect = self.rect_list2[index_num]
                    con_rect = hanoi_1.get_rect(center=save_rect)
                    self.image_list2.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_1, con_rect)

        if len(self.third_hanoi) > 0:
            for c_hanoi in self.third_hanoi:
                index_num = self.third_hanoi.index(c_hanoi)
                if c_hanoi == 7:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_7.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_7, con_rect)
                elif c_hanoi == 6:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_6.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_6, con_rect)
                elif c_hanoi == 5:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_5.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_5, con_rect)
                elif c_hanoi == 4:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_4.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_4, con_rect)
                elif c_hanoi == 3:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_3.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_3, con_rect)
                elif c_hanoi == 2:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_2.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_2, con_rect)
                elif c_hanoi == 1:
                    save_rect = self.rect_list3[index_num]
                    con_rect = hanoi_1.get_rect(center=save_rect)
                    self.image_list3.append([con_rect,c_hanoi])
                    gamepad.blit(hanoi_1, con_rect)

    def check_Traking(self,check_num):
        if check_num == 1:
            if self.first_click == True:
                self.first_click = False
                self.first_hanoi.remove("Traking")
            else:
                self.first_click = True
                self.first_hanoi.append("Traking")
        elif check_num == 2:
            if self.second_click == True:
                self.second_click = False
                self.second_hanoi.remove("Traking")
            else:
                self.second_click = True
                self.second_hanoi.append("Traking")
        elif check_num == 3:
            if self.third_click == True:
                self.third_click = False
                self.third_hanoi.remove("Traking")
            else:
                self.third_click = True
                self.third_hanoi.append("Traking")

    def upgrade_Traking(self):
        if self.first_click == True:
            self.first_click = False
            self.first_hanoi.remove("Traking")
        elif self.second_click == True:
            self.second_click = False
            self.second_hanoi.remove("Traking")
        elif self.third_click == True:
            self.third_click = False
            self.third_hanoi.remove("Traking")



def startgame():
    global gamepad, game_pad
    while True:
        pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:  # 종료 이벤트가 발생한 경우
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if len(game_pad.image_list1) > 0:
                    for a in range(len(game_pad.image_list1)):
                        col_rect = game_pad.image_list1[a][0]
                        if col_rect.collidepoint(event.pos):
                            if game_pad.first_hanoi[-1] == game_pad.image_list1[a][1]:
                                if len(game_pad.mouse_traking) == 0:
                                    save_traking = game_pad.first_hanoi.pop(-1)
                                    game_pad.check_Traking(1)
                                    game_pad.mouse_traking.append(save_traking)
                if len(game_pad.image_list2) > 0:
                    for a in range(len(game_pad.image_list2)):
                        col_rect = game_pad.image_list2[a][0]
                        if col_rect.collidepoint(event.pos):
                            if game_pad.second_hanoi[-1] == game_pad.image_list2[a][1]:
                                if len(game_pad.mouse_traking) == 0:
                                    save_traking = game_pad.second_hanoi.pop(-1)
                                    game_pad.check_Traking(2)
                                    game_pad.mouse_traking.append(save_traking)
                if len(game_pad.image_list3) > 0:
                    for a in range(len(game_pad.image_list3)):
                        col_rect = game_pad.image_list3[a][0]
                        if col_rect.collidepoint(event.pos):
                            if game_pad.third_hanoi[-1] == game_pad.image_list3[a][1]:
                                if len(game_pad.mouse_traking) == 0:
                                    save_traking = game_pad.third_hanoi.pop(-1)
                                    game_pad.check_Traking(3)
                                    game_pad.mouse_traking.append(save_traking)

            if event.type == pygame.MOUSEBUTTONUP:
                if game_pad.mouse_traking:
                    if event.pos[0] <= 360:
                        if game_pad.first_hanoi[-1] != "Traking":
                            if game_pad.first_hanoi:
                                if game_pad.first_hanoi[-1] > game_pad.mouse_traking[0]:
                                    game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                    game_pad.upgrade_Traking()
                                    if game_pad.first_click == True:
                                        game_pad.check_Traking(1)
                                    elif game_pad.second_click == True:
                                        game_pad.check_Traking(2)
                                    elif game_pad.third_click == True:
                                        game_pad.check_Traking(3)
                                else:
                                    if game_pad.second_click:
                                        game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                                        game_pad.check_Traking(2)
                                    elif game_pad.third_click:
                                        game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                                        game_pad.check_Traking(3)
                                    elif game_pad.first_click:
                                        game_pad.first_hanoi.pop(-1)
                                        game_pad.check_Traking(1)

                            else:
                                game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                if game_pad.first_click:
                                    game_pad.check_Traking(1)
                                    game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                elif game_pad.second_click:
                                    game_pad.check_Traking(2)
                                    game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                                elif game_pad.third_click:
                                    game_pad.check_Traking(3)
                                    game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                        else:
                            if game_pad.first_click:
                                game_pad.check_Traking(1)
                            elif game_pad.second_click:
                                game_pad.check_Traking(2)
                            elif game_pad.third_click:
                                game_pad.check_Traking(3)

                    elif 360 < event.pos[0] <= 660:
                        if game_pad.second_hanoi:
                            if game_pad.second_hanoi[-1] != "Traking":
                                if game_pad.second_hanoi[-1] > game_pad.mouse_traking[0]:
                                    game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                                    game_pad.upgrade_Traking()
                                else:
                                    if game_pad.first_click:
                                        game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                        game_pad.check_Traking(1)
                                    elif game_pad.third_click:
                                        game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                                        game_pad.check_Traking(3)
                                    elif game_pad.second_click:
                                        game_pad.second_hanoi.pop(-1)
                                        game_pad.check_Traking(2)
                            else:
                                if game_pad.first_click:
                                    game_pad.check_Traking(1)
                                    game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                elif game_pad.second_click:
                                    game_pad.check_Traking(2)
                                    game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                                elif game_pad.third_click:
                                    game_pad.check_Traking(3)
                                    game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                        else:
                            game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                            if game_pad.first_click:
                                game_pad.check_Traking(1)
                            elif game_pad.second_click:
                                game_pad.check_Traking(2)
                            elif game_pad.third_click:
                                game_pad.check_Traking(3)

                    elif event.pos[0] > 660:
                        if game_pad.third_hanoi:
                            if game_pad.third_hanoi[-1] != "Traking":
                                if game_pad.third_hanoi[-1] > game_pad.mouse_traking[0]:
                                    game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                                    game_pad.upgrade_Traking()
                                else:
                                    if game_pad.first_click:
                                        game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                        game_pad.check_Traking(1)
                                    elif game_pad.second_click:
                                        game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                                        game_pad.check_Traking(2)
                            else:
                                if game_pad.first_click:
                                    game_pad.check_Traking(1)
                                    game_pad.first_hanoi.append(game_pad.mouse_traking.pop(-1))
                                elif game_pad.second_click:
                                    game_pad.check_Traking(2)
                                    game_pad.second_hanoi.append(game_pad.mouse_traking.pop(-1))
                                elif game_pad.third_click:
                                    game_pad.check_Traking(3)
                                    game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                        else:
                            game_pad.third_hanoi.append(game_pad.mouse_traking.pop(-1))
                            if game_pad.first_click:
                                game_pad.check_Traking(1)

                            elif game_pad.second_click:
                                game_pad.check_Traking(2)

                            elif game_pad.third_click:
                                game_pad.check_Traking(3)

        gamepad.fill((255, 255, 255))
        game_pad.draw_hanoi_pad()

        game_pad.draw_hanoi()
        if game_pad.mouse_traking:
            if game_pad.mouse_traking[0] == 1:
                gamepad.blit(hanoi_1,pos)
            elif game_pad.mouse_traking[0] == 2:
                gamepad.blit(hanoi_2,pos)
            elif game_pad.mouse_traking[0] == 3:
                gamepad.blit(hanoi_3,pos)
            elif game_pad.mouse_traking[0] == 4:
                gamepad.blit(hanoi_4,pos)
            elif game_pad.mouse_traking[0] == 5:
                gamepad.blit(hanoi_5,pos)
            elif game_pad.mouse_traking[0] == 6:
                gamepad.blit(hanoi_6,pos)
            elif game_pad.mouse_traking[0] == 7:
                gamepad.blit(hanoi_7,pos)

        print(game_pad.first_hanoi,game_pad.second_hanoi,game_pad.third_hanoi)
        pygame.display.update()

def initgame():
    global gamepad, clock , font, game_pad
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_heith))
    clock = pygame.time.Clock()
    font = pygame.font.Font('BMJUA_ttf.ttf', 45)
    game_pad = Hanoi()
    startgame()


if __name__ == "__MAIN__":
    initgame()