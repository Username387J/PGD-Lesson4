import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

pos=(50,50)
class Rect:
    def __init__(self,color,position,size,thick):
        self.screen = screen
        self.color = color
        self.position = position
        self.size = size
        self.thick = thick

    def drawRect(self):
        pygame.draw.rect(self.screen,self.color,(*self.position,*self.size),self.thick)

redRect=Rect("red",pos,(100,100),1)
redRect.drawRect()
orangeRect=Rect("orange",pos,(130,130),2)
orangeRect.drawRect()
yellowRect=Rect("yellow",pos,(160,160),3)
yellowRect.drawRect()
greenRect=Rect("green",pos,(190,190),4)
greenRect.drawRect()
blueRect=Rect("blue",pos,(210,210),5)
blueRect.drawRect()


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()