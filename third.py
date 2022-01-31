# first, let Python know we're using pygame
import pygame

# needed to draw pixels
import pygame.gfxdraw

# make sure pygame gets set up
pygame.init()

# Set width and height of our screen we'll make next
screenWidth = 800
screenHeight = 800

# create a screen to draw to with screenWidth and screenHeight
screen = pygame.display.set_mode((screenWidth,screenHeight))

# white is red, green, and blue light in equal amounts
# at maximum brightness (255 for pygame)
white = (255,255,255)

# black is an absence of light
black = (0,0,0)

# Let's make something so we know when to stop
running = True

# Let's run while running is still true
while running:

    # fill the screen with black
    screen.fill(black)

    ## Draw a single white pixel in the middle of the screen
    #pygame.gfxdraw.pixel(screen, screenWidth // 2, screenHeight // 2, white)

    # Our for loop, for the width of the screen
    for i in range(0,screenWidth):
        ## Our pixel draw function use i to know the current value
        #pygame.gfxdraw.pixel(screen, i, screenHeight // 2, white)

        ## draw the same x and y for the whole width
        #pygame.gfxdraw.pixel(screen, i, i, white)

        # Our pixel draw function uses i to know the current value
        # drawing a giant 'x' across the screen
        pygame.gfxdraw.pixel(screen, i, i, white)
        pygame.gfxdraw.pixel(screen, i, screenHeight - i, white)

        # extra lines at end of chapter -- not sure how to get the extra 'texture' on 'x' lines, but I have the rest of it I think
        pygame.gfxdraw.pixel(screen, i, screenHeight // 4, white)
        pygame.gfxdraw.pixel(screen, i, 3 * screenHeight // 4, white)

        pygame.gfxdraw.pixel(screen, screenWidth // 4, i, white) # this only works bc screenWidth and screenHeight are equal
        pygame.gfxdraw.pixel(screen, 3 * screenWidth // 4, i, white)



    for event in pygame.event.get():
        #if you try to quit, let's leave this loop
        if event.type == pygame.QUIT:
            running = False # lets loop finish

    # this is how we update the screen we've been drawing on
    pygame.display.flip()