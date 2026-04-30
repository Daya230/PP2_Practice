"""
import pygame

pygame.init() #импортурет массу других расширений
pygame.display.set_caption("My first programm")
clock = pygame.time.Clock()
FPS = 60

W, H = 1200 , 800
sr = pygame.display.set_mode((W, H), pygame.RESIZABLE | pygame.DOUBLEBUF)
WHITE = (255,255, 255)
pygame.draw.line(sr, WHITE , (200,100), (1200,40)) # pygame.draw.line(экран, (настройка цвета), начальная позиция точки, конечная позиция линии, ширина линии)
pygame.draw.rect(sr , WHITE, (80,80,1000,10)) # pygame.draw.rect(экран, (настройка цвета), (х, y, a , b), optional:граница)
pygame.display.flip()
flag = True
while flag:
    for event in pygame.event.get(): #
        if event.type == pygame.QUIT:
            pygame.quit() #выход из цикла программы
            flag = False 
    clock.tick(FPS)
#event.type == pygame.KEYUP // type тип данныхя, которое оно получило от event.get
print("program")
"""
"""
import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

W, H = 1200, 800
x, y = W // 2, H // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

direct = 5
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE | pygame.DOUBLEBUF)
move = 0


flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and event.mod == pygame.KMOD_LCTRL:
        x -= direct
    elif keys[pygame.K_RIGHT] and event.mod == pygame.KMOD_LCTRL:
        x += direct
    elif keys[pygame.K_UP]:
        y-=direct
    elif keys[pygame.K_DOWN]:
        y+=direct    
        

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLACK, (x, y, 10, 20))

    pygame.display.update()
    clock.tick(FPS)

    if flleft:
        x -= direct
    if flright:
        x += direct


"""
"""

import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

W, H = 1200,800

pygame.display.set_caption("Button cursor")
pygame.display.set_mode((W,H), pygame.RESIZABLE | pygame.DOUBLEBUF )


#RGB
WRITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Button was pressed: ", event.button)
        elif event.type == pygame.MOUSEMOTION:
            print("Motion: ", event.rel)
    clock.tick(FPS)
"""
"""
import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

W, H = 1200, 800

WHITE = (255,255,255)
RED = (255,0,0)

pygame.display.set_caption("Paint")
sc = pygame.display.set_mode((W,H), pygame.RESIZABLE | pygame.DOUBLEBUF)

FlStartDraw = False
sp = None

sc.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            FlStartDraw = True
            sp = event.pos

        elif event.type == pygame.MOUSEMOTION and FlStartDraw:
            pos = event.pos

            width = pos[0] - sp[0]
            height = pos[1] - sp[1]

            sc.fill(WHITE)
            pygame.draw.rect(sc, RED, (sp[0], sp[1], width, height))
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            FlStartDraw = False

    clock.tick(FPS)
"""

import pygame

pygame.init()

W,H = 1200,800
sc = pygame.display.set_mode((W,H), pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("get pressed")


#RGB
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


clock = pygame.time.Clock()
FPS = 60 

sp = None

sc.fill(WHITE)
pygame.display.update()

pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            pos = pygame.mouse.get_pos()
            if sp is None:
                sp = pos
            x = min(sp[0], pos[0])
            y = min(sp[1], pos[1])
            width = abs(pos[0] - sp[0])
            height = abs(pos[1] - sp[1])


            sc.fill(WHITE)
            pygame.draw.rect(sc, RED, pygame.Rect(x, y, width, height))
            pygame.display.update()
        else:
            sp= None
            