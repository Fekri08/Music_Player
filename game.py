#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, random, time
import pygame.mixer
pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
zeleniy1 = (0,255,0)
zeleniy2 = (0,255,0)

zen = 0
screen = pygame.display.set_mode((512, 256))

pygame.display.set_icon(pygame.image.load('images/logo.ico'))
bg1 = pygame.image.load('images/play.png')
pygame.display.set_caption("Time Killer")
plays = pygame.image.load("images/play.png")
plays.set_colorkey((255, 255, 255))
gear = pygame.image.load("images/minus.png")
gear.set_colorkey((255, 255, 255))

clock = pygame.time.Clock()
SOUND_FILE = r"C:\Users\FMA\OneDrive - Ministere de l'Enseignement Superieur et de la Recherche Scientifique\Music\Ariana Grande\Greedy\Greedy - Ariana Grande.mp3"

pygame.mixer.music.load(SOUND_FILE)
pygame.mixer.music.play()

def games():
    pygame.mixer.music.stop()

    zelen = 0

    x = 10
    y = 225
    speed = 12

    hero = pygame.image.load("images/mute.png")
    frukt = pygame.image.load("images/next.png")
    hphero = pygame.image.load("images/pause.png")

    fmax = 495
    fmin = 0

    rlift = False
    rright = False

    sgame = True
    clock = pygame.time.Clock()

    def herowin():
        screen.blit(bg1, (0, 0))
        pygame.display.update()

        font11 = pygame.font.Font(None, 20)
        text11 = font11.render(u"Вы победили!", True, black)
        screen.blit(text11, [10, 10])
        pygame.display.update()
        time.sleep(3.0)
        pygame.quit()
        exit()

    #Музыка в игре
    pygame.mixer.music.load(SOUND_FILE)
    pygame.mixer.music.play()

    zen = 0 #y
    spawn1x = random.randint(0, 490) #x
    spawn2x = random.randint(0, 490)
    spawn3x = random.randint(0, 490)
    spawn4x = random.randint(0, 490)
    spawn5x = random.randint(0, 490)
    spawn6x = random.randint(0, 490)
    spawn7x = random.randint(0, 490)
    spawn8x = random.randint(0, 490)
    spawn9x = random.randint(0, 490)
    spawn10x = random.randint(0, 490)

    while sgame:
        font1 = pygame.font.Font(None, 25)
        text1 = font1.render(u"Собрано зелени:" + str(zelen) + "/10", True, black)

        #Контрольные точки
        #Герой
        pos1 = x
        pos2 = x + 20
        #Враг
        var1 = spawn1x + 20
        var2 = spawn2x + 20
        var3 = spawn3x + 20
        var4 = spawn4x + 20
        var5 = spawn5x + 20
        var6 = spawn6x + 20
        var7 = spawn7x + 20
        var8 = spawn8x + 20
        var9 = spawn9x + 20
        var10 = spawn10x + 20

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sgame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sgame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    rright = True
                elif event.key == pygame.K_a:
                    rlift = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    rright = False
                elif event.key == pygame.K_a:
                    rlift = False

        if x == fmax or x > fmax:
            rright = False
            x = 495

        if x == fmin or x < fmin:
            rlift = False
            x = 0

        if rright == True:
            x += speed

        if rlift == True:
            x -= speed

        if zen == 225 or zen > 225:
            spawn1x = random.randint(0, 490)
            spawn2x = random.randint(0, 490)
            spawn3x = random.randint(0, 490)
            spawn4x = random.randint(0, 490)
            spawn5x = random.randint(0, 490)
            spawn6x = random.randint(0, 490)
            spawn7x = random.randint(0, 490)
            spawn8x = random.randint(0, 490)
            spawn9x = random.randint(0, 490)
            spawn10x = random.randint(0, 490)

            zen = 0
        zen += 10

    #Отслеживание сталкновения
        if zen > 215 and pos1 < spawn1x < pos2 or zen > 215 and pos1 < var1 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn2x < pos2 or zen > 215 and pos1 < var2 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn3x < pos2 or zen > 215 and pos1 < var3 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn4x < pos2 or zen > 215 and pos1 < var4 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn5x < pos2 or zen > 215 and pos1 < var5 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn6x < pos2 or zen > 215 and pos1 < var6 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn7x < pos2 or zen > 215 and pos1 < var7 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn8x < pos2 or zen > 215 and pos1 < var8 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn9x < pos2 or zen > 215 and pos1 < var9 < pos2:
            pygame.mixer.music.stop()
            sgame = False

        if zen > 215 and pos1 < spawn10x < pos2 or zen > 215 and pos1 < var10 < pos2:
            zelen += 1
            spawn10x = random.randint(0, 490)

        if zelen == 10 or zelen > 10:
            herowin()

        clock.tick(20)
        screen.blit(bg1, (0, 0))
        screen.blit(hero, (x, y))
        screen.blit(text1, [5, 5])
        screen.blit(frukt, (spawn1x, zen + 10))
        screen.blit(frukt, (spawn2x, zen + 15))
        screen.blit(frukt, (spawn3x, zen + 20))
        screen.blit(frukt, (spawn4x, zen + 25))
        screen.blit(frukt, (spawn5x, zen + 30))
        screen.blit(frukt, (spawn6x, zen + 35))
        screen.blit(frukt, (spawn7x, zen + 40))
        screen.blit(frukt, (spawn8x, zen + 45))
        screen.blit(frukt, (spawn9x, zen + 50))
        screen.blit(hphero, (spawn10x, zen + 55))
        pygame.display.update()

