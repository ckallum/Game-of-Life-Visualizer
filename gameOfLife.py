from random import randint
import pygame


class GameOfLife(object):
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.board = self.initialise()
        self.cellsize = self.width / 100
        self.cells = 100
        self.alivecells = self.getAliveCells()
        self.clock = pygame.time.Clock()

    def initialise(self, alive=[]):
        board = [[False for _ in range(self.cells)] for _ in range(self.cells)]
        if alive:
            for col, row in alive:
                try:
                    self.board[row][col] = True
                except:
                    pass
        return board

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
        new = self.initialise()

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
        pass

    def run(self):
        run = True
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")

        while run:
            self.draw()
            self.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                elif event.type == pygame.K_SPACE:
                    self.board = self.initialise()
        pygame.quit()


def main():
    app = GameOfLife()
    app.run()


if __name__ == '__main__':
    main()
