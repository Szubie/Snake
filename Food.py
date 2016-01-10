from Constants import *
import random

class Food(object):
    
    def __init__(self):
        self.foodExists=False
        self.foodGridPosition=(-1, -1)
        self.foodPosition=(-1, -1)
         
        
    def spawnFood(self, boardGrid):
        xPossibleNodeValues=random.randint(0,world_size-1)
        yPossibleNodeValues=random.randint(0, world_size-1)
                    
        if boardGrid[xPossibleNodeValues][yPossibleNodeValues].getContainsSnake()==False:
            boardGrid[xPossibleNodeValues][yPossibleNodeValues].setContainsFood(True)
            self.foodGridPosition=(xPossibleNodeValues,yPossibleNodeValues)
            self.foodPosition=(boardGrid[xPossibleNodeValues][yPossibleNodeValues].getPosition()[0], boardGrid[xPossibleNodeValues][yPossibleNodeValues].getPosition()[1])
            self.foodExists=True
            
        else:
            self.spawnFood(boardGrid)
            
           
    def clearFood(self, boardGrid):
        boardGrid[self.foodGridPosition[0]][self.foodGridPosition[1]].setContainsFood(False)   