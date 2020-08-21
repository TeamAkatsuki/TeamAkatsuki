import pygame
import time
import random
from pygame.locals import *
import random

'''초기화 세팅'''
pygame.init()
pad_width = 1040
pad_heith = 500
gamepad = pygame.display.set_mode((pad_width, pad_heith))
clock = pygame.time.Clock()
''' 로드 세팅'''
block_image = pygame.image.load("image\\50pixel.png").convert()
blocks = []
blocks2 = []
blocks3 = []
blocks4 = []
blocks5 = []
first_str = []
second_str = []
font = pygame.font.Font('BMJUA_ttf.ttf', 45)
num_string = font.render("%s", True, (255, 255, 255))
num_string.get_rect()
mouse_pos = pygame.mouse.get_pos()
BLACK = (0,0,0)
game_count = 1
def draw_background():
    gamepad.fill((255, 255, 255))


class Gamepad():
    global gamepad

    def __init__(self):
        self.firstline = [[400, 100], (460, 100), (520, 100), (580, 100), (640, 100)]
        self.secondline = [(400, 160), (460, 160), (520, 160), (580, 160), (640, 160)]
        self.thirdline = [(400, 220), (460, 220), (520, 220), (580, 220), (640, 220)]
        self.fourline = [(400, 280), (460, 280), (520, 280), (580, 280), (640, 280)]
        self.fiveline = [(400, 340), (460, 340), (520, 340), (580, 340), (640, 340)]
        self.first_str = []
        self.second_str = []
    def string(self):

        for a in range(1, 26):
            self.first_str.append(a)
        for a in range(26, 51):
            self.second_str.append(a)
        random.shuffle(self.first_str)
        random.shuffle(self.second_str)

    def background(self):
        global block_image, blocks , blocks2,blocks3,blocks4,blocks5
        for a in self.firstline:
            block_rect = block_image.get_rect(topleft=a)
            blocks.append([block_rect,self.first_str.pop(random.randint(0,len(self.first_str)-1))])

        for a in self.secondline:
            block_rect = block_image.get_rect(topleft=a)
            blocks2.append([block_rect,self.first_str.pop(random.randint(0,len(self.first_str)-1))])


        for a in self.thirdline:
            block_rect = block_image.get_rect(topleft=a)
            blocks3.append([block_rect, self.first_str.pop(random.randint(0, len(self.first_str) - 1))])

        for a in self.fourline:
            block_rect = block_image.get_rect(topleft=a)
            blocks4.append([block_rect, self.first_str.pop(random.randint(0, len(self.first_str) - 1))])

        for a in self.fiveline:
            block_rect = block_image.get_rect(topleft=a)
            blocks5.append([block_rect, self.first_str.pop(random.randint(0, len(self.first_str) - 1))])




    def running(self):
        global gamepad, first_str, second_str ,BLACK , block_rect
        global blocks, blocks2, blocks3, blocks4, blocks5


        for position in blocks:
            # x, y = position
            if position[1] != 60:
                game_position = position[0]
                # blocks.append(block_rect)
                gamepad.blit(block_image,game_position)
                text_test = font.render("%s" % position[1], True, (255, 255, 255))
                gamepad.blit(text_test, game_position)



        for position in blocks2:
            if position[1] != 60:
                game_position = position[0]
                gamepad.blit(block_image,game_position)
                text_test = font.render("%s"% position[1], True, (255, 255, 255))
                gamepad.blit(text_test, game_position)

        for position in blocks3:
            if position[1] != 60:
                game_position = position[0]
                gamepad.blit(block_image,game_position)
                text_test = font.render("%s"% position[1], True, (255, 255, 255))
                gamepad.blit(text_test,game_position)

        for position in blocks4:
            if position[1] != 60:
                game_position = position[0]
                gamepad.blit(block_image, game_position)
                text_test = font.render("%s"% position[1], True, (255, 255, 255))
                gamepad.blit(text_test, game_position)

        for position in blocks5:
            if position[1] != 60:
                game_position = position[0]
                gamepad.blit(block_image, game_position)
                text_test = font.render("%s"%position[1], True, (255, 255, 255))
                gamepad.blit(text_test,game_position)


    def drawsetting(self):
        pass


