import pygame,random
import random

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, width=800, height=600):
        
            
        """
        Description: Initalizes the player 
        args: 
        -pygame.sprite.spite arguement is being used as a base class for this "Class Player"
        - width and height argument is used to set the parameter for the player movement of the box
        return: None       
    """  
        super().__init__()
        self.WHITE = (255, 255, 255)
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.speedx = 0

    def update(self, width=800, height=600):
        
        """
        inserts the specficed function to the dictioary with the new added items in this function 
        args: self, width=800, height=600
        return: None
        """
        
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
                
    
            
            
            
    
        
    