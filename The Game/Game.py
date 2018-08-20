import pygame
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
screen = pygame.display.set_mode((500,480))
hitCount = 0 

pygame.display.set_caption("First Game")
bg = pygame.image.load('data/bg.jpg')
myfont = pygame.font.SysFont('Comic Sans MS', 24, True)
textsurface = myfont.render("Score : "+str(hitCount), False, (0, 0, 0))

clock = pygame.time.Clock()

class projectile(object):
    def __init__(self,x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class enemy(object):
    def __init__(self, x,y,width,height,end):
        #Load the images
        self.walkRight = [pygame.image.load('data/R1E.png'), pygame.image.load('data/R2E.png'), pygame.image.load('data/R3E.png'), pygame.image.load('data/R4E.png'), pygame.image.load('data/R5E.png'), pygame.image.load('data/R6E.png'), pygame.image.load('data/R7E.png'), pygame.image.load('data/R8E.png'), pygame.image.load('data/R9E.png'), pygame.image.load('data/R10E.png'), pygame.image.load('data/R11E.png')]
        self.walkLeft = [pygame.image.load('data/L1E.png'), pygame.image.load('data/L2E.png'), pygame.image.load('data/L3E.png'), pygame.image.load('data/L4E.png'), pygame.image.load('data/L5E.png'), pygame.image.load('data/L6E.png'), pygame.image.load('data/L7E.png'), pygame.image.load('data/L8E.png'), pygame.image.load('data/L9E.png'), pygame.image.load('data/L10E.png'), pygame.image.load('data/L11E.png')]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk_count = 0
        self.end = end
        self.velocity = 3
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 17, self.y+2, 31, 57 )
        self.health = 10
        self.visible = True
    
    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            if self.velocity > 0:
                screen.blit(self.walkRight[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            else:
                screen.blit(self.walkLeft[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] -20,50,10  ) )
            pygame.draw.rect(screen, (0,154,0), (self.hitbox[0], self.hitbox[1] -20,50-((50/10)*(10-self.health)),10  ) )
            self.hitbox = (self.x + 17, self.y+2, 31, 57 )
            #pygame.draw.rect(screen,(255,0,0),self.hitbox,2)
    def hit(self):
        global hitCount 
        hitCount += 1
        if self.health > 1 :
            self.health -= 1
        else:
            self.visible=False
        global textsurface 
        textsurface = myfont.render("Score :"+str(hitCount), False, (0, 0, 0))
       


    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walk_count = 0

class player(object):
    def __init__(self, x,y,width,height):
        #Load the images
        self.walkRight = [pygame.image.load('data/R1.png'), pygame.image.load('data/R2.png'), pygame.image.load('data/R3.png'), pygame.image.load('data/R4.png'), pygame.image.load('data/R5.png'), pygame.image.load('data/R6.png'), pygame.image.load('data/R7.png'), pygame.image.load('data/R8.png'), pygame.image.load('data/R9.png')]
        self.walkLeft = [pygame.image.load('data/L1.png'), pygame.image.load('data/L2.png'), pygame.image.load('data/L3.png'), pygame.image.load('data/L4.png'), pygame.image.load('data/L5.png'), pygame.image.load('data/L6.png'), pygame.image.load('data/L7.png'), pygame.image.load('data/L8.png'), pygame.image.load('data/L9.png')]
        self.char = pygame.image.load('data/standing.png')
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
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60 )
    
    def draw(self,screen):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not(self.standing):
            if self.left:
                screen.blit(self.walkLeft[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            elif self.right:
                screen.blit(self.walkRight[self.walk_count//3], (self.x,self.y))
                self.walk_count +=1
        else:
            if self.right:
                screen.blit(self.walkRight[0], (self.x,self.y))
            elif self.left:
                screen.blit(self.walkLeft[0], (self.x,self.y))
            else :
                screen.blit(self.char, (self.x,self.y))
        self.hitbox = (self.x + 17, self.y+11, 29, 52 )
        #pygame.draw.rect(screen,(255,0,0),self.hitbox,2)        

def redraw_game_window():
    screen.blit(bg, (0,0))
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    screen.blit(textsurface,(390,10))
    pygame.display.update()


#mainloop
man = player(300,410,64,64)
goblin = enemy(100,410, 64,64,450)
bullets = []
shoots = 0

run = True
while run:
    clock.tick(27)

    if shoots > 0:
        shoots += 1
    if shoots > 3:
        shoots = 0 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.radius + bullet.y > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shoots == 0:
        x=int(round(man.x + man.width*0.7))
        if man.left :
            facing = -1
            x=int(round(man.x+ man.width*0.3))
        else :
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile( x, int(round(man.y+man.height//2)) , 6, (139,0,0), facing ))  
        shoots = 1

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x += man.velocity
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walk_count = 0
        
    if not(man.is_jump):
        if keys[pygame.K_UP]:
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