def startgame():
    global game_pad, mouse_pos , block_rect
    global game_count

    while True:
        events = pygame.event.get()
        # print(blocks)
        for event in events:  # ❷ 이벤트 목록을 순회하며 각 이벤트를 처리한다
            if event.type == pygame.MOUSEBUTTONUP:


                for num in range(5):
                    if num <= len(blocks)-1:
                        block = blocks[num][0]
                    else:
                        break
                    #if block.collidepoint(event.pos) and blocks[num][1] == game_count:
                    if type(block) != list:
                        if block.collidepoint(event.pos) and blocks[num][1] == game_count:
                            if len(game_pad.second_str) > 0:
                                blocks[num] = [blocks[num][0],game_pad.second_str.pop(random.randrange(len(game_pad.second_str)))]
                            else:
                                blocks[num] = [blocks[num][0],60]

                            game_count += 1


                        #game_pad.running()

                        print("True")
                for num2 in range(5):
                    if num2 <= len(blocks2) - 1:
                        block2 = blocks2[num2][0]
                    else:
                        break
                    #if block2.collidepoint(event.pos) and blocks2[num2][1] == game_count:
                    if type(block2) != list:
                        if block2.collidepoint(event.pos) and blocks2[num2][1] == game_count:
                            if len(game_pad.second_str) > 0:
                                blocks2[num2] = [blocks2[num2][0],game_pad.second_str.pop(random.randrange(len(game_pad.second_str)))]
                            else:
                                blocks2[num2] = [blocks2[num2][0], 60]

                            game_count += 1


                        #game_pad.running()

                for num3 in range(5):
                    if num3 <= len(blocks3) - 1:
                        block3 = blocks3[num3][0]
                    else:
                        break
                    #if block3.collidepoint(event.pos) and blocks3[num3][1] == game_count:
                    if type(block3) != list:
                        if block3.collidepoint(event.pos) and blocks3[num3][1] == game_count and type(block3) != list:
                            if len(game_pad.second_str) > 0:
                                blocks3[num3] = [blocks3[num3][0],game_pad.second_str.pop(random.randrange(len(game_pad.second_str)))]
                            else:
                                blocks3[num3] = [blocks3[num3][0], 60]

                            game_count += 1
                        #game_pad.running()

                for num4 in range(5):
                    if num4 <= len(blocks4) - 1:
                        block4 = blocks4[num4][0]
                    else:
                        break
                    #if block4.collidepoint(event.pos) and blocks4[num4][1] == game_count:
                    if type(block4) != list:
                        if block4.collidepoint(event.pos) and blocks4[num4][1] == game_count and type(block4) != list:
                            if len(game_pad.second_str) > 0:
                                blocks4[num4] = [blocks4[num4][0],game_pad.second_str.pop(random.randrange(len(game_pad.second_str)))]
                            else:
                                blocks4[num4] = [blocks4[num4][0], 60]

                            game_count += 1

                        #game_pad.running()

                for num5 in range(5):
                    if num5 <= len(blocks5) - 1:
                        block5 = blocks5[num5][0]
                    else:
                        break
                    #if block5.collidepoint(event.pos) and blocks5[num5][1] == game_count:
                    if type(block5) != list:
                        if block5.collidepoint(event.pos) and blocks5[num5][1] == game_count and type(block5) != list:
                            if len(game_pad.second_str) > 0:
                                blocks5[num5] = [blocks5[num5][0],game_pad.second_str.pop(random.randrange(len(game_pad.second_str)))]
                            else:
                                blocks5[num5] = [blocks5[num5][0], 60]

                            game_count += 1



            if event.type == pygame.QUIT:  # ❸ 종료 이벤트가 발생한 경우
                exit()
        draw_background()
        if game_count == 51:
            pygame.quit()
        game_pad.running()
        pygame.display.update()


def initgame():
    global clock, gamepad
    global game_pad
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_heith))
    clock = pygame.time.Clock()
    game_pad = Gamepad()
    game_pad.string()
    game_pad.background()
    startgame()

if __name__ == "__MAIN__":
    initgame()
