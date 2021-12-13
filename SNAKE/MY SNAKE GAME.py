import pygame
from pygame.constants import K_LEFT, K_RETURN
import random

pygame.init()
pygame.mixer.init()

# defining colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (184, 255, 136)
food_col = (0, 255, 0)
black=(0,0,0)
blue=(0,0,255)
yellow=(255,255,0)

scrn_width = 700
scrn_height = 500
gameover = False
bckimg=pygame.image.load('BCK IMG.jpg')
bckimg=pygame.transform.scale(bckimg,(scrn_width,scrn_height))

gameWindow = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("Pinnell's Snake Game")


fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)


def show_score(text, color, x, y):
    My_score = font.render(text, True, color)
    gameWindow.blit(My_score, [x, y])


def mainpart():
    pygame.mixer.music.load("GAME MUSIC.mp3")
    pygame.mixer.music.play()
    exit_game = False
    snk_x = 40
    snk_y = 40
    s_size = 10
    f_size = 7
    velocity_x = 0
    velocity_y = 0
    list_size=[]

    food_x = random.randint(0, scrn_width-70)
    food_y = random.randint(0, scrn_height-70)
    points = 0

    while not exit_game:
        if snk_x < 0 or snk_x > scrn_width or snk_y < 0 or snk_y > scrn_height:
            pygame.mixer.music.load('GAME OVER.mp3')
            pygame.mixer.music.play()
            gameWindow.fill(white)
            show_score("Game Over , Press Enter to Play Again", red, 150, 200)
            show_score("Your Score : " + str(points*5), black, 260, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        mainpart()
        else:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        
                        # snk_x=snk_x+7
                        velocity_x = 3
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        # snk_y=snk_y+7
                        velocity_y = 3
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        # snk_x=snk_x-7
                        velocity_x = -3
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        # snk_y=snk_y-7
                        velocity_y = -3
                        velocity_x = 0

            if abs(snk_x-food_x) < 20 and abs(snk_y-food_y) < 20:
                points += 1
                s_size+=3
                food_x = random.randint(0, scrn_width-70)
                food_y = random.randint(0, scrn_height-70)

            elif abs(snk_x-food_x) < 3 and abs(snk_y-food_y) < 3:
                points += 2
                food_x = random.randint(0, scrn_width-70)
                food_y = random.randint(0, scrn_height-70)
            if s_size==0:
                show_score("Your Score : " + str(points*5), black, 260, 250)
            snk_x += velocity_x
            snk_y += velocity_y
            gameWindow.fill(white)
            gameWindow.blit(bckimg,(0,0))
            show_score("Your Score : " + str(points*5), white, 275, 5)
            pygame.draw.rect(gameWindow, red, [snk_x,snk_y,s_size, s_size])
            pygame.draw.rect(gameWindow, yellow, [food_x, food_y, f_size, f_size])
        pygame.display.update()
        clock.tick(fps)

mainpart()
pygame.quit()
quit()
