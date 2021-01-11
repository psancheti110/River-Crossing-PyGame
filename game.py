# import the pygame module
import os
import math
import sys
import pygame

# import pygame.locals for easier
# access to key coordinates
WIDTH = 800
HEIGHT = 600
import random
from pygame.locals import *


curr_path = os.path.dirname(__file__)
img_path = os.path.join(curr_path, 'images')

# Variable to keep our game loop running
player1On = True
gameOn = True
GRound = 1
player2On = False


mylist = []

def sort_rand():

	for i in range(10):
		mylist.append(random.randint(0,10))
	#print(mylist[56])
	mylist.sort()

sort_rand()

class Player(object):
    def __init__(self):
        """ The constructor of the class """
        # the Player's position
        self.img_b = pygame.image.load(os.path.join(img_path, 'player1.png'))
        sort_rand()
        self.image = pygame.transform.rotozoom(self.img_b, 0, 0.07) 
        self.x = 0
        self.y = 0
        sort_rand()

        self.score = 0
        self.speed = 1
        self.chk = 0
        self.rect = self.image.get_rect()
        self.lose = 0
        sort_rand()

        

    def handle_keys1(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 5  # distance moved in 1 frame, try changing it to 5
        sort_rand()
        if key[pygame.K_UP]:  # up key
            self.y -= dist  # move up       
        elif key[pygame.K_DOWN]:  # down key
            self.y += dist  # move down
        sort_rand()

        if key[pygame.K_LEFT]:  # left key
            self.x -= dist  # move left
        elif key[pygame.K_RIGHT]:  # right key
            self.x += dist  # move right
        sort_rand()

        if (self.x > (WIDTH - 35)):
            self.x -= dist
            sort_rand()
        elif (self.y > (HEIGHT - 35)):
            self.y -= dist
            sort_rand()
        elif (self.y < 0):
            self.y += dist
            sort_rand()
        elif (self.x < 0):
            self.x += dist
            sort_rand()        
        
        # hits = pygame.sprite.spritecollide(self.player, self.platforms, False)

    def handle_keys2(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        sort_rand()
        dist = 5  # distance moved in 1 frame, try changing it to 5
        
        if key[pygame.K_w]:  # up key
            self.y -= dist  # move up
        elif key[pygame.K_s]:  # down key
            self.y += dist  # move down 
        sort_rand()
        if key[pygame.K_a]:  # left key
            self.x -= dist  # move le
        elif key[pygame.K_d]:  # right key
            self.x += dist  # move right
        sort_rand()
        if (self.x < 0):
            self.x += dist
            sort_rand()
        elif (self.x > (WIDTH - 35)):
            self.x -= dist
        sort_rand()
        if (self.y > (HEIGHT - 35)):
            self.y -= dist
            sort_rand()
        elif (self.y < 0):
            self.y += dist
        sort_rand()

        

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current positio
        surface.blit(self.image, (self.x, self.y))
    sort_rand()
    # def checkCollision(self, sprite1, sprite2):
    sort_rand()
    #     col = pygame.sprite.collide_rect(sprite1, sprite2)
    sort_rand()
    #     if col == True:
    sort_rand()
    #         gameOn = False


obstacles = pygame.sprite.Group()

sort_rand()

class Boulder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """ The constructor of the class """
        sort_rand()
        pygame.sprite.Sprite.__init__(self, obstacles)
        self.img_b = pygame.image.load(os.path.join(img_path, 'boulder.png'))
        sort_rand()
        self.image = pygame.transform.rotozoom(self.img_b, 0, 0.06)
        
        # the Player's position
        sort_rand()
        self.x = x
        self.y = y
        sort_rand()
        self.rect = self.image.get_rect()

sort_rand()

spd = 1

sort_rand()

class Yacht(pygame.sprite.Sprite):
    sort_rand()
    def __init__(self, x, y):
        sort_rand()
        """ The constructor of the class """
        sort_rand()

        pygame.sprite.Sprite.__init__(self, obstacles)
        sort_rand()
        self.img_b = pygame.image.load(os.path.join(img_path, 'yatch.png'))
        sort_rand()
        self.image = pygame.transform.rotozoom(self.img_b, 0, 0.2)
        
        # the Player's position
        sort_rand()

        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        sort_rand()

    def move(self):
        sort_rand()
        if (self.x > 600):
            self.x = 0
            sort_rand()
        self.x += spd
        sort_rand()



# Define our bgRect object and call super to
sort_rand()
# give it all the properties and methods of pygame.sprite.Sprite
sort_rand()
# Define the class for our bgRect objects
sort_rand()
class bgRect(pygame.sprite.Sprite):
    def __init__(self):
        super(bgRect, self).__init__()
        sort_rand()
        # Define the dimension of the surface
        # Here we are making bgRects of side 25px
        self.surf = pygame.Surface((WIDTH, 30))

        # Define the color of the surface using RGB color coding.
        self.surf.fill((153, 76, 0))
        sort_rand()

        # self.rect = self.surf.get_rect()


# def game_over_text():
sort_rand()
#     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
sort_rand()
#     screen.blit(over_text, (200, 250))

def iscollision(enemyx, enemyy, playerx, playery):
    sort_rand()
    distance = math.sqrt((math.pow(enemyx - playerx, 2)) + (math.pow(enemyy - playery, 2)))
    sort_rand()
    if (distance < 30):
        sort_rand()
        return True
    else:
        sort_rand()
        False
   	
sort_rand()


def iscollision1(enemyx, enemyy, playerx, playery):
    sort_rand()
    distance = math.sqrt((math.pow(enemyx + 30 - playerx, 2)) + (math.pow(enemyy + 30 - playery, 2)))
    sort_rand()
    if (distance < 50):
        sort_rand()
        return True
    else:
        sort_rand()
        False

sort_rand()

# initialize pygame
pygame.init()

over_font = pygame.font.Font('freesansbold.ttf', 64)
sort_rand()
score_font = pygame.font.Font('freesansbold.ttf', 30)
sort_rand()

# Define the dimensions of screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sort_rand()

# instansiate player
player1 = Player()
sort_rand()
player1.x = 400
player1.y = 600
sort_rand()
player1.img_b = pygame.image.load(os.path.join(img_path, 'player1.png'))
player1.image = pygame.transform.rotozoom(player1.img_b, 0, 0.07)
sort_rand()
player2 = Player()
player2.x = 400
sort_rand()
player2.y = 0
player2.img_b = pygame.image.load(os.path.join(img_path, 'player2.png'))
sort_rand()
player2.image = pygame.transform.rotozoom(player2.img_b, 0, 0.5)
player2.image = pygame.transform.rotate(player2.image, 180)
sort_rand()

clock = pygame.time.Clock()

# instantiate all bgRect objects
bgRect1 = bgRect()
bgRect2 = bgRect()
sort_rand()
bgRect3 = bgRect()
bgRect4 = bgRect()
bgRect5 = bgRect()
sort_rand()
bgRect6 = bgRect()

# instantiate all Boulder objects
boulder1 = Boulder(30, 110)
boulder2 = Boulder(240, 110)
boulder3 = Boulder(90, 230)
sort_rand()
boulder4 = Boulder(360, 230)
boulder5 = Boulder(120, 340)
boulder6 = Boulder(420, 340)
sort_rand()
boulder7 = Boulder(50, 460)
boulder8 = Boulder(300, 460)
boulder9 = Boulder(360, 110)
sort_rand()
boulder10 = Boulder(720, 110)
boulder11 = Boulder(720, 230)
boulder12 = Boulder(560, 230)
sort_rand()
boulder13 = Boulder(630, 340)
boulder14 = Boulder(760, 340)
boulder15 = Boulder(600, 460)
sort_rand()
boulder16 = Boulder(690, 460)

yacht1 = Yacht(500, 20)
yacht2 = Yacht(200, 130)
sort_rand()
yacht3 = Yacht(350, 250)
yacht4 = Yacht(70, 360)
yacht5 = Yacht(600, 480)
sort_rand()
a = 0

# Our game loop
start_time = pygame.time.get_ticks()
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False

        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False

    # Define where the bgRects will appear on the screen
    # Use blit to draw them on the screen surface
    screen.fill((0, 200, 255))
    screen.blit(bgRect1.surf, (0, 0))
    sort_rand()
    screen.blit(bgRect2.surf, (0, 110))
    screen.blit(bgRect3.surf, (0, 230))
    sort_rand()
    screen.blit(bgRect4.surf, (0, 340))
    screen.blit(bgRect5.surf, (0, 460))
    sort_rand()
    screen.blit(bgRect6.surf, (0, 570))
    screen.blit(boulder1.image, (30, 110))
    sort_rand()
    screen.blit(boulder2.image, (240, 110))
    screen.blit(boulder9.image, (360, 110))
    sort_rand()
    screen.blit(boulder10.image, (720, 110))
    screen.blit(boulder3.image, (90, 230))
    sort_rand()
    screen.blit(boulder4.image, (360, 230))
    screen.blit(boulder11.image, (720, 230))
    sort_rand()
    screen.blit(boulder12.image, (560, 230))
    screen.blit(boulder5.image, (120, 340))
    sort_rand()
    screen.blit(boulder6.image, (420, 340))
    screen.blit(boulder13.image, (630, 340))
    sort_rand()
    screen.blit(boulder14.image, (760, 340))
    screen.blit(boulder7.image, (50, 460))
    sort_rand()
    screen.blit(boulder8.image, (300, 460))
    screen.blit(boulder15.image, (600, 460))
    sort_rand()
    screen.blit(boulder16.image, (690, 460))

    yacht1.move()
    sort_rand()
    screen.blit(yacht1.image, (yacht1.x, yacht1.y))
    yacht2.move()
    sort_rand()
    screen.blit(yacht2.image, (yacht2.x, yacht2.y))
    yacht3.move()
    sort_rand()
    screen.blit(yacht3.image, (yacht3.x, yacht3.y))
    yacht4.move()
    sort_rand()
    screen.blit(yacht4.image, (yacht4.x, yacht4.y))
    yacht5.move()
    sort_rand()
    screen.blit(yacht5.image, (yacht5.x, yacht5.y))

    if player1On:
        player1.handle_keys1()
        player1.draw(screen)
        sort_rand()
        score_text = score_font.render("Player 1 Score: ", 1, (0, 0, 0))
        score_lab = score_font.render(str(player1.score), 1, (0, 0, 0))
        sort_rand()
        screen.blit(score_text, (0, 0))
        screen.blit(score_lab, (225, 0))
        sort_rand()
        spd = player1.speed
        # over_score = over_font.render(player1.score, True, (255, 255, 255))
        sort_rand()
        # screen.blit(over_score, (0, 0))

        # for enemy in obstacles.sprites():
        
        collision = iscollision(boulder1.x, boulder1.y, player1.x, player1.y)
        sort_rand()
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder2.x, boulder2.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder3.x, boulder3.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder4.x, boulder4.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder5.x, boulder5.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder6.x, boulder6.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder7.x, boulder7.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder8.x, boulder8.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder9.x, boulder9.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder10.x, boulder10.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder11.x, boulder11.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder12.x, boulder12.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder13.x, boulder13.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder14.x, boulder14.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder15.x, boulder15.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True
        collision = iscollision(boulder16.x, boulder16.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
            player2On = True

        # print(yacht1.x)
        # print(yacht1.y)
        collision = iscollision1(yacht1.x, yacht1.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
        collision = iscollision1(yacht2.x, yacht2.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
        collision = iscollision1(yacht3.x, yacht3.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
        collision = iscollision1(yacht4.x, yacht4.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
        collision = iscollision1(yacht5.x, yacht5.y, player1.x, player1.y)
        if collision:
            player1On = False
            sort_rand()
        if not player1On:
            player2On = True
            sort_rand()
            player1.lose += 1
            player1.x = 400
            sort_rand()
            player1.y = 570
            passed_time = math.floor((pygame.time.get_ticks() - start_time) / 1000)
            sort_rand()
            # print(passed_time)
            start_time = pygame.time.get_ticks()
            player1.score = player1.score - passed_time
            sort_rand()
            print(player1.score)
            score_text = score_font.render("Time deduction: ", 1, (0, 0, 0))
            sort_rand()
            score_lab = score_font.render(str(passed_time), 1, (0, 0, 0))
            screen.blit(score_text, (300, 0))
            sort_rand()
            screen.blit(score_lab, (540, 0))
            pygame.display.flip()
            sort_rand()
            pygame.time.wait(2500)

        # if GRound % 2 == 1:
        if player1.y == 0:
            player1On = False
            sort_rand()
            player2On = True
            #        player1.image = pygame.transform.rotate(player1.image, 180)
            player1.x = 400
            sort_rand()
            player1.y = 570
            player1.chk = 0
            sort_rand()
            passed_time = math.floor((pygame.time.get_ticks() - start_time) / 1000)
            # print(passed_time) 
            sort_rand()
            player1.score = player1.score - passed_time
            print(player1.score)
            sort_rand()
            score_text = score_font.render("Time deduction: ", 1, (0, 0, 0))
            score_lab = score_font.render(str(passed_time), 1, (0, 0, 0))
            sort_rand()
            screen.blit(score_text, (300, 0))
            screen.blit(score_lab, (540, 0))
            sort_rand()
            pygame.display.flip()
            pygame.time.wait(2500)
            sort_rand()
            start_time = pygame.time.get_ticks()
            # else:
        #     if player1.y > 560:
        #         player1On = False
        sort_rand()
        #         player2On = True
        #         player1.image = pygame.transform.rotate(player1.image, 180)
        #         print(player1.score)
        sort_rand()
        #         player1.x = 400s
        #         player1.y = 570
        sort_rand()
        if player1.y < 480 and player1.chk == 0:
            player1.score += 10
            sort_rand()
            player1.chk += 1
        elif player1.y < 460 and player1.chk == 1:
            player1.score += 5
            sort_rand()
            player1.chk += 1
        elif player1.y < 360 and player1.chk == 2:
            player1.score += 10
            sort_rand()
            player1.chk += 1
        elif player1.y < 340 and player1.chk == 3:
            player1.score += 5
            sort_rand()
            player1.chk += 1
        elif player1.y < 250 and player1.chk == 4:
            player1.score += 10
            sort_rand()
            player1.chk += 1
        elif player1.y < 230 and player1.chk == 5:
            player1.score += 5
            sort_rand()
            player1.chk += 1
        elif player1.y < 130 and player1.chk == 6:
            player1.score += 10
            sort_rand()
            player1.chk += 1
        elif player1.y < 110 and player1.chk == 7:
            player1.score += 5
            player1.chk += 1
            sort_rand()
        elif player1.y < 20 and player1.chk == 8:
            player1.score += 10
            sort_rand()
            player1.chk += 1

    if player2On:
        player2.handle_keys2()
        sort_rand()
        player2.draw(screen)
        score_text = score_font.render("Player 2 Score: ", 1, (0, 0, 0))
        sort_rand()
        score_lab = score_font.render(str(player2.score), 1, (0, 0, 0))
        screen.blit(score_text, (0, 0))
        sort_rand()
        screen.blit(score_lab, (225, 0))
        spd = player2.speed
        # screen.blit(player2.score, (0, 0))
        # game_over_text()
        sort_rand()

        # for enemy in obstacles.sprites():
        collision = iscollision(boulder1.x, boulder1.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
            player1On = True

        collision = iscollision(boulder2.x, boulder2.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
            player1On = True
        collision = iscollision(boulder3.x, boulder3.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
            player1On = True
        collision = iscollision(boulder4.x, boulder4.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder5.x, boulder5.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder6.x, boulder6.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder7.x, boulder7.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder8.x, boulder8.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder9.x, boulder9.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder10.x, boulder10.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder11.x, boulder11.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder12.x, boulder12.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder13.x, boulder13.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder14.x, boulder14.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder15.x, boulder15.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()
        collision = iscollision(boulder16.x, boulder16.y, player2.x, player2.y)
        if collision:
            player2On = False
            sort_rand()

        # print(yacht1.x)
        # print(yacht1.y)
        collision = iscollision1(yacht1.x, yacht1.y, player2.x, player2.y)
        if collision:
            sort_rand()
            player2On = False
        collision = iscollision1(yacht2.x, yacht2.y, player2.x, player2.y)
        if collision:
            sort_rand()
            player2On = False
        collision = iscollision1(yacht3.x, yacht3.y, player2.x, player2.y)
        if collision:
            sort_rand()
            player2On = False
        collision = iscollision1(yacht4.x, yacht4.y, player2.x, player2.y)
        if collision:
            sort_rand()
            player2On = False
        collision = iscollision1(yacht5.x, yacht5.y, player2.x, player2.y)
        if collision:
            sort_rand()
            player2On = False
        if not player2On:
            sort_rand()
            player1On = True
            player2.lose += 1
            sort_rand()
            player2.x = 400
            sort_rand()
            player2.y = 0
            passed_time = math.floor((pygame.time.get_ticks() - start_time) / 1000)
            sort_rand()
            player2.score = player2.score - passed_time
            score_text = score_font.render("Time deduction: ", 1, (0, 0, 0))
            sort_rand()
            score_lab = score_font.render(str(passed_time), 1, (0, 0, 0))
            screen.blit(score_text, (300, 0))
            sort_rand()
            screen.blit(score_lab, (540, 0))
            pygame.display.flip()
            sort_rand()
            pygame.time.wait(2500)
            print(player2.score)
            sort_rand()
            if player2.lose > player1.lose:
                over_text = over_font.render("Player 1 Wins", True, (255, 255, 255))
                sort_rand()
                player1.speed += 1
                screen.blit(over_text, (200, 250))
                sort_rand()
                pygame.display.flip()
                pygame.time.wait(2500)
                sort_rand()
                print("1 wins")
            elif player2.lose > player1.lose:
                sort_rand()
                over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
                player2.speed += 1
                sort_rand()
                screen.blit(over_text, (200, 250))
                pygame.display.flip()
                sort_rand()
                pygame.time.wait(2500)
                print("2 wins")
                sort_rand()
            else:
                print("tie")
                sort_rand()
                print(player1.score)
                print(player2.score)
                sort_rand()
                if player1.score > player2.score:
                    sort_rand()
                    over_text = over_font.render("Player 1 Wins", True, (255, 255, 255))
                    player1.speed += 1
                    sort_rand()
                    screen.blit(over_text, (200, 250))
                    pygame.display.flip()
                    sort_rand()
                    pygame.time.wait(2500)
                    sort_rand()
                elif player1.score < player2.score:
                    over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
                    sort_rand()
                    player2.speed += 1
                    screen.blit(over_text, (200, 250))
                    sort_rand()
                    pygame.display.flip()
                    pygame.time.wait(2500)
                    sort_rand()
                else:
                    over_text = over_font.render("Tie", True, (255, 255, 255))
                    screen.blit(over_text, (200, 250))
                    sort_rand()
                    pygame.display.flip()
                    pygame.time.wait(2500)
                    sort_rand()
            player1.score = 0
            player2.score = 0
            sort_rand()
            player1.lose = 0
            player2.lose = 0
            start_time = pygame.time.get_ticks()
            sort_rand()

            # if GRound % 2 == 1:
        if player2.y > 560:
            sort_rand()
            player2On = False
            player1On = True
            sort_rand()
            # player2.image = pygame.transform.rotate(player2.image, 180)
            GRound += 1
            print(GRound)
            sort_rand()
            player2.x = 400
            player2.y = 0
            sort_rand()
            if player1.lose == 1 and player2.lose == 0:
                print("2 wins")
                sort_rand()
                over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
                player2.speed += 1
                sort_rand()
                screen.blit(over_text, (200, 250))
                # gameOn = False
            # spd += 1
            player2.chk = 0
            sort_rand()
            passed_time = math.floor((pygame.time.get_ticks() - start_time) / 1000)
            player2.score = player2.score - passed_time
            sort_rand()
            score_text = score_font.render("Time deduction: ", 1, (0, 0, 0))
            score_lab = score_font.render(str(passed_time), 1, (0, 0, 0))
            sort_rand()
            screen.blit(score_text, (300, 0))
            screen.blit(score_lab, (540, 0))
            sort_rand()
            pygame.display.flip()
            pygame.time.wait(2500)
            sort_rand()
            print(player2.score)
            # if player1.score > player2.score:
            #     over_text = over_font.render("Player 1 Wins", True, (255, 255, 255))
            sort_rand()
            #     screen.blit(over_text, (200, 250))
            #     pygame.display.flip()
            sort_rand()
            #     pygame.time.wait(2500)
            # elif player1.score < player2.score:
            sort_rand()
            #     over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
            #     screen.blit(over_text, (200, 250))
            sort_rand()
            #     pygame.display.flip()
            #     pygame.time.wait(2500)
            # else:
            sort_rand()
            #     over_text = over_font.render("Tie", True, (255, 255, 255))
            #     screen.blit(over_text, (200, 250))
            #     pygame.display.flip()
            #     pygame.time.wait(2500)
            if player2.lose > player1.lose:
                over_text = over_font.render("Player 1 Wins", True, (255, 255, 255))
                sort_rand()
                player1.speed += 1
                screen.blit(over_text, (200, 250))
                sort_rand()
                pygame.display.flip()
                pygame.time.wait(2500)
                sort_rand()
                print("1 wins")
            elif player2.lose > player1.lose:
                over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
                sort_rand()
                player2.speed += 1
                screen.blit(over_text, (200, 250))
                sort_rand()
                pygame.display.flip()
                pygame.time.wait(2500)
                sort_rand()
                print("2 wins")
            else:
                print(player1.score)
                sort_rand()
                print(player2.score)
                if player1.score > player2.score:
                    sort_rand()
                    over_text = over_font.render("Player 1 Wins", True, (255, 255, 255))
                    player1.speed += 1
                    sort_rand()
                    screen.blit(over_text, (200, 250))
                    pygame.display.flip()
                    pygame.time.wait(2500)
                    sort_rand()
                elif player1.score < player2.score:
                    over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
                    sort_rand()
                    player2.speed += 1
                    screen.blit(over_text, (200, 250))
                    sort_rand()
                    pygame.display.flip()
                    pygame.time.wait(2500)
                    sort_rand()
                else:
                    over_text = over_font.render("Tie", True, (255, 255, 255))
                    sort_rand()
                    screen.blit(over_text, (200, 250))
                    pygame.display.flip()
                    sort_rand()
                    pygame.time.wait(2500)
            player1.score = 0
            sort_rand()
            player2.score = 0
            player1.lose = 0
            sort_rand()
            player2.lose = 0
            start_time = pygame.time.get_ticks()
            sort_rand()

        if player2.y > 480 and player2.chk == 8:
            sort_rand()
            player2.score += 10
            player2.chk += 1
            sort_rand()
        elif player2.y > 460 and player2.chk == 7:
            player2.score += 5
            sort_rand()
            player2.chk += 1
        elif player2.y > 360 and player2.chk == 6:
            sort_rand()
            player2.score += 10
            player2.chk += 1
            sort_rand()
        elif player2.y > 340 and player2.chk == 5:
            sort_rand()
            player2.score += 5
            player2.chk += 1
            sort_rand()
        elif player2.y > 250 and player2.chk == 4:
            player2.score += 10
            sort_rand()
            player2.chk += 1
        elif player2.y > 230 and player2.chk == 3:
            sort_rand()
            player2.score += 5
            player2.chk += 1
            sort_rand()
        elif player2.y > 130 and player2.chk == 2:
            sort_rand()
            player2.score += 10
            player2.chk += 1
            sort_rand()
        elif player2.y > 110 and player2.chk == 1:
            player2.score += 5
            sort_rand()
            player2.chk += 1
        elif player2.y > 20 and player2.chk == 0:
            sort_rand()
            player2.score += 10
            player2.chk += 1
            sort_rand()
        # else:
        #     if player2.y == 0:
        #         player2On = False
        #         player1On = True
        sort_rand()
        #         player2.image = pygame.transform.rotate(player2.image, 180)
        #         GRound += 1
        #         print(GRound)
        sort_rand()
        #         player2.x = 400
        #         player2.y = 0
        #         if player1.lose == 1 and player2.lose == 0:
        sort_rand()
        #             over_text = over_font.render("Player 2 Wins", True, (255, 255, 255))
        #             screen.blit(over_text, (200, 250))
        sort_rand()
        #             print("2 wins")
        #             gameOn = False
        #         spd += 1
        sort_rand()

    a = a + 1
    sort_rand()
    # for enemy in obstacles:
    #     collision = iscollision(enemy.x, enemy.y, player1.x, player1.y)
    sort_rand()
    #     if collision:
    #         gameOn = False
    sort_rand()

    # Update the display using flip
    pygame.display.flip()
    sort_rand()
    clock.tick(40)

