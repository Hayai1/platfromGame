import pygame
from pygame.locals import *

pygame.init()
size = 1000, 900
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('test')

#################################
spriteRightImg = pygame.image.load('C://Users//Dylan//PycharmProjects//pypro//sprite folder//1.png')
cursorImg = pygame.image.load('C://Users//Dylan//PycharmProjects//pypro//sprite folder//Cursor.png')


##############################
class player(object):
    def __init__(self, x, y):
        self.count = 0
        self.counterPower = 0
        self.x = x
        self.y = y
        self.game1 = True
        self.walkCount = 0
        self.Right = False
        self.Left = False
        self.jump = False
        self.jumpCount = 10.0
        self.count = 0
        self.startGame = True
        self.startPos = 0

    def draw(self, screen, spirter):
        if self.walkCount >= 1.0:
            self.counterPower = 0.0
        if self.Right:
            screen.blit(spirter, (self.x, self.y))
        elif self.Left:
            screen.blit(spirter, (self.x, self.y))
        else:
            screen.blit(spirter, (self.x, self.y))
        self.walkCount += 1

    pygame.display.update()


man = player(90, 90)
cursor = player(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
run = True
pygame.mouse.set_visible(False)
while run:
    cursor.x = pygame.mouse.get_pos()[0]
    cursor.y = pygame.mouse.get_pos()[1]
    if man.startGame:
        if man.y < 740:
            man.y += 10
        else:
            man.startGame = False

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        man.x -= 5
        man.Left = True
    if keys[pygame.K_RIGHT]:
        man.x += 5
        man.Right = True
    if keys[pygame.K_SPACE]:
        man.jump = True
    else:
        man.walkCount = 0

    if man.jump:
        if man.jumpCount == 10:
            man.startPos = man.y
        neg = 0
        # moving up
        if man.jumpCount > 0:
            neg = 1
        # moving down
        if man.jumpCount < 0:
            neg = -1
        man.y -= ((man.jumpCount ** 2) * 0.5) * neg
        man.jumpCount -= 1
        if man.y >= man.startPos:
            man.jumpCount = 10
            man.jump = False
            man.y = man.startPos

    man.draw(screen, spriteRightImg)
    cursor.draw(screen, cursorImg)
    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(240)
# test
