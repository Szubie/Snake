from Constants import *

class Node(object):
    
    def __init__(self, position):
        self.position=position
        self.containsSnake=False
        self.containsFood=False
        self.neighbours=[]
        
    def getPosition(self):
        return self.position
        
    def setPosition(self,Coordinates):
        self.position=Coordinates
        
    def getContainsSnake(self):
        return self.containsSnake
        
    def setContainsSnake(self, boolean):
        self.containsSnake=boolean
        
    def getContainsFood(self):
        return self.containsFood
        
    def setContainsFood(self, boolean):
        self.containsFood=boolean
        
    #def findNeighbours(self):
    #    if self.position[0]<=0
        

class Board(object):
    
    def __init__(self):
        self.grid=[]
        self.fillGrid()
        
    def updateNodes(self, snake):
        self.resetNodes()
        self.setSnakeNodes(snake)
        
    def resetNodes(self):
        for List in self.grid:
            for node in List:
                node.setContainsSnake(False)
                #node.setContainsFood(False)
        
    def setSnakeNodes(self, snake):
        segment=snake.getHead()
        for List in self.grid:
            for node in List:
                if segment.getPosition()==node.getPosition():
                    node.setContainsSnake(True)
                    
        segment=snake.getHead().getLastNode()
        while segment!=snake.getHead():
            for List in self.grid:
                for node in List:
                    if segment.getPosition()==node.getPosition():
                        node.setContainsSnake(True)
            segment=segment.getPreviousNode()
            
        if snake.getHead().getLength()==1:
            segment=snake.getHead().getLastNode()
            for List in self.grid:
                for node in List:
                    if segment.getPosition()==node.getPosition():
                        node.containsSnake=True

    
    def fillGrid(self):    
        xValue=0
        yValue=0
        
        for i in range(world_size):
            yAxis=[]
            for j in range(world_size):
                yAxis.append(Node((xValue, yValue)))
                yValue+=(scaling_factor_height)
            self.grid.append(yAxis)
            yValue=0
            
            xValue+=scaling_factor_width