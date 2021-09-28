import pygame
pygame.init()
def create_building(height,x,y,r,g,b,windows):
  building=pygame.Rect(x,y,60,height)
  pygame.draw.rect(screen,(r,g,b),building)
  door=pygame.Rect(x+15,340,30,100)
  pygame.draw.rect(screen,(0,0,0),door)
  for i in range(1,windows+1):
    window=pygame.Rect(x+20,50*i+60,20,20)
    pygame.draw.rect(screen,(255,255,0),window)
  




screen = pygame.display.set_mode((300,400))
pygame.display.set_caption("Project C13")

carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False 
  screen.fill((36,90,190))
  create_building(400,100,100,255,0,0,4)
  
    
  pygame.display.flip()
    
pygame.quit()
