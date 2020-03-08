import pygame
import time
import random

# always init pygame
pygame.init()

display_width = 800
display_height = 600
car_width = 73

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

carImg = pygame.image.load('racecar.png')
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("First game")
clock = pygame.time.Clock()  # specific game clock


class Thing:
    def __init__(self, thingx, thingy, thing_width,
                 thing_height, thing_speed, color):
        self.x = thingx
        self.y = thingy
        self.w = thing_width
        self.h = thing_height
        self.speed = thing_speed
        self.color = color

    def draw(self):
        pygame.draw.rect(game_display, self.color,
                         [self.x, self.y, self.w, self.h])


def thing_generator(count):
    things = []
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    for i in range(count):
        thing_startx = random.randrange(0, display_width)
        ran_color = (random.randrange(0, 255), random.randrange(0, 255),
                     random.randrange(0, 255))
        things.append(Thing(thing_startx, thing_starty, thing_width,
                            thing_height, thing_speed, ran_color))
    return things


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    game_display.blit(text, (0, 0))


def car(x, y):
    game_display.blit(carImg, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf", 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (display_width/2, display_height/2)
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_vel = 5

    dodged = 0
    thing_freq = 4
    thing_count = thing_freq
    things = thing_generator(int(thing_count/thing_freq))

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            x -= x_vel
        elif key_pressed[pygame.K_RIGHT]:
            x += x_vel

        game_display.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        for thing in things:
            thing.draw()
            thing.y += thing.speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if things[0].y > display_height:
            dodged += int(thing_count/thing_freq)
            thing_count += 1
            things = thing_generator(int(thing_count/thing_freq)
            # thing_speed += 1
            # thing_width += (dodged * 1.2)

        for thing in things:
            if y < thing.y + thing.h:
                if x > thing.x and x < thing.x + thing.w or x + car_width > thing.x and x + car_width < thing.x + thing.w:
                    crash()

        pygame.display.flip()
        clock.tick(120)  # frames per second


game_loop()
pygame.quit()
quit()
