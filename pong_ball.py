import pygame
import random
from pong_player import Player

class Ball:
    acceleration = 0.000005     #HOW QUICKLY SPEED INCREASES

    def __init__(self):
        self.image = pygame.image.load("puck.png")
        self.x = 370
        self.y = 0
        self.x_len = 64
        self.y_len = 32
        self.x_speed = random.choice([-0.2, 0.2])
        self.y_speed = random.randint(1,3) / 10

    def update_pos(self, player, computer):
        #UPDATE BALL POSITION
        self.x += self.x_speed
        self.y += self.y_speed

        #INCREASE BALL SPEED IN MOVEMENT DIRECTION
        self.x_speed += self.x_speed // abs(self.x_speed) * Ball.acceleration
        try:
            self.y_speed += self.y_speed // abs(self.y_speed) * Ball.acceleration
        except ZeroDivisionError:
            self.y_speed = 0

        #BOUNCE BACK BALL TOWARD SCREEN
        if self.y < 0:
            self.y = 0
            self.y_speed = abs(self.y_speed)
        elif self.y > 600 - self.y_len:
            self.y_speed = -1 * abs(self.y_speed)

        #CHECK FOR CHANGE IN BALL BEHAVIOR
        self.check_collision(player)
        self.check_collision(computer)
        self.check_goal(player, computer)

    def draw_object(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))

    def check_collision(self, player):
        #SETS BOUNDARY POSITIONS ON PLAYER/COMPUTER
        player_x1, player_x2 = player.x + 30 , player.x + 50
        player_y1, player_y2 = player.y - 20, player.y + player.y_len + 20

        #ESTABLISH POINTS OF CONTACT
        if player.ai:
            ball_xContact = self.x + self.x_len
        else:
            ball_xContact = self.x
        ball_yContact = self.y + (self.y_len / 2)

        #CHECK IF BALL HAS ENTERED INTO REGION OF PLAYER/COMPUTER
        if ball_xContact > player_x1 and ball_xContact < player_x2:
            if ball_yContact > player_y1 and ball_yContact < player_y2:

                #SENDS BALL BACK LEFT OR RIGHT DEPENDS ON WHICH PLAYER IS HIT
                if player.ai:
                    self.x_speed = -1 * abs(self.x_speed)
                else:
                    self.x_speed = abs(self.x_speed)

    #CHECK IF PASSED GOAL BOUNDS, UPDATES CORRECT SCORE
    def check_goal(self, player, computer):
        if self.x < -100 or self.x > 900:
            if self.x < -100:
                computer.score +=1
            elif self.x > 900:
                player.score += 1
            self.__init__()
