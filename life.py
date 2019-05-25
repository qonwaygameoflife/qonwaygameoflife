import pygame, copy, math, random
import numpy as np
from qrules import SQGOL
pygame.init()

PIXEL_SIZE = 5
WIN_WIDTH = 640
WIN_HEIGHT = 480

#Update every 2ms
REFRESH = 2
TARGET_FPS = 60

class Grid():
    def __init__(self, *args, **kwargs):
        self.grid = [[np.array([1,0]) for i in range(WIN_HEIGHT // PIXEL_SIZE)] for i in range(WIN_WIDTH // PIXEL_SIZE)]

    def setCell(self, x, y, stat):
        self.grid[x][y] = stat
        
    def getCell(self, x, y):
        return self.grid[x][y]

    def getNeighboursAround(self, x, y):
        neighbors = []

        for sub_x in range(3):
            row = []

            for sub_y in range(3):
                actual_x = x - 1 + sub_x
                actual_y = y - 1 + sub_y
                if (actual_x < 0 or actual_x >= WIN_WIDTH // PIXEL_SIZE or
                    actual_y < 0 or actual_y >= WIN_HEIGHT // PIXEL_SIZE):
                    cell = np.array([1,0])
                else:
                    cell = self.getCell(actual_x, actual_y)

                row.append(cell)

            neighbors.append(row)

        return neighbors

class debugText():
    def __init__(self, screen, clock, *args, **kwargs):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.SysFont("Monospaced", 20)
    
    def printText(self):
        label_frameRate = self.font.render("FPS: " + str(self.clock.get_fps()), 1, (255,255,255))
        self.screen.blit(label_frameRate, (8, 22))

    def update(self, *args, **kwargs):
        self.screen = kwargs.get("screen",self.screen)
        self.clock = kwargs.get("clock",self.clock)
 
def init_grid(grid, background):
    for x in range(0, WIN_WIDTH // PIXEL_SIZE):
        for y in range(0, WIN_HEIGHT // PIXEL_SIZE):
            a_pow = random.random()
            b_pow = 1 - a_pow

            grid.setCell(x, y, np.array([math.sqrt(a_pow),math.sqrt(b_pow)]))
            drawSquare(background, x, y, grid.getCell(x,y))

def drawSquare(background, x, y, array):
    #Cell colour
    value = np.floor((array[1]**2)*255)
    colour = value, value, value
    pygame.draw.rect(background, colour, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))       

def main():
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    clock = pygame.time.Clock()

    isActive = True
    actionDown = False
    
    final = pygame.time.get_ticks()
    grid = Grid()  
    debug = debugText(screen, clock)  

    #Create the orginal grid pattern randomly
    init_grid(grid, background)

    screen.blit(background, (0, 0)) 
    pygame.display.flip()

    while isActive:
        clock.tick(TARGET_FPS)
        newgrid = Grid()

        if pygame.time.get_ticks() - final > REFRESH:
            background.fill((0, 0, 0))

            for x in range(0, WIN_WIDTH // PIXEL_SIZE):
                for y in range(0, WIN_HEIGHT // PIXEL_SIZE):
                    subgrid = grid.getNeighboursAround(x,y)
                    newgrid.setCell(x,y,SQGOL(subgrid))
                    drawSquare(background,x,y,newgrid.getCell(x,y))

            final = pygame.time.get_ticks() 

        else:
            newgrid = grid
            
        debug.update()

        actionDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isActive = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                actionDown = True

                while actionDown:
                    newgrid.setCell(pygame.mouse.get_pos()[0] / PIXEL_SIZE, 
                    	pygame.mouse.get_pos()[1] / PIXEL_SIZE, True)
                    	
                    drawSquare(background, pygame.mouse.get_pos()[0] / PIXEL_SIZE, 
                    	pygame.mouse.get_pos()[1] / PIXEL_SIZE)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            actionDown = False
                    
                    screen.blit(background, (0, 0)) 
                    pygame.display.flip()

        #Draws the new grid
        grid = newgrid       

        #Updates screen
        screen.blit(background, (0, 0)) 
        debug.update()
        debug.printText()
        pygame.display.flip()
       
if __name__ == "__main__":
    main()