def options():
    red = (255, 0, 0)
    zeleniy1 = (0,255,0)
    zeleniy2 = (0,255,0)
    opti =True
    while opti:

        font31 = pygame.font.Font(None, 35)
        text31 = font31.render(u"q - Назад", True, red)

        font32 = pygame.font.Font(None, 35)
        text32 = font32.render(u"w - Старт", True, red)

        font34 = pygame.font.Font(None, 35)
        text34 = font34.render(u"s - Настройки", True, red)

        font35 = pygame.font.Font(None, 35)
        text35 = font35.render(u"a - Движ. в лево", True, red)

        font36 = pygame.font.Font(None, 35)
        text36 = font36.render(u"d - Движ. в право", True, red)

        font33 = pygame.font.Font(None, 35)
        text33 = font33.render(u"<-Назад", True, red)

        ss = (255,0,0)
        sss = (0,255,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opti = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    opti = False
                if event.key == pygame.K_q:
                    opti = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 15 and pygame.mouse.get_pos()[1] >= 210:
                    if pygame.mouse.get_pos()[0] <= 135 and pygame.mouse.get_pos()[1] <= 240:
                        opti = False

        clock.tick(20)
        screen.blit(bg1, (0, 0))
        screen.blit(text31, [10, 20])
        screen.blit(text32, [10, 100])
        screen.blit(text33, [10, 210])
        screen.blit(text34, [10, 40])
        screen.blit(text35, [10, 60])
        screen.blit(text36, [10, 80])
        #start_button2 = pygame.draw.rect(screen,ss,(15,210,120,30));#3
        pygame.display.update()

def upgrate():
    clock.tick(20)
    screen.blit(bg1, (0, 0))
    screen.blit(plays, (20, 25))
    screen.blit(gear, (250, 0)) #256X256
#    start_button = pygame.draw.rect(screen,(0,0,240),(20,25,200,200));
#    start_button2 = pygame.draw.rect(screen,(0,0,240),(280,25,200,200));
    pygame.display.update()

pygame.display.flip();

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_w:
                games()
            if event.key == pygame.K_s:
                options()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 25:
                if pygame.mouse.get_pos()[0] <= 220 and pygame.mouse.get_pos()[1] <= 225:
                    games()

            if pygame.mouse.get_pos()[0] >= 280 and pygame.mouse.get_pos()[1] >= 25:
                if pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] <= 225:
                    options()

    upgrate()

pygame.quit()
exit()