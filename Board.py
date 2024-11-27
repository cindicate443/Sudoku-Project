import pygame, sys
from sudoku_generator import SudokuGenerator
from Cell import Cell

LINE_COLOR = (0, 0, 0)
SQUARE_SIZE = 600
LINE_WIDTH_THICK = 6
LINE_WIDTH_THIN = 2


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.board = [[0 for i in range (9)] for j in range (9)]

    def draw(self):

    #vertical
        for i in range (1,3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i* SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height),
                LINE_WIDTH_THIN
            )

        for i in range(4, 6):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height),
                LINE_WIDTH_THIN
            )

        for i in range(7, 9):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height),
                LINE_WIDTH_THIN
            )

        for i in [3, 6, 9]:
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i* SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height),
                LINE_WIDTH_THICK
                )
    #horizontal
        for i in range(1,3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE // 9),
                (self.width, i * SQUARE_SIZE // 9),
                LINE_WIDTH_THIN
            )
        for i in range(4, 6):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE // 9),
                (self.width, i * SQUARE_SIZE // 9),
                LINE_WIDTH_THIN
                )
        for i in range(7, 9):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE // 9),
                (self.width, i * SQUARE_SIZE // 9),
                LINE_WIDTH_THIN
                )
        for i in [3, 6, 9]:
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE // 9),
                (self.width, i * SQUARE_SIZE // 9),
                LINE_WIDTH_THICK
            )

    def select(self, row, col):
        pass



    def click(self, row, col):
        pass



    def clear(self):
        #only filled by player
        if self.selected:
            self.selected.set_cell_value(0)

    def sketch(self, value):
        if self.selected:
            self.selected.set_sketched_value(value)


    def place_number(self, value):
        #only if event.key == pygame.K_enter
        if self.selected:
            self.selected.set_cell_value(value)


    def reset_to_original(self):
        pass

