import pygame
import sys
import random
import time
pygame.init()
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("screen")

start_time = pygame.time.get_ticks()


score = 0
font = pygame.font.SysFont("Arial",35)
font2 = pygame.font.SysFont("Arial",105)

flower2x = random.randint(50,1470)
flower2y = random.randint(50,730)

#time_limit = 5

clock = pygame.time.Clock()

end_rect = pygame.Rect(0,0,1520,780)




bee_rect = pygame.Rect(500,500,100,100)
flower_rect = pygame.Rect(flower2x,flower2y,100,100)

speed = 13

bg = pygame.image.load("background bee game.png")
bee = pygame.image.load("bee.png")
flower = pygame.image.load("flower.png")
resize_bg = pygame.transform.scale(bg,(1520,780))
resize_bee = pygame.transform.scale(bee,(100,100))
resize_flower = pygame.transform.scale(flower,(100,100))

def movement_bee():
     keys = pygame.key.get_pressed()
     if keys[pygame.K_w] and bee_rect.y > 0:
          bee_rect.y = bee_rect.y - speed
     if keys[pygame.K_a] and bee_rect.x > 0:
          bee_rect.x = bee_rect.x - speed
     if keys[pygame.K_s] and bee_rect.y < 680:
          bee_rect.y = bee_rect.y + speed
     if keys[pygame.K_d] and bee_rect.x < 1420:
          bee_rect.x = bee_rect.x + speed
     


def draw():
    screen.blit(resize_bg,(0,0))
    screen.blit(resize_bee,(bee_rect.x,bee_rect.y))
    screen.blit(resize_flower,(flower_rect.x,flower_rect.y))
    #pygame.draw.rect(screen,"blue",flower_rect)
    #pygame.draw.rect(screen,"blue",bee_rect)
    score_text = font.render("SCORE " + str(score),True,"white") 
    screen.blit(score_text,(10,10))

def scoring():
    global score
    global flower2x
    global flower2y
    if bee_rect.colliderect(flower_rect):
             flower_rect.x = random.randint(100,1420)
             flower_rect.y = random.randint(100,680)
             score = score + 1
             print(score)


def timesup():
     pygame.draw.rect(screen,"black",end_rect)
     end_text = font2.render("TIME IS UP          YOUR SCORE: "+ str(score),True,"white") 
     screen.blit(end_text,(100,100))


def timer():
     passed_time = (pygame.time.get_ticks() -start_time)/1000
     if passed_time >= 10:
         timesup()
            
while True:
     draw()
     movement_bee()
     scoring()
     timer()
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()




