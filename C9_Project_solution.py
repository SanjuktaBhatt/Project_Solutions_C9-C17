import pygame
pygame.init() 

size = (400, 400)
screen = pygame.display.set_mode(size)

# Load the bedroom image location
bedroom=pygame.image.load("Assets/Bedroom.png").convert()
# Scale the bedroom image to size (600, 400) 
bedroom_scaled=pygame.transform.smoothscale(bedroom,(600,400))
# Load the john_childhood image location 
john=pygame.image.load("Assets/john_childhood.PNG").convert_alpha()
# Scale john's image to size (100, 200) 
john_scaled=pygame.transform.smoothscale(john,(100,200))

pygame.display.set_caption("Project C9")
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
  # Display scaled bedroom image at (-15, 0)
  screen.blit(bedroom_scaled,(-15,0))
  # Display scaled john's image at (150, 100)
  screen.blit(john_scaled,(150,100))
  pygame.display.flip()
pygame.quit()
