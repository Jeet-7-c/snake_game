import pygame
import random
pygame.init()

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

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)


def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gameWindow, color,[y,x,snake_size,snake_size]) #snake diagram
	
#creating a game loop
def game_loop():
        #game specific variables

        exit_game=False
        game_over=False

        snake_x =250
        snake_y =350
        snake_size =15

        speed_0=0
        speed_=5
        velocity_x=speed_
        velocity_y=speed_0
        fps=30

        food_x=random.randint(20,width//2)
        food_y=random.randint(20,height//2)

        score=0
        with open ("highscore.txt","r") as f:
                h_score=f.read()

        snk_list=[]
        snk_legth=1

        
        while not exit_game:
                if game_over:
                        gameWindow.fill(black)
                        with open ("highscore.txt","w") as f:
                                f.write(str(h_score))

                        text_screen("Game over,",red,width/3,height/3)
                        text_screen("Press \"Enter\" to replay",red,width/5,height/2.5)
                        text_screen("  Highest Score: "+str(h_score),blue,width/4.5,height/2)


                        for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                        exit_game=True
                                if event.type==pygame.KEYDOWN:
                                        if event.key==pygame.K_RETURN:
                                                game_loop()
                                                exit_game=True
                else:
                        
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
                        
                        pygame.draw.rect(gameWindow, red,[food_y,food_x,snake_size,snake_size]) #food draw
                        
                        
                        if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10: #snake action (eat,score) 
                                score+=10
                                food_x=random.randint(20,width//2)
                                food_y=random.randint(20,height//2)
                                snk_legth+=5
                                if score>int(h_score):
                                        h_score=score
                        text_screen("Score: "+str(score) ,blue,5,5)
                        
                        head=[]
                        head.append(snake_x)
                        head.append(snake_y)
                        snk_list.append(head)
                        if len(snk_list)>snk_legth:
                                del snk_list[0]

                        plot_snake(gameWindow,green,snk_list,snake_size)

                        if snake_x<=0 or snake_y<=0 or snake_x>=520 or snake_y>=720:
                                game_over=True
                        if head in snk_list[:-1]:
                                game_over=True

                        
                pygame.display.update()	
                clock.tick(fps)			


        pygame.quit()
        

game_loop()
