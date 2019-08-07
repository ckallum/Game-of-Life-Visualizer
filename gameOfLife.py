from random import randint


def evolve(board):
    newBoard = initialise()

    for row, val in enumerate(board):
        for col, val2 in enumerate(val):
            count = getNeighbours((col, row), board)
            if board[row][col]:
                if count > 3 or count < 2:
                    newBoard[row][col] = False
                else:
                    newBoard[row][col] = True
            else:
                if count == 3:
                    newBoard[row][col] = True
    return newBoard


def initialise(alive=[]):
    board = [[False for _ in range(50)] for _ in range(50)]
    if alive:
        for col, row in alive:
            try:
                board[row][col] = True
            except:
                pass
    return board


def getAliveCoords(board):
    alive = [(x, y) for x in range(len(board[0])) for y in range(len(board)) if board[y][x]]
    return alive


def getNeighbours(coordinate, board):
    x, y = coordinate
    count = 0
    neighbours = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                  (x, y + 1)]
    for neighbour in neighbours:
        col, row = neighbour
        try:
            if board[row][col]:
                count += 1
        except:
            pass
    if board[y][x]:
        print(count, (x, y))
    return count


def main():
    board = initialise([(0, 10), (0, 1), (1, 0), (1, 1), (4, 4)])
    for _ in range(1000):
        print(getAliveCoords(board))
        board = evolve(board)


if __name__ == '__main__':
    main()
