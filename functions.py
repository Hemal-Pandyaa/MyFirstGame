import pygame
import random
pygame.font.init()

def getRandX(Total):
    return random.randint(0,Total)

def getRandY(Total):
    return random.randint(0,Total)

def renderText(text,color,background):
    Font = pygame.font.SysFont("Roboto",50)
    Text = Font.render(text,1,color,background)
    return Text

