from SnakeClasses import *
from Constants import *
import pygame
import random

class SnakeGame:
    
    def __init__(self):
        self.foodExists=False
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_up = False
        self.pressed_down = False
        
        self.playerInput=-1
        
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption('Snake')
        self.window.fill(black)
        
        self.fps_increment=80
        self.FPS=STARTING_FPS
        
        self.prospectiveDirection=0
        self.direction=0
        
        self.board=Board()
        
        self.head=Segment((scaling_factor_width*(float(world_size)/2),scaling_factor_height*(float(world_size)/2)))
        self.snake=Snake(self.head)
        
        self.foodExists=False
        self.foodGridPosition=(-1, -1)
        self.foodPosition=(-1, -1)
        

    def main(self):
        pygame.init()
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                self.takeInput(event)
            if self.foodExists==False:
                self.spawnFood()
            if self.foundFood()==True:
                self.clearFood()
                self.board.updateNodes(self.snake)
                self.drawBoard() 
                self.foodExists=False
                self.snake.grow()
            self.snake.setDirection(self.direction)
            self.direction=self.prospectiveDirection
            self.snake.moveSnake()
            self.board.updateNodes(self.snake)
            self.drawBoard()
            
            
            
            if self.snake.checkCollision()==True:
                break
            
            clock.tick(self.FPS)

            
            pygame.display.update()
            self.increaseFPS()
            

        pygame.quit()
        
    def drawBoard(self):
        for List in self.board.grid:
            for node in List:
                if node.getContainsFood()==True:
                    pygame.draw.rect(self.window, red, (node.getPosition()[0], node.getPosition()[1], rectangle_width, rectangle_height),0)
                elif node.getContainsSnake()==True:
                    pygame.draw.rect(self.window, white, (node.getPosition()[0], node.getPosition()[1], rectangle_width, rectangle_height),0)
                elif node.getContainsSnake()==False:
                    pygame.draw.rect(self.window, black, (node.getPosition()[0], node.getPosition()[1], rectangle_width, rectangle_height),0)

        
        
    def spawnFood(self):
        xPossibleNodeValues=random.randint(0,world_size-1)
        yPossibleNodeValues=random.randint(0, world_size-1)
                    
        if self.board.grid[xPossibleNodeValues][yPossibleNodeValues].getContainsSnake()==False:
            self.board.grid[xPossibleNodeValues][yPossibleNodeValues].setContainsFood(True)
            self.foodGridPosition=(xPossibleNodeValues,yPossibleNodeValues)
            self.foodPosition=(self.board.grid[xPossibleNodeValues][yPossibleNodeValues].getPosition()[0], self.board.grid[xPossibleNodeValues][yPossibleNodeValues].getPosition()[1])
            self.foodExists=True
            
        else:
            self.spawnFood()
            
    def foundFood(self):
       if self.head.getPosition()==self.foodPosition:
           return True
           
    def clearFood(self):
        self.board.grid[self.foodGridPosition[0]][self.foodGridPosition[1]].setContainsFood(False)
                
                
    def takeInput(self, event):
        
        if event.type == pygame.KEYDOWN:          # check for key presses          
            if event.key == pygame.K_LEFT:        # left arrow turns left
                self.pressed_left = True
            elif event.key == pygame.K_RIGHT:     # right arrow turns right
                self.pressed_right = True
            elif event.key == pygame.K_UP:        # up arrow goes up
                self.pressed_up = True
            elif event.key == pygame.K_DOWN:     # down arrow goes down
                self.pressed_down = True
        elif event.type == pygame.KEYUP:            # check for key releases
            if event.key == pygame.K_LEFT:        # left arrow turns left
                self.pressed_left = False
            elif event.key == pygame.K_RIGHT:     # right arrow turns right
                self.pressed_right = False
            elif event.key == pygame.K_UP:        # up arrow goes up
                self.pressed_up = False
            elif event.key == pygame.K_DOWN:     # down arrow goes down
                self.pressed_down = False
                
        if self.pressed_left:
            if self.direction!=right:
                self.prospectiveDirection=left
        if self.pressed_right:
            if self.direction!=left:
                self.prospectiveDirection=right
        if self.pressed_up:
            if self.direction!=down:
                self.prospectiveDirection=up
        if self.pressed_down:
            if self.direction!=up:
                self.prospectiveDirection=down
             
        
        
        
    def increaseFPS(self):
        self.fps_increment-=1
        if self.fps_increment<=0:
            if self.FPS<=fps_cap:
                self.FPS+=1
                self.fps_increment=80
                    

SnakeGame=SnakeGame()
SnakeGame.main()