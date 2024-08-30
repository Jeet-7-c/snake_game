import pygame
import random
import os
#Castellar

pygame.mixer.init()

pygame.init()


eat=pygame.mixer.Sound("eat.mp3")
#colour
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

#creating window
height=520
width=720
gameWindow=pygame.display.set_mode((width,height))

#game title
pygame.display.set_caption("snake game")
icon_c=pygame.image.load("Snake_2.jpg")
pygame.display.set_icon(icon_c)

#clock and font
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)

#text screen defination 
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,[x,y])

# snake diagram plot
def plot_snake(gameWindow,color,snk_list,snake_size):
	for x,y in snk_list:
		pygame.draw.circle(gameWindow, color,[y,x],snake_size) #snake diagram


#welcome screen
def welcome_screen():
        exit_game=False
        while not exit_game:
                gameWindow.fill((150,0,150))
                text_screen("WELCOME TO MY SNAKE GAME",white,width/7.5,height/2.5)
                text_screen("PRESS ENTER TO START",white,width/5,height/2)
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                return(False)
                        if event.type==pygame.KEYDOWN:
                                
                                if event.key==pygame.K_RETURN:
                                        return(True)

#defination main game loop
def game_loop():
        #game specific variables
        exit_game=False
        game_over=False

        snake_x =250
        snake_y =350
        rad=9
        speed_0=0
        speed_=5
        velocity_x=speed_
        velocity_y=speed_0
        
        fps=30

        food_x=random.randint(20,width//2)
        food_y=random.randint(20,height//2)

        score=-1
        #if high score not exists & highscore read
        if (not os.path.exists("highscore.txt")):
                with open ("highscore.txt","w") as f:
                        f.write("0")
        with open ("highscore.txt","r") as f:
                h_score=f.read()

        snk_list=[]
        snk_legth=1

        #game start
        while not exit_game:
                pygame.display.update()
                clock.tick(fps)	
                
                #game_over
                if game_over:
                        

                        gameWindow.fill(black)
                        with open ("highscore.txt","w") as f:
                                f.write(str(h_score))
                        
                        #screen_text
                        text_screen("Game over,",red,width/3,height/3)
                        text_screen("Press \"Enter\" to replay",red,width/5,height/2.5)
                        text_screen("  Highest Score: "+str(h_score),blue,width/4.5,height/2)
                        text_screen("  Your Score: "+str(score),white,width/4.5,height/1.7)

                        #key handeling
                        for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                        exit_game=True
                                if event.type==pygame.KEYDOWN:
                                        if event.key==pygame.K_RETURN:
                                                # for background music
                                                pygame.mixer.music.load('background.mp3')
                                                pygame.mixer.music.play()

                                                game_loop()
                                                exit_game=True
                                                
                # game play                              
                else:
                        # for background music
                        if score==-1:
                                pygame.mixer.music.load('background.mp3')
                                pygame.mixer.music.play()
                                score+=1

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT: #for pygame quit
                                        exit_game=True
                                
                                if event.type == pygame.KEYDOWN: #action for keys 
                                        if event.key==pygame.K_LEFT:
                                                velocity_y=-speed_
                                                velocity_x=speed_0
                                        if event.key==pygame.K_RIGHT:
                                                velocity_y=speed_
                                                velocity_x=speed_0
                                        if event.key==pygame.K_UP:
                                                velocity_x=-speed_
                                                velocity_y=speed_0
                                        if event.key==pygame.K_DOWN:
                                                velocity_x=speed_
                                                velocity_y=speed_0
                                        if event.key==pygame.K_l:
                                                if velocity_y==speed_:
                                                        velocity_y=10
                                                if velocity_y==-speed_:
                                                        velocity_y=-10
                                                if velocity_x==speed_:
                                                        velocity_x=10
                                                if velocity_x==-speed_:
                                                        velocity_x=-10

                        snake_x+=velocity_x #for giving the motion to our snake
                        snake_y+=velocity_y #for giving the motion to our snake
                        
                        gameWindow.fill(black) #window black
                        
                        pygame.draw.circle(gameWindow, red,[food_y,food_x],rad) #food draw
                        
                        #snake action (eat,score) 
                        if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                                eat.play()

                                score+=10
                                food_x=random.randint(20,width//2)
                                food_y=random.randint(20,height//2)
                                snk_legth+=5
                                #highscore <score
                                if score>int(h_score):
                                        h_score=score
                        text_screen("Score: "+str(score) ,blue,5,5)
                        
                        head=[]
                        head.append(snake_x)
                        head.append(snake_y)
                        snk_list.append(head)
                        if len(snk_list)>snk_legth:
                                del snk_list[0]
                        # snake call
                        plot_snake(gameWindow,green,snk_list,rad)

                        if snake_x<=0 or snake_y<=0 or snake_x>=520 or snake_y>=720:
                                pygame.mixer.music.load('over.mp3')
                                pygame.mixer.music.play()
                                game_over=True
                        if head in snk_list[:-1]:
                                pygame.mixer.music.load('over.mp3')
                                pygame.mixer.music.play()
                                game_over=True

                        if score ==50:
                                speed_=6
                        if score==100:
                                speed_=8
                        if score==150:
                                speed_=10
                        

                        
                		
        pygame.quit()

# return from welcome_screen
r_s=welcome_screen()
if r_s== True:
        game_loop()
else:
        pygame.quit()
