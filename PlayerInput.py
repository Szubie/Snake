import pygame
from Constants import *

class PlayerInput(object):
    
    def __init__(self):
        self.foodExists=False
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_up = False
        self.pressed_down = False
        
        self.playerInput=-1
        
        self.prospectiveDirection=0
        self.direction=0
        
      
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
             
    def finaliseDirection(self):
        self.direction=self.prospectiveDirection