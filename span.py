import pygame, time
from pygame.locals import *
import random, math, sys

pygame.init()

WHITE = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 32

FramesPerSec = pygame.time.Clock()
SCREEN_WIDTH = 572 * 3
SCREEN_HEIGHT = 256 * 3

phrases = []
phrases.append("oh for FUCKS sake")
phrases.append("oh COME on")
phrases.append("You owe arsalan 240 dollars")
phrases.append("Ahh SHIT")
phrases.append("you've GOT to be kidding me")
phrases.append("JEEZUS")
phrases.append("Beautiful")
phrases.append("Mouse Band Ho gaya Mera")
phrases.append("BHAIsahab")
phrases.append("tl;dr you're stupid")
phrases.append("Ae Nakli")
phrases.append("Tera Baap Nalla")
x = len(phrases)
#x_speed = 5
#y_speed = 5

#font = pygame.font.SysFont("Verdana", 60)

DIS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DIS.fill(BLACK)
pygame.display.set_caption("Don't blame connectivity")

class Paddle_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1 * 3, 256 * 3))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(3 * 3, SCREEN_HEIGHT / 2))
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_w]:
            if self.rect.top > 4 * 3:
                self.rect.move_ip(0, -4 * 3)
        if pressed_key[K_s]:
            if self.rect.bottom < SCREEN_HEIGHT - 4 * 3:
                self.rect.move_ip(0, 4 * 3)

