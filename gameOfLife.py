from random import randint
import pygame


class GameOfLife(object):
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.cells = 100
        self.board = [[False for _ in range(self.cells)] for _ in range(self.cells)]
        self.cellsize = self.width / 100
        self.alivecells = []
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.width, self.height))

    def addRandomCells(self, alive=[]):
        if alive:
            for col, row in alive:
                try:
                    self.board[row][col] = True
                except:
                    pass

    def randomcells(self):
        return [(randint(1, 99), randint(1, 99)) for _ in range(randint(1, 15))]

    def getNeighbours(self, cell):
        x, y = cell
        count = 0
        neighbours = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x + 1, y), (x + 1, y + 1), (x + 1, y - 1),
                      (x - 1, y + 1),
                      (x, y + 1)]
        for neighbour in neighbours:
            col, row = neighbour
            try:
                if self.board[row][col]:
                    count += 1
            except:
                pass
        return count

    def evolve(self):
        new = [[False for _ in range(self.cells)] for _ in range(self.cells)]

        for row, val in enumerate(self.board):
            for col, val2 in enumerate(val):
                count = self.getNeighbours((col, row))
                if self.board[row][col]:
                    if count > 3 or count < 2:
                        new[row][col] = False
                    else:
                        new[row][col] = True
                else:
                    if count == 3:
                        new[row][col] = True
        self.board = new

    def getAliveCells(self):
        alive = [(x, y) for x in range(len(self.board[0])) for y in range(len(self.board)) if self.board[y][x]]
        return alive

    def draw(self):
        h = 0
        for row in range(self.cells):
            for col in range(self.cells):
                centerX = (col * self.cellsize) + self.cellsize / 2
                centerY = (row * self.cellsize) + self.cellsize / 2
                if self.board[row][col]:
                    pygame.draw.rect(self.surface, (h, 128, 128), (centerX, centerY, self.cellsize, self.cellsize))
                    h = (h + 10) % 255
                else:
                    pygame.draw.rect(self.surface, (0, 0, 0), (centerX, centerY, self.cellsize, self.cellsize))

        pygame.display.update()

    def run(self):
        run = True
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")

        while run:
            self.clock.tick(40)
            self.addRandomCells([(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (4, 4)])
            self.alivecells = self.getAliveCells()
            print(self.alivecells)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_SPACE]:
                        self.addRandomCells(self.randomcells())
                    elif key[pygame.K_ESCAPE]:
                        run = False
                        pygame.display.quit()
            self.draw()
            self.evolve()
            self.alivecells = self.getAliveCells()
            pygame.display.update()
        pygame.quit()


def main():
    app = GameOfLife()
    app.run()


if __name__ == '__main__':
    main()
