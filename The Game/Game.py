import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")
#Load the images
walkRight = [pygame.image.load('data/R1.png'), pygame.image.load('data/R2.png'), pygame.image.load('data/R3.png'), pygame.image.load('data/R4.png'), pygame.image.load('data/R5.png'), pygame.image.load('data/R6.png'), pygame.image.load('data/R7.png'), pygame.image.load('data/R8.png'), pygame.image.load('data/R9.png')]
walkLeft = [pygame.image.load('data/L1.png'), pygame.image.load('data/L2.png'), pygame.image.load('data/L3.png'), pygame.image.load('data/L4.png'), pygame.image.load('data/L5.png'), pygame.image.load('data/L6.png'), pygame.image.load('data/L7.png'), pygame.image.load('data/L8.png'), pygame.image.load('data/L9.png')]
bg = pygame.image.load('data/bg.jpg')
char = pygame.image.load('data/standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
    
    def draw(self,screen):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.left:
            screen.blit(walkLeft[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walkRight[self.walk_count//3], (self.x,self.y))
            self.walk_count +=1
        else:
            screen.blit(char, (self.x,self.y))

def redraw_game_window():
    win.blit(bg, (0,0))
    man.draw(win)    
    pygame.display.update()


#mainloop
man = player(300,410,64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x += man.velocity
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walk_count = 0
        
    if not(man.is_jump):
        if keys[pygame.K_SPACE]:
            man.is_jump = True
            man.right = False
            man.left = False
            man.walk_count = 0
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10
            
    redraw_game_window()

pygame.quit()

