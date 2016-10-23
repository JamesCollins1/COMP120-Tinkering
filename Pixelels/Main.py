import pygame, sys, math
from pygame.locals import *

#key I, G, R, L, W, S, C

Picture = pygame.image.load("Parrots.jpeg")

Running = True
pygame.init()

Width = 850   #Change these depending on the picture
Height = 480

Screen = pygame.display.set_mode((Width, Height))
Picture =pygame.transform.scale(Picture, (Width,Height))   #Scales the picture to fit the screen
Screen.blit(Picture, (0, 0))
pygame.display.update()

PXArray = pygame.PixelArray(Screen)

White = (255, 255, 255)
Black = (0,0,0)
Brown = (150, 80, 50)

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

#does weird stuff, dont trust this one
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

#Checks the distance between two colours, if the colours are within the tolerance it will return true
def ColourDistanceCheck(Colour1, Colour2, Tolerance):

   (Red1, Green1, Blue1) = Colour1
   (Red2, Green2, Blue2) = Colour2

   ColourDistance = math.sqrt(((Red1 - Red2) ** 2) + ((Green1 - Green2) ** 2) + ((Blue1 - Blue2) ** 2))
   if ColourDistance < Tolerance:
       return True
   else:
       return False


#if A pixel is close to input Colour (brown) it will half the red value of that pixel
def CloseEnough(Colour):
    for Y in range(0, Height):
        for X in range(0, Width):

            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            CurrentColour = (Red, Green, Blue)
            CloseBrown = False

            CloseBrown = ColourDistanceCheck(CurrentColour,Colour, 150)

            if CloseBrown:
                PXArray[X, Y] = ((Red / 2), Green, Blue)
            else:
                PXArray[X, Y] = (Red, Green, Blue)

    pygame.display.update()

#Posterizes the picture, level of Posterizsation depends on the ColourVariance
def Posterize(ColourVariance):
    ColourVariance = (255 / ColourVariance)

    for Y in range(0, Height):
        for X in range(0, Width):
            Red = Screen.get_at((X, Y)).r
            Green = Screen.get_at((X, Y)).g
            Blue = Screen.get_at((X, Y)).b

            Red = ColourPolz(Red,ColourVariance)
            Green = ColourPolz(Green, ColourVariance)
            Blue = ColourPolz(Blue, ColourVariance)

            PXArray[X, Y] = (Red, Green, Blue)
    pygame.display.update()


#Posterizes each colour, Used in the Posterize function

def ColourPolz(Colour,ColourVariance):
    ColourCounter = 255
    while True:
        if ColourCounter < 0:
            ColourCounter = 0
        if Colour >= ColourCounter:
            return ColourCounter
        else:
            ColourCounter = ColourCounter - ColourVariance

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
        if event.type == KEYDOWN and event.key == K_w:
            WoodTex()
        if event.type == KEYDOWN and event.key == K_s:
            Spooky()
        if event.type == KEYDOWN and event.key == K_c:
            CloseEnough(Brown) # Can choose any colour
        if event.type == KEYDOWN and event.key == K_p:
            Posterize(3)  # Try changing the value to alter the amount of posterization
pygame.quit()
sys.exit()