class Paddle_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((12, 60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH - 15 * 3, SCREEN_HEIGHT / 2))
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_UP]:
            if self.rect.top > 8 * 3:
                self.rect.move_ip(0, -8 * 3)
        if pressed_key[K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT - 8 * 3:
                self.rect.move_ip(0, 8 * 3)
    def change_image(self, path):
        self.image = pygame.image.load(path)

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60,60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    def position(self, X, Y):
        self.rect.x = X 
        self.rect.y = Y

class Ball(pygame.sprite.Sprite):
    speed = 4 * 3
    x_speed = 0
    y_speed = 0
    angle = 0
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((4 * 3, 4 * 3))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.angle = random.uniform(0, 2 * 3.14529)
    def set_speed(self):
        self.speed = 5 * 3
        self.x_speed = 0
        while(abs(self.x_speed) < 1.5):
            self.angle = random.uniform(0, 2 * 3.14529)
            self.x_speed = self.speed * math.cos(self.angle)
            self.y_speed = self.speed * math.sin(self.angle)
    def move(self):
        if self.y_speed > 0:
            if self.rect.bottom > SCREEN_HEIGHT:
                self.y_speed = self.y_speed * -1
        elif self.y_speed < 0:
            if self.rect.top < 0:
                self.y_speed = self.y_speed * -1
        self.rect.move_ip(self.x_speed, self.y_speed)
count = 0
P1 = Paddle_1()
P2 = Paddle_2()
B1 = Ball()
B1.set_speed()
players = pygame.sprite.Group()
players2 = pygame.sprite.Group()
players.add(P1)
players.add(P2)
players2.add(P2)
s_a = 0
s_b = 0
font = pygame.font.SysFont("robotoslab", 90)
msg = ""
INC_SPEED = pygame.USEREVENT + 1
Change_Font = pygame.USEREVENT + 2
pygame.time.set_timer(INC_SPEED, 3000)
pygame.time.set_timer(Change_Font, 5000)
Br1 = Brick()
Br2 = Brick()
Br3 = Brick()
Br4 = Brick()
Br5 = Brick()
Br6 = Brick()
Br7 = Brick()
Br8 = Brick()
Br9 = Brick()
check = []
for v in range(9):
    check.append(0)
Br1.position(int(SCREEN_WIDTH * 1 / 10), int(SCREEN_HEIGHT * 2 / 10))
Br2.position(int(SCREEN_WIDTH * 1 / 10), int(SCREEN_HEIGHT * 5 / 10))
Br3.position(int(SCREEN_WIDTH * 1 / 10), int(SCREEN_HEIGHT * 8 / 10))
Br4.position(int(SCREEN_WIDTH * 4 / 10), int(SCREEN_HEIGHT * 2 / 10))
Br5.position(int(SCREEN_WIDTH * 4 / 10), int(SCREEN_HEIGHT * 5 / 10))
Br6.position(int(SCREEN_WIDTH * 4 / 10), int(SCREEN_HEIGHT * 8 / 10))
Br7.position(int(SCREEN_WIDTH * 7 / 10), int(SCREEN_HEIGHT * 2 / 10))
Br8.position(int(SCREEN_WIDTH * 7 / 10), int(SCREEN_HEIGHT * 5 / 10))
Br9.position(int(SCREEN_WIDTH * 7 / 10), int(SCREEN_HEIGHT * 8 / 10))
w1 = pygame.sprite.Group()
w2 = pygame.sprite.Group()
w3 = pygame.sprite.Group()
w4 = pygame.sprite.Group()
w5 = pygame.sprite.Group()
w6 = pygame.sprite.Group()
w7 = pygame.sprite.Group()
w8 = pygame.sprite.Group()
w9 = pygame.sprite.Group()
w1.add(Br1)
w2.add(Br2)
w3.add(Br3)
w4.add(Br4)
w5.add(Br5)
w6.add(Br6)
w7.add(Br7)
w8.add(Br8)
w9.add(Br9)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == INC_SPEED:
            B1.speed = B1.speed + 0.5 * 3
            B1.x_speed = B1.x_speed * (B1.speed) / (B1.speed - 0.5 * 3)
            B1.y_speed = B1.y_speed * (B1.speed) / (B1.speed - 0.5 * 3)
        if event.type == Change_Font:
            msg = phrases[count]
        count = count + 1
        if(count > 11):
            count = 0
    DIS.fill(BLACK)
    for entity in players:
        entity.move()
        DIS.blit(entity.image, entity.rect)
    if(check[0] == 0):
        DIS.blit(Br1.image, Br1.rect)
    if(check[1] == 0):
        DIS.blit(Br2.image, Br2.rect)
    if(check[2] == 0):
        DIS.blit(Br3.image, Br3.rect)
    if(check[3] == 0):
        DIS.blit(Br4.image, Br4.rect)
    if(check[4] == 0):
        DIS.blit(Br5.image, Br5.rect)
    if(check[5] == 0):
        DIS.blit(Br6.image, Br6.rect)
    if(check[6] == 0):
        DIS.blit(Br7.image, Br7.rect)
    if(check[7] == 0):
        DIS.blit(Br8.image, Br8.rect)
    if(check[8] == 0):
        DIS.blit(Br9.image, Br9.rect)
    B1.move()
    DIS.blit(B1.image, B1.rect)
    score_a = font.render(str(s_a), True, WHITE)
    DIS.blit(score_a, (SCREEN_WIDTH - 15 * 3, SCREEN_HEIGHT - 40 * 3))
    msg_render = font.render(msg, True, RED)
    DIS.blit(msg_render, (20 * 3, 20 * 3))
    if pygame.sprite.spritecollideany(B1, w1):
        B1.x_speed = B1.x_speed * -1
        Br1.image = pygame.image.load("image69.jpeg")
    if pygame.sprite.spritecollideany(B1, w2):
        B1.x_speed = B1.x_speed * -1
        Br2.image = pygame.image.load("image70.jpeg")
    if pygame.sprite.spritecollideany(B1, w3):
        B1.x_speed = B1.x_speed * -1
        Br3.image = pygame.image.load("image71.jpeg")
    if pygame.sprite.spritecollideany(B1, w4):
        B1.x_speed = B1.x_speed * -1
        Br4.image = pygame.image.load("image72.jpeg")
    if pygame.sprite.spritecollideany(B1, w5):
        B1.x_speed = B1.x_speed * -1
        Br5.image = pygame.image.load("image73.jpeg")
    if pygame.sprite.spritecollideany(B1, w6):
        B1.x_speed = B1.x_speed * -1
        Br6.image = pygame.image.load("image74.jpg")
    if pygame.sprite.spritecollideany(B1, w7):
        B1.x_speed = B1.x_speed * -1
        Br7.image = pygame.image.load("image75.jpg")
    if pygame.sprite.spritecollideany(B1, w8):
        B1.x_speed = B1.x_speed * -1
        Br8.image = pygame.image.load("image76.jpg")
    if pygame.sprite.spritecollideany(B1, w9):
        B1.x_speed = B1.x_speed * -1
        Br9.image = pygame.image.load("image77.jpg")
    
    if pygame.sprite.spritecollideany(B1, players):
        B1.x_speed = B1.x_speed * -1
    if pygame.sprite.spritecollideany(B1, players2):
        msg = phrases[count]
        count = count + 1
        if(count > 11):
            count = 0
    if B1.rect.left < 0:
        B1.x_speed = B1.x_speed * -1
    elif B1.rect.right > SCREEN_WIDTH:
        s_a += 1
        if(s_a == 10):
            DIS.fill(RED)
            message = font.render("Made by panduga,", True, BLACK)
            message2 = font.render("the idiots you don't need", True, BLACK)
            message3 = font.render("but the idiots you deserve", True, BLACK)
            DIS.blit(message, (10 * 3, 10 * 3))
            DIS.blit(message2, (10 * 3, 40 * 3))
            DIS.blit(message3, (10 * 3, 70 * 3))
            pygame.display.update()
            for entity in players:
                entity.kill()
                time.sleep(5)
            pygame.quit()
            sys.exit()
        else:
            DIS.fill(RED)
            asd = font.render("What was it this time?", True, BLACK)
            efg = font.render("Offline Ping Lag?", True, BLACK)
            DIS.blit(asd, (10 * 3, 20 * 3))
            DIS.blit(efg, (10 * 3, 150))
            pygame.display.update()
            time.sleep(2)
            P1.rect.x = 3 * 3
            P1.rect.y = SCREEN_HEIGHT / 2
            P2.rect.x = SCREEN_WIDTH - 15 * 3
            P2.rect.y = SCREEN_HEIGHT / 2
            B1.rect.x = SCREEN_WIDTH / 2
            B1.rect.y = SCREEN_HEIGHT / 2
            B1.set_speed()
            time.sleep(2)
    pygame.display.update()
    FramesPerSec.tick(FPS)
