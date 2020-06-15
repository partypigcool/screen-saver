import sys, pygame, random
from pygame.locals import *
import sys
from fish import *
pygame.init()
screen_info = pygame.display.Info()


size = (width, height) =(screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)


  



school = []
def main():
  for i in range(10):
    school.append(Fish((width/2, height/2)))

  while True:
    clock.tick(60)
    screen.fill(color)
    for x in school:
      x.update()
      x.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
  main()