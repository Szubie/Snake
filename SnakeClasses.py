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
        
    def foundFood(self, foodPosition):
       if self.head.getPosition()==foodPosition:
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
        

