import pygame
from pong_player import Player
from pong_player import ComputerPlayer
from pong_ball import Ball

class PongGame():
    running = True          #GAME IS BEING PLAYED
    player_engine = 0.35    #PLAYER MOVEMENT SPEED
    final_score = 10        #WHEN THE GAME ENDS

    def __init__(self):
        #INITIALIZE GAME
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.smallFont = pygame.font.Font("freesansbold.ttf", 32)

        #CREATE GAME OBJECTS
        self.player = Player(False) #FALSE = NOT COMPUTER
        self.computer = ComputerPlayer(True, 8) #TRUE = COMPUTER, DIFFICULTY
        self.ball = Ball()

    def play_game(self):
        while self.running:
            #MANAGE DISPLAY AND USER INPUT
            self.set_background()
            self.show_game_data()
            self.user_controls()

            #CHECKS FOR FINAL SCORE REACHED/UPDATES SCREEN
            if self.still_playing():
                #UPDATE BALL
                self.ball.update_pos(self.player, self.computer)
                self.ball.draw_object(self.screen)

                #UPDATE PLAYER
                self.player.update_pos()
                self.player.draw_object(self.screen)

                #UPDATE COMPUTER
                self.computer.update_pos(self.ball.y, self.ball.x_speed)
                self.computer.draw_object(self.screen)

            pygame.display.update()

    def set_background(self):
        #TINTS BACKGROUND COLOR TO SHOW WHO IS WINNING
        if self.player.score == self.computer.score:
            self.screen.fill((255, 255, 255))
        elif self.player.score > self.computer.score:
            self.screen.fill((240, 240, 255))
        elif self.player.score < self.computer.score:
            self.screen.fill((255, 240, 240))

    def user_controls(self):
        # CHECK ALL USER INPUTS
        for event in pygame.event.get():

            # EXIT BUTTON HAS BEEN SELECTED
            if event.type == pygame.QUIT:
                PongGame.running = False

            # EVALUATE WHICH KEY HAS BEEN PRESSED DOWN/UPDATE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.y_speed = -1 * self.player_engine
                elif event.key == pygame.K_DOWN:
                    self.player.y_speed = self.player_engine

            # EVALUATE WHICH KEY HAS BEEN RELEASED/UPDATE
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.y_speed = 0

    def show_game_data(self):
        #SHOW PLAYER SCORE
        player_score = self.smallFont.render(str(self.player.score), True, (0, 0, 255))
        self.screen.blit(player_score, (10, 5))

        #SHOW COMPUTER SCORE
        comp_score = self.smallFont.render(str(self.computer.score), True, (255, 0, 0))
        self.screen.blit(comp_score, (760, 5))

    def still_playing(self):
        #CHECK IF PLAYER OR COMPUTER HAS ACHEIVED FINAL SCORE
        if self.player.score == PongGame.final_score:
            final_text = self.smallFont.render("YOU WIN", True, (0, 0 , 255))
            self.screen.blit(final_text, (320, 270))
            return False
        elif self.computer.score == PongGame.final_score:
            final_text = self.smallFont.render("YOU LOSE", True, (255, 0 , 0))
            self.screen.blit(final_text, (320, 270))
            return False
        return True

game1 = PongGame()
game1.play_game()
