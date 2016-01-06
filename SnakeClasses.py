from Constants import *


class Snake(object):
    
    def __init__(self, head):
        self.direction=up
        self.head=head
        
    def moveSnake(self):   
        self.updateSnake()
        self.moveHead()
            
    def moveHead(self):
        if self.direction==left:
            originalPosition=self.head.getPosition()
            self.head.setPosition((originalPosition[0]-scaling_factor_width, originalPosition[1]))
        elif self.direction==right:
            originalPosition=self.head.getPosition()
            self.head.setPosition((originalPosition[0]+scaling_factor_width, originalPosition[1]))
        elif self.direction==up:
            originalPosition=self.head.getPosition()
            self.head.setPosition((originalPosition[0],originalPosition[1]-scaling_factor_height))
        elif self.direction==down:
            originalPosition=self.head.getPosition()
            self.head.setPosition((originalPosition[0],originalPosition[1]+scaling_factor_height))      
            
    def updateSnake(self):
        segment=self.head.getLastNode()
        while segment!=self.head:
            segment.setPosition(segment.getPreviousNode().getPosition())
            segment=segment.getPreviousNode()
        
    def getHead(self):
        return self.head
        
    def getDirection(self):
        return self.direction
                
    def setDirection(self, direction):
        self.direction=direction
        
    def checkCollision(self):
        if self.collideWithSelf() or self.collideWithBoundary():
            return True
        else:
            return False
        
    def collideWithSelf(self):
        position = self.head.getPosition()
        
        if self.head.getLength()>1:
            segment=self.head.getLastNode()
            while segment!=self.head:
                if segment.getPosition()==position:
                    return True
                segment = segment.getPreviousNode()
            return False
                        
        
    def collideWithBoundary(self):
        position = self.head.getPosition()
        xCoordinate=position[0]
        yCoordinate=position[1]
        
        if xCoordinate<0 or xCoordinate>(width-scaling_factor_width):
            return True
        if yCoordinate<0 or yCoordinate>(height-scaling_factor_height):
            return True
        
        
    def grow(self):
        newSegment=Segment(self.head.getLastNode().getPosition)
        self.head.appendNode(newSegment)

    

class SnakeAI(Snake):
    
    def __init__(self):
        self.visitedNodes=[]
        super(SnakeAI, self).__init__()
    
    def BFS(self, node, visitedNodes):
        
        visitedNodes.append(something)
        
        if node.position==foodPosition:
            return visitedNodes
            
        else:
            nodesToVisit.append(node.getAllNeighbours)
        
        



class Segment(object):
    """A linked list, which stores the body of the snake."""
    
    def __init__(self, position):
        self.position=position
        self.previousNode=None
        self.nextNode=None
        self.length=1
        
    def appendNode(self, Segment):
        lastNode=self.getLastNode()
        lastNode.setNextNode(Segment)
        Segment.setPreviousNode(lastNode)
        self.length+=1
        
    def getElement(self, num):
        if num==0:
            return self
        else:
            if self.nextNode==None:
                if num>0:
                    print "Error, out of range"
            else:
                return self.getNextNode().getElement(num-1)
            
    def getLastNode(self):
        if self.getNextNode()==None:
            return self
        else:
            return Segment.getLastNode(self.getNextNode())
            
    def getPosition(self):
        return self.position
        
    def setPosition(self,Coordinates):
        self.position=Coordinates
        
    def getLength(self):
        return self.length
        
    def getNextNode(self):
        return self.nextNode
        
    def setNextNode(self,Segment):
        self.nextNode=Segment
    
    def getPreviousNode(self):
        return self.previousNode
        
    def setPreviousNode(self,Segment):
        self.previousNode=Segment
        


"""     
test=Segment((0,0))
test2=Segment((0,20))
test3=Segment((0,40))
test.appendNode(test2)
test.appendNode(test3)


snake=Snake(test)
"""

class Node(object):
    
    def __init__(self, position):
        self.position=position
        self.containsSnake=False
        self.containsFood=False
        
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
        
#testBlock=Node((0,0))

class Board(object):
    
    def __init__(self):
        #self.snake
        #self.food
        self.grid=[]
        self.fillGrid()
        
    def updateNodes(self, snake):
        self.resetNodes()
        self.setSnakeNodes(snake)
        #self.setFoodNodes(food)
        
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
                        
    #def setFoodNodes(self, food):
    #    for List in self.grid:
    #        for node in List:
    #            if food.getPosition()==node.getPosition():
    #                node.setContainsSnake(True)

    
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
"""
board=Board()
head=Segment((240,240))
snake=Snake(head)
board.updateNodes(snake)"""