import pygame
import sys
import star
import player

class Controller:
   def __init__(self, width=800, height=600):
         
      """
   descrption: initalizes the game screen
   args: self, width=800, and height= 600
   return=None 
    """
      pygame.init()
      self.width = width
      self.height = height
      self.screen = pygame.display.set_mode((width, height))
      pygame.display.set_caption("DreamCatcher")
      self.clock = pygame.time.Clock()
      self.font = pygame.font.SysFont(None, 36)
      self.WHITE = (255, 255, 255)
      self.BLACK = (0, 0, 0)
      self.YELLOW = (255, 255, 0)
      self.score = 0
      self.game_over = False
      self.start_time = pygame.time.get_ticks()
      self.play_time = 30
      self.player = player.Player(self.width, self.height)
      self.stars = pygame.sprite.Group()
      for _ in range(10):
            stars = star.Star(self.width, self.height)
            self.stars.add(stars)
   
   def end_menu(self, score):
      
      """
      descrption: displays end menu where it says if you won the game and you can press Q for quit
      Args: self, score
      return: None  
      """
        
      self.screen.fill(self.BLACK)
      game_over_text = self.font.render("GAME OVER", True, self.WHITE)
      result_text = self.font.render("You Win!" if score > 60 else "You Lose!", True, self.WHITE)
      instruction_text = self.font.render("Press Q to quit", True, self.WHITE)
      self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 3))
      self.screen.blit(result_text, (self.width // 2 - result_text.get_width() // 2, self.height // 2))
      self.screen.blit(instruction_text, (self.width // 2 - instruction_text.get_width() // 2, self.height // 2 + 50))
      pygame.display.flip()

      waiting = True
      while waiting:
         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
               if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_q:
                     pygame.quit()
                     sys.exit()

   def main_game(self):
      
      """
   descrption: runs a loop of where the stars fall down from the sky at different speeds
   args: self
   return=None 
    """
    
      all_sprites = pygame.sprite.Group()
      stars = pygame.sprite.Group()

      playerOne = player.Player()
      all_sprites.add(playerOne)

      for _ in range(10):
         starObject = star.Star()
         all_sprites.add(starObject)
         stars.add(starObject)

      score = 0
      start_time = pygame.time.get_ticks()
      game_over = False

      while not game_over:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

         all_sprites.update()

   
         hits = pygame.sprite.spritecollide(playerOne, stars, True)
         for hit in hits:
            score += 1
            starHit = star.Star()
            all_sprites.add(starHit)
            stars.add(starHit)

      
         self.screen.fill("BLACK")
         all_sprites.draw(self.screen)

      
         score_text = self.font.render("Score: " + str(score), True, "WHITE")
         self.screen.blit(score_text, (10, 10))

      
         current_time = pygame.time.get_ticks()
         time_left = max(0, 30 - (current_time - start_time) // 1000)
         timer_text = self.font.render("Time: " + str(time_left), True, "WHITE")
         self.screen.blit(timer_text, (self.width - 120, 10))

         if time_left == 0:
            game_over = True

         pygame.display.flip()
         pygame.time.Clock().tick(60)
      self.end_menu(score)

       

            

   def game_over_loop(self,width=800, height=600):
      
      """
        descrption: this allows for the game over screen to be on display for a duration amount of time, allows the user to exit out of the game using the alloted keys illustrated
        args: self, width=800 and height=600 of the screen
        return: None
         """
      self.WHITE = (255, 255, 255)
      self.BLACK = (0, 0, 0)
      self.YELLOW = (255, 255, 0)
      self.screen.fill(self.BLACK)
      self.screen.blit(self.game_over_text, (width // 2 - self.game_over_text.get_width() // 2, height // 2 - 50))
      pygame.display.flip()

      pygame.time.delay(3000)
      pygame.quit()
      sys.exit()
   pass

   def update(self):
      """
        this displays the score of the player and also it updates the system by redisplaying the screen
        args: self
        return: None
         """
      self.player.update(self.width, self.height)
      self.stars.update(self.width, self.height)

      hits = pygame.sprite.spritecollide(self.player, self.stars, True)
      for self.hit in hits:
            self.score += 1
            new_star = star.Star(self.width, self.height)
            self.stars.add(new_star)

      current_time = pygame.time.get_ticks()
      elapsed_time = (current_time - self.start_time) // 1000
      remaining_time = max(self.play_time - elapsed_time, 0)
      if self.score == 10:
         self.game_over = True
      if self.score > 60:
        self.game_over_text = self.font.render("GAME OVER. You Win!", True, self.WHITE)
      else:
        self.game_over_text = self.font.render("GAME OVER. You Lose!", True, self.WHITE)



      
              

               