import pygame
import time
import random

time.sleep(1)

pygame.init()
crash_sound = pygame.mixer.Sound("crash.wav")
vehicle_speed = 5         # Default speed of the car
max_speed = 15            # Maximum speed allowed
min_speed = 2             # Minimum speed allowed
speed_increment = 1       # Speed change per key press



#############

#############

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

crash_sound = pygame.mixer.Sound("crash.mp3")

vehicle_width = 55

play_surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Dodge Game')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('vehicleIcon.png')

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
play_surface.blit(backgroundImage, (0, 0))

vehicleImg = pygame.image.load("racevehicle.png")
vehicleImg = pygame.transform.scale(vehicleImg, (60, 100)) # resize graphic
vehicleImg = vehicleImg.convert_alpha() # remove whitespace from graphic

vehicle1 = pygame.image.load("diablo.png")
vehicle1 = pygame.transform.scale(vehicle1, (60, 100)) # resize graphic
vehicle1 = vehicle1.convert_alpha() # remove whitespace from graphic

vehicle2 = pygame.image.load("aventador.png")
vehicle2 = pygame.transform.scale(vehicle2, (60, 100)) # resize graphic
vehicle2 = vehicle2.convert_alpha() # remove whitespace from graphic

vehicle3 = pygame.image.load("nsx.png")
vehicle3 = pygame.transform.scale(vehicle3, (60, 100)) # resize graphic
vehicle3 = vehicle3.convert_alpha() # remove whitespace from graphic

vehicle4 = pygame.image.load("speeder.png")
vehicle4 = pygame.transform.scale(vehicle4, (60, 100)) # resize graphic
vehicle4 = vehicle4.convert_alpha() # remove whitespace from graphic

vehicle5 = pygame.image.load("slr.png")
vehicle5 = pygame.transform.scale(vehicle5, (60, 100)) # resize graphic
vehicle5 = vehicle5.convert_alpha() # remove whitespace from graphic

vehicle6 = pygame.image.load("Mach6.png")
vehicle6 = pygame.transform.scale(vehicle6, (60, 100)) # resize graphic
vehicle6 = vehicle6.convert_alpha() # remove whitespace from graphic

vehicle7 = pygame.image.load("Stingray.png")
vehicle7 = pygame.transform.scale(vehicle7, (60, 100)) # resize graphic
vehicle7 = vehicle7.convert_alpha() # remove whitespace from graphic

vehicle8 = pygame.image.load("bike.png")
vehicle8 = pygame.transform.scale(vehicle8, (60, 100)) # resize graphic
vehicle8 = vehicle8.convert_alpha() # remove whitespace from graphic

randomCars = [vehicle1, vehicle2, vehicle3, vehicle4, vehicle5, vehicle6, vehicle7, vehicle8]
enemy = random.choice(randomCars)


#brought to you by code-projects.org
pygame.display.set_icon(gameIcon)

pause = False


# crash = True

def survival_score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("SCORE: " + str(count), True, red)
    play_surface.blit(text, (0, 0))


def blockers(blockerx, blockery, blockerw, blockerh, color, enemyC):
    #pygame.draw.rect(play_surface, color, [blockerx, blockery, blockerw, blockerh])
    play_surface.blit(enemy, [blockerx, blockery, blockerw, blockerh])

def vehicle(x, y):
    play_surface.blit(vehicleImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    crash_sound.play()
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    play_surface.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(play_surface, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(play_surface, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    play_surface.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    play_surface.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        play_surface.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Car Dodge", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        play_surface.blit(TextSurf, TextRect)

        button("LET PLAY!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def handle_speed(keys, current_speed):
    if keys[pygame.K_UP] and current_speed < max_speed:
        current_speed += speed_increment
    elif keys[pygame.K_DOWN] and current_speed > min_speed:
        current_speed -= speed_increment
    return current_speed

def game_loop():
    global pause, enemy
    enemy = random.choice(randomCars)
    
    # Music
    pygame.mixer.music.load('bgmusic.mp3')
    pygame.mixer.music.play(-1)

    # Car position
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

    # Blocker/Enemy
    blocker_startx = random.randrange(0, display_width)
    blocker_starty = -600
    blocker_width = 55
    blocker_height = 95
    enemyC = random.choice(randomCars)
    enemy_speed = 4
    blockerCount = 1

    # Speed controls
    vehicle_speed = 5
    max_speed = 15
    min_speed = 2
    speed_increment = 1

    # Score
    obstacles_avoided = 0

    gameExit = False

    while not gameExit:
        keys = pygame.key.get_pressed()
        vehicle_speed = handle_speed(keys, vehicle_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -vehicle_speed
                elif event.key == pygame.K_RIGHT:
                    x_change = vehicle_speed
                elif event.key == pygame.K_UP:
                    y_change = -vehicle_speed
                elif event.key == pygame.K_DOWN:
                    y_change = vehicle_speed

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x_change = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    y_change = 0

        x += x_change
        y += y_change

        # ✅ add rest of game logic, collision, rendering etc...



        play_surface.blit(backgroundImage, (0, 0))

        blockers(blocker_startx, blocker_starty, blocker_width, blocker_height, block_color, enemyC)

        blocker_starty += enemy_speed
        vehicle(x, y)
        survival_score(obstacles_avoided)

        if x > display_width - vehicle_width or x < 0:
            crash()

        if blocker_starty > display_height:
            blocker_starty = 0 - blocker_height
            blocker_startx = random.randrange(0, display_width)
            obstacles_avoided += 1
            #enemy_speed += .25
            if obstacles_avoided % 5 == 0:
                enemy_speed += (obstacles_avoided * 1)


        if y < blocker_starty + blocker_height:
            #print('y crossover')

            if x > blocker_startx and x < blocker_startx + blocker_width or x + vehicle_width > blocker_startx and x + vehicle_width < blocker_startx + blocker_width:
                #print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
