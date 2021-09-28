import pygame
pygame.init()
class Student:
  def __init__(self,name,grade,teacher,rollnumber,photo):
    self.name=name
    self.grade=grade
    self.teacher=teacher
    self.rollnumber=rollnumber
    self.photo=photo

  def display(self,screen):
    font = pygame.font.Font(None, 34)
    name_text = font.render("Name: "+self.name, 1, (255,255,0))
    screen.blit(name_text, (200,10))
    grade_text=font.render("Grade: "+self.grade, 1, (0,255,0))
    screen.blit(grade_text, (200,40))
    teacher_text=font.render("Teacher: "+self.teacher, 1, (0,255,255))
    screen.blit(teacher_text, (200,70))
    roll_text=font.render("Roll.No.: "+self.rollnumber, 1, (255,0,255))
    screen.blit(roll_text, (200,100))
    screen.blit(self.photo,(50,10))

              
screen = pygame.display.set_mode((400,200))
pygame.display.set_caption("Project C14")
photo=pygame.image.load("Assets/photo.JPG").convert()
photo_scaled=pygame.transform.smoothscale(photo,(100,100))
myself=Student("San","11","Mary","5",photo_scaled)
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False 
  screen.fill((255,255,255))
  myself.display(screen)
  pygame.display.flip()


pygame.quit()



