# Is there anything better than Pygame?
# The best overall pygame alternative is Flutter. Other similar apps like pygame are Syncfusion 
# Essential Studio, python pillow, pandas python, and Progress Kendo UI. pygame alternatives can 
# be found in Component Libraries Software but may also be in Mobile Development Frameworks or 
# Application Development Platforms 
import pygame
import random


# pygame.init()

res=(500,500)

game_window=pygame.display.set_mode(res)

# game specific veriables
clock=pygame.time.Clock()

game_play=False
game_over=False

snk_x=30
snk_y=30
snk_size=15

velocity_x=4
velocity_y=0
fps=30

#colour
black=0,0,0
white=255,255,255
red=255,0,0
green=0,255,0
blue=0,0,255

while not game_play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_play=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                velocity_x=-4
            if event.key==pygame.K_RIGHT:
                velocity_x=4
            if event.key==pygame.K_UP:
                print("sam")
            if event.key==pygame.K_DOWN:
                print("ram")
    snk_x+=velocity_x
    game_window.fill(white)
    pygame.draw.rect(game_window,red,[snk_x,snk_y,snk_size,snk_size])
    rad=10
    pygame.draw.circle(game_window,blue,[snk_x+20,snk_y+20],rad)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()