\import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))

black= (0,0,0)
red= (255,0,0)
green=(0,255,0)
blue=(0,0,255)
pink=(255,190,203)
white=(255,255,255)

screen.fill(white)

position=(300,300)
radius=50
wid=2

pygame.draw.circle(screen,red,position,radius,wid)
pygame.display.update()

class Circle:
    def __init__(self,color,position,rad,wid=0):
        self.color=color
        self.position=position
        self.rad=rad
        self.screen=screen
        self.wid=wid

    def drawCircle(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.rad,self.wid)
    
    def grow(self,r):
        self.rad = self.rad+r
        pygame.draw.circle(self.screen,self.color,self.position,self.rad,self.wid)

blueCircle=Circle(blue,position,radius+90,4)
redCircle=Circle(red,position,radius+50,3)
greenCircle=Circle(green,position,radius+70,2)
pinkCircle=Circle(pink,position,radius+60,1)  


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#Mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            blueCircle.drawCircle()
            redCircle.drawCircle()
            greenCircle.drawCircle()
            pinkCircle.drawCircle()
            pygame.display.update()
#mouse is released            
        if event.type == pygame.MOUSEBUTTONUP:
            blueCircle.grow(2)
            redCircle.grow(2)
            greenCircle.grow(2)
            pinkCircle.grow(2)
            pygame.display.update()
#mouse is moving            
        if event.type == pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            blackCircle=Circle(black,pos,5)
            blackCircle.drawCircle()
            pygame.display.update()



        


