from ast import Pass
from tkinter import image_names
import pygame, os, random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
GROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
BIRD_IMAGES = [
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))), 
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))), 
                pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
            ]

pygame.font.init()
POINTS_FONT = pygame.font.SysFont('arial', 50)



class Bird:
    IMAGES = BIRD_IMAGES
    
    #rotation animation
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_SPEED = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.heigh = self.y
        self.time = 0
        self.image_index = 0
        self.image = self.IMAGES[0]
        
    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.heigh = self.y
    
    def movement(self):
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.speed * self.time
        
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2
            
        self.y += displacement
        
        #angle
        
        if displacement < 0 or self.y < (self.heigh + 50):
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION
            else:
                if self.angle > -90:
                    self.angle -= self.ROTATION_SPEED
        
        ######################################################

    def draw(self, window):
        self.image_index += 1
        
        if self.image_index < self.ANIMATION_SPEED:
            self.image = self.IMAGES[0]
        elif self.image_index < self.ANIMATION_SPEED*2:
            self.image = self.IMAGES[1]
        elif self.image_index < self.ANIMATION_SPEED*3:
            self.image = self.IMAGES[2]
        elif self.image_index < self.ANIMATION_SPEED*4:
            self.image = self.IMAGES[1]
        elif self.image_index >= self.ANIMATION_SPEED*4+1:
            self.image = self.IMAGES[0]
            self.image_index = 0
            
        if self.angle <= -80:
            self.image = self.IMAGES[1]
            self.image_index = self.ANIMATION_SPEED*2
        
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        image_center_pos = self.image.get_rect(topleft = (self.x, self.y)).center
        rect = rotated_image.get_rect(center=image_center_pos)
        window.blit(rotated_image, rect.topleft)
        
        def get_mask(self):
            pygame.mask.from_surface(self.image)
        
class Pipe:
    pass

class Ground:
    pass