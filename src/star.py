import pygame
import random 

class Star(pygame.sprite.Sprite):
    def __init__(self, width=800, height=600):
        
        """
    description: intializes the yellow "stars" (the boxes)
    args: self, and  width=800
    return: None
    """
        super().__init__()
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.image = pygame.Surface((30, 30))
        self.image.fill(self.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(3, 7)

    def update(self, width=800, height=600):
        
        """
        descritption: it resets the position of the stars and handles the different speed of the stars 
        args: self, width = 800, and height=600
        return: None
        """
    
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, width - self.rect.width)
            self.speedy = random.randint(3, 7)
            
    