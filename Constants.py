import pygame

world_size = 60  
STARTING_FPS = 20
fps_increment=80
fps_cap=35

width=480
height=480
size = (width, height)
scaling_factor_width=width/world_size
scaling_factor_height=height/world_size
 
clock=pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)
red=(255,0,0)

playerX=float(size[0]/2)
playerY=float(size[1]/2)
startingPosition=(playerX, playerY)

rectangle_width=width/world_size
rectangle_height=height/world_size


#Player input constants:
up=0
down=1
left=2
right=3
direction=0