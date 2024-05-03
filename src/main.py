import pygame
import controller
            

def main():
    pygame.init()
    game = controller.Controller()
    game.main_game()
if __name__ == '__main__':
    main()
    