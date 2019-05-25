import pygame, copy, math, random
import numpy as np
from qrules import SQGOL
pygame.init()

PIXEL_SIZE = 5
WIN_WIDTH = 640
WIN_HEIGHT = 480
Y_LIMIT = WIN_HEIGHT // PIXEL_SIZE
X_LIMIT = WIN_WIDTH // PIXEL_SIZE

#Update every 2ms
REFRESH = 2
TARGET_FPS = 60

class Grid():
    def __init__(self, *args, **kwargs):
        self.grid = [[np.array([1,0]) for i in range(Y_LIMIT)] for i in range(X_LIMIT)]

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
                if actual_x < 0:
                    actual_x = X_LIMIT + actual_x
                elif actual_x >= X_LIMIT:
                    actual_x -= X_LIMIT

                actual_y = y - 1 + sub_y
                if actual_y < 0:
                    actual_y = Y_LIMIT + actual_y
                elif actual_y >= Y_LIMIT:
                    actual_y -= Y_LIMIT

                cell = self.getCell(actual_x, actual_y)

                row.append(cell)

            neighbors.append(row)

        return neighbors

    def countNeighbours(self, x, y):
        neighbours = self.getNeighboursAround(x,y)

        count = 0
        for x in range(3):
            for y in range(3):
                if x == 1 and y == 1:
                    continue
    
                count += 1 if (neighbours[x][y] == np.array([0.,1.])).all() else 0

        return count

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

def init_grid(grid, background, grid2, background2):
    for x in range(X_LIMIT):
        for y in range(Y_LIMIT):
            a = random.random()
            b = math.sqrt(1 - a**2)

            grid.setCell(x, y, np.array([a,b]))
            drawSquare(background, x, y, grid.getCell(x,y))

            if b >= 0.5:
                grid2.setCell(x, y, np.array([0,1]))
                drawSquareClassic(background2, x, y)
            else:
                grid2.setCell(x, y, np.array([1,0]))
                drawSquareClassic(background2, x, y)

def drawSquare(background, x, y, array):
    #Cell colour
    value = 255.0 - np.floor((array[1]**2)*255)
    colour = value, value, value
    pygame.draw.rect(background, colour, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def drawBlankSpace(background, x, y):
    #Random cell colour
    colour = (40,40,40)
    pygame.draw.rect(background, colour, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def drawSquareClassic(background, x, y):
    colour = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    pygame.draw.rect(background, colour, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def main():
    screen = pygame.display.set_mode((2*WIN_WIDTH+100, WIN_HEIGHT))

    background_Final = pygame.Surface(screen.get_size())

    rect_quantum = pygame.Rect(0,0,WIN_WIDTH,WIN_HEIGHT)
    background_quantum = background_Final.subsurface(rect_quantum)
    background_quantum = background_quantum.convert()
    background_quantum.fill((0, 0, 0))

    rect_interspace = pygame.Rect(WIN_WIDTH+100,0,100,WIN_HEIGHT)
    interspace = background_Final.subsurface(rect_interspace)
    interspace = interspace.convert()
    interspace.fill((0, 0, 0))

    for x in range(0, 100 // PIXEL_SIZE):
        for y in range(0, WIN_HEIGHT // PIXEL_SIZE):
            drawBlankSpace(interspace, x, y)

    rect_classical = pygame.Rect(WIN_WIDTH+100,0,WIN_WIDTH,WIN_HEIGHT)
    background_classical = background_Final.subsurface(rect_classical)
    background_classical = background_classical.convert()
    background_classical.fill((0, 0, 0))

    clock = pygame.time.Clock()

    isActive = True
    actionDown = False

    final = pygame.time.get_ticks()
    grid_quantum = Grid()
    grid_classical = Grid()
    debug = debugText(screen, clock)

    #Create the orginal grid pattern randomly
    init_grid(grid_quantum, background_quantum, grid_classical, background_classical)

    screen.blit(background_classical, (0, 0))
    screen.blit(interspace, (WIN_WIDTH, 0))
    screen.blit(background_quantum, (WIN_WIDTH+100, 0))
    pygame.display.flip()

    while isActive:
        clock.tick(TARGET_FPS)
        newgrid_quantum = Grid()
        newgrid_classical = Grid()

        if pygame.time.get_ticks() - final > REFRESH:
            background_quantum.fill((0, 0, 0))
            background_classical.fill((0, 0, 0))

            for x in range(0, X_LIMIT):
                for y in range(0, Y_LIMIT):
                    subgrid = grid_quantum.getNeighboursAround(x, y)
                    newgrid_quantum.setCell(x, y, SQGOL(subgrid))
                    drawSquare(background_quantum, x, y, newgrid_quantum.getCell(x,y))
					#Classic game of life
                    if (grid_classical.getCell(x, y) == np.array([0,1])).all():
                        if grid_classical.countNeighbours(x, y) < 2:
                            grid_classical.setCell(x, y, np.array([1,0]))

                        elif grid_classical.countNeighbours(x, y) <= 3:
                            newgrid_classical.setCell(x, y, np.array([0,1]))
                            drawSquareClassic(background_classical, x, y)

                        elif grid_classical.countNeighbours(x, y) >= 4:
                            newgrid_classical.setCell(x, y, np.array([1,0]))
                    else:
                        if grid_classical.countNeighbours(x, y) == 3:
                            newgrid_classical.setCell(x, y, np.array([0,1]))
                            drawSquareClassic(background_classical, x, y)

            final = pygame.time.get_ticks()

        else:
            newgrid_quantum = grid_quantum
            newgrid_classical = grid_classical

        debug.update()

        actionDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isActive = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                actionDown = True

                while actionDown:
                    x = pygame.mouse.get_pos()[0] // PIXEL_SIZE
                    y = pygame.mouse.get_pos()[1] // PIXEL_SIZE
                    newgrid.setCell(x, y, np.array([0,1]))
                    drawSquare(background, x, y, newgrid.getCell(x,y))

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            actionDown = False

                    screen.blit(background, (0, 0))
                    pygame.display.flip()

        #Draws the new grid
        grid_quantum = newgrid_quantum
        grid_classical = newgrid_classical

        #Updates screen
        screen.blit(background_classical, (0, 0))
        screen.blit(interspace, (WIN_WIDTH, 0))
        screen.blit(background_quantum, (WIN_WIDTH+100, 0))
        debug.update()
        debug.printText()
        pygame.display.flip()

if __name__ == "__main__":
    main()
