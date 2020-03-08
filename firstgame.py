import pygame

# always init pygame
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

carImg = pygame.image.load('racecar.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("First game")
clock = pygame.time.Clock() # specific game clock

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False
while not crashed:
    # makes sure things do not happen to quick
    pygame.time.delay(100)
    # check for event with for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill(white)
    #car(x, y)
    pygame.display.update()
    clock.tick(60) # frames per second
pygame.quit()
quit()
