import pygame
# import time
import datetime
import random
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 500

pygame.init() # 모듈 초기화
gamepad = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
block = pygame.image.load("image\\pixel.png")
player_head =pygame.image.load("image\\Snake\\head.png").convert()
player_body =pygame.image.load("image\\Snake\\body.png").convert()
item_feed = pygame.image.load("image\\Snake\\feed.png").convert()
font = pygame.font.Font('BMJUA_ttf.ttf', 25)
'''캐릭터방향세팅'''
Player_see = {pygame.K_UP:'UP' ,pygame.K_DOWN:'DOWN',pygame.K_RIGHT:'RIGHT',pygame.K_LEFT:'LEFT'}
Player_move = datetime.datetime.now()
Head_see = 'LEFT'

'''게임 초기 세팅'''
game_time = 0.3
INIT_TURN = datetime.timedelta(seconds= game_time)
body_len = 0
score = 0
speed = 0.1

def background():
    scoreground = pygame.Rect((0,0),(240,500))
    scoreground.center = (920,250)
    background = pygame.Rect((0, 0), (800, 500))
    background.center = (400, 250)
    pygame.draw.rect(gamepad, ( 0,0,0),scoreground)
    pygame.draw.rect(gamepad, (255, 255, 255), background)

def draw_block(screen,color,position):

    gamepad.blit(block,(position[0]*block_size,position[1]*block_size))
class Self_die(Exception):
    pass

class Player(): # 플레이어
    # color = GREEN
    def __init__(self):
        self.positions = [(520,240),(520,260)]
        self.direction = 'UP'
    def lenup(self):
        last_position = self.positions[-1]
        x , y = last_position
        if self.direction == 'UP':
            self.positions.append((x,y+20))
        elif self.direction == 'DOWN':
            self.positions.append((x,y-20))
        elif self.direction == 'RIGHT':
            self.positions.append((x-20,y))
        elif self.direction == 'LEFT':
            self.positions.append((x+20,y))

    def create(self,gamepad):
        for position in self.positions:
            if self.positions[0] == position:
                gamepad.blit(player_head,position)
            else:
                gamepad.blit(player_body,position)

    def eat_item(self):
        head_position = self.positions[0]
        x,y = head_position
        if self.direction == 'UP':
            self.positions = [(x,y-20)] + self.positions[:-1]
        elif self.direction == 'DOWN':
            self.positions = [(x,y+20)] + self.positions[:-1]
        elif self.direction == 'RIGHT':
            self.positions = [(x+20,y)] + self.positions[:-1]
        elif  self.direction == 'LEFT':
            self.positions = [(x-20,y)] + self.positions[:-1]

    def rotate(self,see):
        self.direction = see

class Item(): # 먹을 먹이

    def __init__(self, position =(60,60)):
        self.position = position
    def create(self,gamepad):
        gamepad.blit(item_feed,self.position)

class Gamepad(): # 게임판

    def __init__(self):
        self.player = Player()
        self.item = Item()
    def  create(self,gamepad):
        self.player.create(gamepad)
        self.item.create(gamepad)
    def init_game(self):
        global game_time ,  score,speed
        self.player.eat_item()
        if self.player.positions[0] == self.item.position:
            score += 100
            speed += 0.1
            game_time = game_time * 0.97
            self.player.lenup()
            self.new_item()
        if self.player.positions[0] in self.player.positions[1:]:
            raise Self_die()
        if self.player.positions[0][0] < 0 or self.player.positions[0][1] < 0:
            raise Self_die()
        elif self.player.positions[0][0] == 800 or self.player.positions[0][1] == SCREEN_HEIGHT:
            raise Self_die()
    def new_item(self):
        global time,time2
        self.item = Item((random.randint(0,38)*20,random.randint(0,23)*20))
        for position in self.player.positions:
            if self.item.position == position:
                self.new_item()
                break
def start_game():
    global Head_see, block
    global Player_move, Player_see
    global block_size ,block_position

    game_pad = Gamepad()
    while True:
        main_text2 = font.render("스피드 :%0.1f"%speed, True ,(255,255,255))
        main_text1 = font.render("점수 : %d" % score, True, (255, 255, 255))
        len_text = font.render("길이 : %d"%len(game_pad.player.positions[1:]),True, (255,255,255))
        INIT_TURN = datetime.timedelta(seconds=game_time)
        events = pygame.event.get()  # ❶ 발생한 이벤트 목록을 읽어들인다
        for event in events:         # ❷ 이벤트 목록을 순회하며 각 이벤트를 처리한다
            if event.type == pygame.QUIT:  # ❸ 종료 이벤트가 발생한 경우
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in Player_see:
                    if game_pad.player.direction == 'UP' and Player_see[event.key] == 'DOWN':
                        pass
                    elif game_pad.player.direction == 'DOWN' and Player_see[event.key] == 'UP':
                        pass
                    elif game_pad.player.direction == 'RIGHT' and Player_see[event.key] == 'LEFT':
                        pass
                    elif game_pad.player.direction == 'LEFT'  and Player_see[event.key] == 'RIGHT':
                        pass
                    else:
                        game_pad.player.rotate(Player_see[event.key])


        if datetime.timedelta(seconds=1) <= datetime.datetime.now() - Player_move:
            if Head_see == 'UP':
                block_position[1] = block_position[1] - 20
            elif Head_see == 'DOWN':
                block_position[1] = block_position[1]  + 20
            elif Head_see == 'RIGHT':
                block_position[0]  = block_position[0] + 20
            elif Head_see == 'LEFT':
                block_position[0] = block_position[0] - 20
            Player_move = datetime.datetime.now()

        if INIT_TURN < datetime.datetime.now() - Player_move:
            try:
                game_pad.init_game()
            except Self_die:
                exit()
            Player_move = datetime.datetime.now()

        background()
        gamepad.blit(len_text,(SCREEN_WIDTH-120,SCREEN_HEIGHT-420))
        gamepad.blit(main_text2,(SCREEN_WIDTH-120,SCREEN_HEIGHT-450))
        gamepad.blit(main_text1,(SCREEN_WIDTH-120,SCREEN_HEIGHT-480))
        game_pad.create(gamepad)
        pygame.display.update()

if __name__ == '__main__':
    start_game()
