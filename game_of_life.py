# gol

'''
Implement game of life -> https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

'''

import random

MAX_COL = 25
MAX_ROW = 40


matrix = [[0 for i in range(MAX_COL)] for j in range(MAX_ROW)]
new_matrix = [[0 for i in range(MAX_COL)] for j in range(MAX_ROW)]


for i in range(MAX_ROW):
    for j in range(MAX_COL):
        matrix[i][j] = random.randint(0,1)

def printGrid(matrix):
    for i in range(MAX_ROW):
        print(matrix[i])

printGrid(matrix)

def getsum(grid, x, y):

    # (0 - 1 + 10) % 10 => 9
    # (9 + 1 + 10) % 10 => 0

    sum = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            sum += matrix[(x + i + 10) % 10][(y + j + 10) % 10]

    return sum

def getNextGen(matrix):
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            sum = getsum(matrix, i, j)

            #  rule #1
            if (matrix[i][j] and sum < 2):
                new_matrix[i][j] = 0
            # rule #2
            elif (matrix[i][j] and (sum == 2 or sum ==3)):
                new_matrix[i][j] = 1
            # rule #3
            elif (matrix[i][j] and sum > 3):
                new_matrix[i][j] = 0
            # rule #4
            elif (not matrix[i][j] and sum == 3):
                new_matrix[i][j] = 1

            else:
                new_matrix[i][j] = matrix[i][j]

    return new_matrix


for i in range(10):
    print('\n-------------------------\n')
    matrix = getNextGen(matrix)
    printGrid(matrix)
