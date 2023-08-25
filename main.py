import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((800,600))

running = True

font = pygame.font.SysFont('Arial',32,'bold')

def score_text():
    img=font.render(f'Score:{score}',True,'white')
    screen.blit(img,(10,10))

font_gameover = pygame.font.SysFont('Arial',64,'bold')

def gameOver():
    imgGameOver = font_gameover.render('GAME OVER',True,'white')
    screen.blit(imgGameOver,(200,250))


pygame.display.set_caption('Space Shooter Game')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('bg.png')
background = pygame.transform.scale(background,(800,600))
spaceshipimg = pygame.image.load('arcade.png')

alienimg = []
alienX = []
alienY = []
alienSpeedX = []
alienSpeedY = []

noOfAliens = 6

for i in range(noOfAliens):
    alienimg.append(pygame.image.load('enemy.png'))
    alienX.append(random.randint(0,736))
    alienY.append(random.randint(30,150))
    alienSpeedX.append(-.2)
    alienSpeedY.append(40)

score = 0

bulletimg = pygame.image.load('bullet.png')
check = False
bulletX = 386
bulletY = 490
spaceshipX = 370
spaceshipY = 480
changeX = 0


while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -.2
            if event.key == pygame.K_RIGHT:
                changeX = .2
            if event.key == pygame.K_SPACE:
                if check is False:
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    check = True
                    bulletX = spaceshipX+16
        if event.type == pygame.KEYUP:
                changeX = 0
    spaceshipX+=changeX #spaceshipX= spaceshipX + changeX
    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736
    for i in range(noOfAliens):
        if alienY[i] > 420:
            for j in range(noOfAliens):
                alienY[j] = 2000
            gameOver()
            break
        alienX[i] += alienSpeedX[i]
        if alienX[i] <= 0:
            alienSpeedX[i] = .2
            alienY[i] += alienSpeedY[i]
        elif alienX[i] >= 736:
            alienSpeedX[i] = -.2
            alienY[i] += alienSpeedY[i]

        distance = math.sqrt( math.pow(bulletX-alienX[i],2) + math.pow(bulletY-alienY[i],2))
        if distance < 27:
            explosion = mixer.Sound('explosion.wav')
            explosion.play()
            bulletY = 480
            check = False
            alienX[i] = random.randint(0,736)
            alienY[i] = random.randint(30,150)
            score += 1
        screen.blit(alienimg[i], (alienX[i],alienY[i]))
    if bulletY <= 0:
        bulletY = 490
        check = False
    if check:
        screen.blit(bulletimg,(bulletX,bulletY))
        bulletY -= .5

    screen.blit(spaceshipimg, (spaceshipX,spaceshipY))

    score_text()
    pygame.display.update()












