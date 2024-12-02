import pygame, sys
from sudoku_generator import SudokuGenerator
from Cell import Cell

LINE_COLOR = (0, 0, 0)
SQUARE_SIZE = 630
LINE_WIDTH_THICK = 6
LINE_WIDTH_THIN = 2


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_one = None
        self.board = [[Cell(0, i, j, self.screen) for i in range (9)] for j in range (9)]

    def draw(self):
    #sketch values
        for row in self.board:
            for val in row:
                val.draw()
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
        if selected_one != None:
            self.selected_one.selected = False
        self.board[row][col].selected = True
        self.selected_one = self.board[row][col]
        self.draw()


    def click(self, row, col):
        if 0<= row <= self.width and 0<= col <= self.height:
            click_x = row // (SQUARE_SIZE // 9)
            click_y = col // (SQUARE_SIZE // 9)
            return click_x, click_y
        else:
            return None

    def clear(self):
        #only filled by player
        if self.selected_one is not None:
            self.selected_one.set_cell_value(0)
            self.selected_one.set_sketched_value(0)

    def sketch(self, value):
        if self.selected_one is not none:
            self.selected_one.set_sketched_value(value)


    def place_number(self, value):
        #only if event.key == pygame.K_enter
        if self.selected_one:
            self.selected_one.set_cell_value(value)


    def reset_to_original(self):
        for i in range(9):
            for j in range (9):
                if self.board[i][j].selected:
                    self.board[i][j].set_sketched_value(0)
                    self.board[i][j].set_cell_value(0)

    def is_full(self):
        for i in self.board:
            for j in i:
                if self.board[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        # isn't the board continuously updating? 
        pass

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].value == 0:
                    return i, j
        return -1

    def check_board(self):
        if not self.is_full():
            return False
        #rows
        for i in self.board:
            vals = [k.value for k in i]
            for j in vals:
                if vals.count(j) > 1:
                    return False
        #cols
        board_t = [[r[i].value for r in self.board] for i in range(9)]
        for i in board_t:
            for j in i:
                if i.count(j) > 1:
                    return False
        #boxes
        boxes = []
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(self.board[box_row + i][box_col + j].value)
                boxes.append(box)
        for i in boxes:
            for j in i:
                if i.count(j) > 1:
                    return False
        return True






