from SnakeClasses import *
from Constants import *
from PlayerInput import *
from BoardClasses import *
from Food import *

import pygame

class SnakeGame:
    
    def __init__(self):

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption('Snake')
        self.window.fill(black)
        
        self.fps_increment=80
        self.FPS=STARTING_FPS
        
        self.playerInput = PlayerInput()
        
        self.board=Board()
        
        self.head=Segment((scaling_factor_width*(float(world_size)/2),scaling_factor_height*(float(world_size)/2)))
        self.snake=Snake(self.head)
        
        self.food=Food()

    def game(self):
        pygame.init()
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                self.playerInput.takeInput(event)
            if self.food.foodExists==False:
                self.food.spawnFood(self.board)
            if self.snake.foundFood(self.food.foodPosition)==True:
                self.food.clearFood(self.board)
                self.board.updateNodes(self.snake)
                self.drawBoard() 
                self.food.foodExists=False
                self.snake.grow()
            self.snake.setDirection(self.playerInput.direction)
            self.playerInput.finaliseDirection()
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

   
        
    def increaseFPS(self):
        self.fps_increment-=1
        if self.fps_increment<=0:
            if self.FPS<=fps_cap:
                self.FPS+=1
                self.fps_increment=80
                
                
    def main(self):
       self.game() 

SnakeGame=SnakeGame()
SnakeGame.main()