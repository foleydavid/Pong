import pygame
import random

class Player:

    def __init__(self, ai):
        #INITIALIZE BASED ON IF IS COMPUTER OR HUMAN PLAYER
        self.image = pygame.image.load("player.png")
        if ai:
            self.x = 720
            self.y = 350
            self.x_len = 40  # pixels
            self.y_len = 100  # pixels
            self.y_speed_max = 0.3
            self.y_speed = self.y_speed_max
        else:
            self.x = 20
            self.y = 350
            self.x_len = 100   #pixels
            self.y_len = 100   #pixels
            self.y_speed = 0
        self.ai = ai
        self.score = 0

    def update_pos(self):
        #CHANGE PLAYER/COMPUTER POSITION
        self.y += self.y_speed

        #PLAYER VERTICAL BOUNDARIES
        if self.y < 0:
            self.y = 0
        elif self.y > 600 - self.y_len:
            self.y = 600 - self.y_len

    def draw_object(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))

class ComputerPlayer(Player):

    def __init__(self, ai, difficulty):
        super().__init__(ai)
        self.difficulty = difficulty

    def update_pos(self, ball_y, ball_x_speed):
        #UPDATE COMPUTER POSITION
        self.y += self.y_speed

        #RETURN TO CENTER WHEN BALL MOVES AWAY
        #POTENTIALLY MOVES TOWARD BALL OR STOPS, DEPENDING ON DIFFICULTY
        if ball_x_speed < 0 and self.y < (320 - self.y_len):
            self.y_speed = self.y_speed_max
        elif ball_x_speed < 0 and self.y > (340 - self.y_len):
            self.y_speed = -1 * self.y_speed_max
        elif ball_x_speed < 0:
            self.y_speed = 0
        elif random.randint(1, 10) > self.difficulty:
            self.y_speed = 0
        elif self.y < ball_y:
            self.y_speed = self.y_speed_max
        else:
            self.y_speed = -1 * self.y_speed_max

        #COMPUTER VERTICAL BOUNDARIES
        if self.y < 0:
            self.y = 0
        elif self.y > 600 - self.y_len:
            self.y = 600 - self.y_len
