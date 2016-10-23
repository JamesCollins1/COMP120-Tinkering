import pygame, sys
from pygame.locals import *

#key I, G, R, L, Q, W, S

Picture = pygame.image.load("MonaLisa.jpg")
Picture2 = pygame.image.load("Stars.jpg")
Running = True
pygame.init()

Width = 400
Height = 500

Screen = pygame.display.set_mode((Width, Height))
Picture =pygame.transform.scale(Picture, (Width,Height))
Screen.blit(Picture, (0, 0))
pygame.display.update()

PXArray2 = pygame.PixelArray(Screen)
PXArray = pygame.PixelArray(Screen)

#Inverts the colours
def Invert():

    for Y in range(0, Height):
        for X in range(0, Width):

            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            Red = 255 - Red
            Green = 255 - Green
            Blue = 255 - Blue

            PXArray[X, Y] = (Red, Green, Blue)

    pygame.display.update()

#Greyscale
def GreyScale():

    for Y in xrange(Height):
        for X in xrange(Width):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            grey = (Red + Green + Blue)/3

            PXArray[X, Y] = (grey, grey, grey)

    pygame.display.update()

#halves all the red values
def LessRed():

    for Y in xrange(Height):
        for X in xrange(Width):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            PXArray[X, Y] = (Red/2, Green, Blue)

    pygame.display.update()

def ColourTest():
    ColourChange = 0
    Gradient = 1.25
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                Red =  0
                Green = ColourChange
                Blue =  ColourChange/2
            else:
                Red =255
                Green =255 - ColourChange
                Blue = 255 - ColourChange/2
            PXArray[X, Y] = (Red, Green, Blue)
        ColourChange = ColourChange + Gradient
        if ColourChange == 255:
            Gradient = -1.25
        elif ColourChange == 0:
            Gradient = 1.25
    pygame.display.update()

#Interesting affect
def HUEHUEHUE():
    ColourChange = 0
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange = ColourChange + 1
            else:
                ColourChange = ColourChange - 1
            Red = Red + ColourChange
            Green = Green + ColourChange
            Blue = Blue + ColourChange
            if ColourChange > 150:
                ColourChange = 0
            if ColourChange < -0:
                ColourChange = 150

            if Red > 255:
                Red = 255
            elif Red < 0:
                Red = 0
            if Green > 255:
                Green = 255
            elif Green < 0:
                Green = 0
            if Blue > 255:
                Blue = 255
            elif Blue < 0:
                Blue = 0
            PXArray[X, Y] = (Red, Green, Blue)
    pygame.display.update()


#Somehow it makes a wood texture, dont ask how
def WoodTex():
    ColourChange = 0
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange = ColourChange + 1
                Red = Red + ColourChange
                Green = Green + ColourChange
                Blue = Blue + ColourChange
            else:
                ColourChange = ColourChange - 1
                Red = Red - ColourChange
                Green = Green - ColourChange
                Blue = Blue - ColourChange
            if ColourChange > 150:
                ColourChange = 0
            if ColourChange < -0:
                ColourChange = 150

            if Red > 255:
                Red = 255
            elif Red < 0:
                Red = 0
            if Green > 255:
                Green = 255
            elif Green < 0:
                Green = 0
            if Blue > 255:
                Blue = 255
            elif Blue < 0:
                Blue = 0
            PXArray[X, Y] = (Red, Green, Blue)

    pygame.display.update()

#2spooky5u white fade ghostly effect
def Spooky():
    ColourChange = 0
    for X in xrange (Width):
        for Y in xrange (Height):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            if Red > 25 and Green > 25 and Blue > 25:
                ColourChange = ColourChange + 1
            else:
                ColourChange = ColourChange - 1
            Red = Red + ColourChange
            Green = Green + ColourChange
            Blue = Blue + ColourChange
            if ColourChange > 150:
                ColourChange = 150
            if ColourChange < 0:
                ColourChange = 0

            if Red > 255:
                Red = 255
            elif Red < 0:
                Red = 0
            if Green > 255:
                Green = 255
            elif Green < 0:
                Green = 0
            if Blue > 255:
                Blue = 255
            elif Blue < 0:
                Blue = 0
            PXArray[X, Y] = (Red, Green, Blue)

    pygame.display.update()

#Press the keys and it does stuff
while Running:
    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            Running = False
        if event.type == KEYDOWN and event.key == K_i:
            Invert()
        if event.type == KEYDOWN and event.key == K_g:
            GreyScale()
        if event.type == KEYDOWN and event.key == K_r:
            LessRed()
        if event.type == KEYDOWN and event.key == K_l:
            ColourTest()
        if event.type == KEYDOWN and event.key == K_q:
            HUEHUEHUE()
        if event.type == KEYDOWN and event.key == K_w:
            WoodTex()
        if event.type == KEYDOWN and event.key == K_s:
            Spooky()
pygame.quit()
sys.exit()

