import pygame, sys
from pygame.locals import *

#key I, G, R, L, Q, W, S

Picture = pygame.image.load("MonaLisa.jpg")
Picture2 = pygame.image.load("Stars.jpg")
Running = True
pygame.init()

Width = 400
Height = 536
screen = pygame.display.set_mode((Width, Height))

screen.blit(Picture, (0, 0))
pygame.display.update()
pxarray2 = pygame.PixelArray(screen)
pxarray = pygame.PixelArray(screen)

#Inverts the colours
def Invert():
    y = 0

    for x in xrange (Width):
        X = 0
        for x in xrange (Height):
            RGBint = pxarray[y,X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

            Blue = 255 - Blue
            Green = 255 - Green
            Red = 255 - Red

            pxarray[y, X] = (Red, Green, Blue)
            X = X + 1
        y = y + 1

    pygame.display.update()

#Greyscale
def GreyScale():
    y = 0

    for x in xrange(Width):
        X = 0
        for x in xrange(Height):
            RGBint = pxarray[y, X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

            grey = (Red + Green + Blue)/3

            pxarray[y, X] = (grey, grey, grey)
            X = X + 1
        y = y + 1

    pygame.display.update()

#halves all the red values
def LessRed():
    y = 0

    for x in xrange(Width):
        X = 0
        for x in xrange(Height):
            RGBint = pxarray[y, X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

            pxarray[y, X] = (Red/2, Green, Blue)
            X = X + 1
        y = y + 1

    pygame.display.update()

def ColourTest():
    ColourChange = 0
    Gradient = 1.25
    y = 0
    for x in xrange (Width):
        X = 0
        for x in xrange (Height):
            RGBint = pxarray[y,X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

            if Red > 25 and Green > 25 and Blue > 25:
                Red =  0
                Green = ColourChange
                Blue =  ColourChange/2
            else:
                Red =255
                Green =255 - ColourChange
                Blue = 255 - ColourChange/2
            pxarray[y, X] = (Red, Green, Blue)
            X = X + 1
        y = y + 1
        ColourChange = ColourChange + Gradient
        if ColourChange == 255:
            Gradient = -1.25
        elif ColourChange == 0:
            Gradient = 1.25
    pygame.display.update()

def HUEHUEHUE():
    ColourChange = 0
    y = 0
    for x in xrange (Width):
        X = 0
        for x in xrange (Height):
            RGBint = pxarray[y,X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

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
            pxarray[y, X] = (Red, Green, Blue)
            X = X + 1
        y = y + 1
    pygame.display.update()



def WoodTex():
    ColourChange = 0
    y = 0
    for x in xrange (Width):
        X = 0
        for x in xrange (Height):
            RGBint = pxarray[y,X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

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
            pxarray[y, X] = (Red, Green, Blue)
            X = X + 1
        y = y + 1
    pygame.display.update()


def Spooky():
    ColourChange = 0
    y = 0
    for x in xrange (Width):
        X = 0
        for x in xrange (Height):
            RGBint = pxarray[y,X]
            Blue = RGBint & 255
            Green = (RGBint >> 8) & 255
            Red = (RGBint >> 16) & 255

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
            pxarray[y, X] = (Red, Green, Blue)
            X = X + 1
        y = y + 1
    pygame.display.update()

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

