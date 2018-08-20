import pygame

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("First Game")

    x = 50
    y = 400
    width = 40
    height = 60
    velocity = 8 

    screen_width = 500
    screen_heigth = 500

    isJump = False
    jumpCount = 10
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((screen_width,screen_heigth))
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        pygame.time.delay(50)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > velocity:
            x -= velocity
        if keys[pygame.K_RIGHT] and x < screen_width-width-velocity:
            x += velocity
        if not (isJump):
            if keys[pygame.K_UP] and y > velocity:
                y -= velocity
            if keys[pygame.K_DOWN] and y < screen_heigth-height:
                y += velocity
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount>= -10:
                neg = 1 
                if jumpCount<0 :
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10


              
        screen.fill( (0,0,0) )
        pygame.draw.rect(screen, (255,255,255), (x,y,width,height) )
        pygame.display.update()


win=pygame.display.set_mode((500,500))

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()