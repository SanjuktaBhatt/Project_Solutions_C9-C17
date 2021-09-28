import pygame
pygame.init() 
johnx=190
johny=150
size = (400, 400)
screen = pygame.display.set_mode(size)

# Load the bedroom image and store in 'bedroom' variable
bedroom=pygame.image.load("Assets/room.png").convert()
# Scale the bedroom image and store in 'bedroom_scaled' variable
bedroom_scaled=pygame.transform.smoothscale(bedroom,(600,400))
# Load john's childhood image and store in 'john' variable
john=pygame.image.load("Assets/john.png").convert_alpha()
# Scale john's childhood image and store in 'john_scaled' variable 
john_scaled=pygame.transform.smoothscale(john,(300,300))

pygame.display.set_caption("Project C10")
#Create "carryOn" variable and set to true
carryOn = True
#Begin the while loop
while carryOn:
  #Iterate through each event
  for event in pygame.event.get():
    #Identify is user has quit 
    if event.type == pygame.QUIT: 
      #change "carryOn" to False
      carryOn = False 
  screen.blit(bedroom_scaled,(0,0))
  if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
                johnx-=5
  screen.blit(john_scaled,(johnx,johny))
  pygame.display.flip()
pygame.quit()
