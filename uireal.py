# pygame.event module
# https://www.pygame.org/docs/ref/event.html
#
# Making a clickable grid using Pygame
# https://stackoverflow.com/questions/73835007/making-a-clickable-grid-using-pygame/73835336#73835336
#
# GitHub - Grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_grid.md

import pygame

class Cell:
    def __init__(self):
        self.clicked = False

columns, rows = 10, 4
cell_size = 20

board = [[Cell() for _ in range(columns)] for _ in range(rows)]

pygame.init()
window = pygame.display.set_mode((columns * cell_size, rows * cell_size))
clock = pygame.time.Clock()






Start_Coord = [5, 0]
End_Coord = [2, 2]

def manhattan_distance(a, b):
    return (b[0] - a[0], b[1] - a[1]) # end minus start coord

print(manhattan_distance(Start_Coord, End_Coord))





def fill_cell(board, coords):
    col, row = coords[0], coords[1] # xy
    pygame_row = rows - 1 - row # this line is the result of an hour of pain and torture
    board[pygame_row][col].clicked = True

fill_cell(board, Start_Coord)
fill_cell(board, End_Coord)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill('black')
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            color = (64, 64, 64) if cell.clicked else (164, 164, 164)
            cell_rect = pygame.Rect(ix * cell_size + 1, iy * cell_size + 1, cell_size - 2, cell_size - 2)
            pygame.draw.rect(window, color, cell_rect)
    pygame.display.flip()

pygame.quit()
exit()