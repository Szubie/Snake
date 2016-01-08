from Constants import *
import random

class Food(object):
    
    def __init__(self):
        self.foodExists=False
        self.foodGridPosition=(-1, -1)
        self.foodPosition=(-1, -1)
         
        
    def spawnFood(self, board):
        xPossibleNodeValues=random.randint(0,world_size-1)
        yPossibleNodeValues=random.randint(0, world_size-1)
                    
        if board.grid[xPossibleNodeValues][yPossibleNodeValues].getContainsSnake()==False:
            board.grid[xPossibleNodeValues][yPossibleNodeValues].setContainsFood(True)
            self.foodGridPosition=(xPossibleNodeValues,yPossibleNodeValues)
            self.foodPosition=(board.grid[xPossibleNodeValues][yPossibleNodeValues].getPosition()[0], board.grid[xPossibleNodeValues][yPossibleNodeValues].getPosition()[1])
            self.foodExists=True
            
        else:
            self.spawnFood(board)
            
           
    def clearFood(self, board):
        board.grid[self.foodGridPosition[0]][self.foodGridPosition[1]].setContainsFood(False)   