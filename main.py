import pygame
from pygame.locals import *

pygame.init()
size = 1000, 900
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('test')

#################################
spriteRight = pygame.image.load('C://Users//Dylan//PycharmProjects//pypro//sprite folder//1.png')


##############################
class player(object):
    def __init__(self, x, y):
        self.count = 0
        self.counterpower = 0
        self.x = x
        self.y = y
        self.game1 = True
        self.walkcount = 0
        self.Right = False
        self.Left = False
        self.jump = False
        self.jumpcount = 10
        self.count = 0
        self.startgame = True

    def game(self, screen):
        if self.walkcount >= 1:
            self.counterpower = 0
        if self.Right:
            screen.blit(spriteRight, (self.x, self.y))
        elif self.Left:
            screen.blit(spriteRight, (self.x, self.y))
        else:
            screen.blit(spriteRight, (self.x, self.y))
        self.walkcount += 1

    pygame.display.update()


man = player(90, 90)
run = True
while run:
    if man.startgame:
        if man.y < 740:
            man.y += 10
        else:
            man.startgame = False

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        man.x -= 5
        man.Left = True
    elif keys[pygame.K_RIGHT]:
        man.x += 5
        man.Right = True
    elif keys[pygame.K_SPACE]:
        man.jump = True

    else:
        man.walkcount = 0

    man.game(screen)

    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(30)
# test
