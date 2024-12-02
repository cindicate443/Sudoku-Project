import pygame, sys
from sudoku_generator import *
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
        self.original = generate_sudoku(9, {"easy":30,"medium":40,"hard":50}[difficulty])
        self.board = [[Cell(self.original[i][j], i, j, self.screen) for i in range (9)] for j in range (9)]

    def draw(self):
        #vertical
        for i in range (1,3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i* SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height-90),
                LINE_WIDTH_THIN
            )

        for i in range(4, 6):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height-90),
                LINE_WIDTH_THIN
            )

        for i in range(7, 9):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE // 9, 0),
                (i * SQUARE_SIZE // 9, self.height-90),
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
        # CELLS
        for row in self.board:
            for val in row:
                val.draw()
        # RESET
        font = pygame.font.Font(None, 60)
        text = font.render("RESET", True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(30, self.height-60))
        self.screen.blit(text, text_rect)

        # RESTART
        font = pygame.font.Font(None, 60)
        text = font.render("RESTART", True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(220, self.height - 60))
        self.screen.blit(text, text_rect)

        # EXIT
        font = pygame.font.Font(None, 60)
        text = font.render("EXIT", True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(475, self.height - 60))
        self.screen.blit(text, text_rect)



    def select(self, row, col):
        if self.selected_one is not None:
            # Deselect previous selection
            self.selected_one.selected = False
        self.board[row][col].selected = True
        self.selected_one = self.board[row][col]
        self.draw()


    def click(self, row, col):
        if 0<= row <= self.width and 0<= col <= self.height:
            click_x = row // (SQUARE_SIZE // 9)
            click_y = col // (self.height // 10)
            return click_x, click_y
        else:
            return None

    def clear(self):
        #only filled by player
        # cannot change preset cells
        if self.original[self.selected_one.row][self.selected_one.col] != 0:
            return
        if self.selected_one is not None:
            self.selected_one.set_cell_value(0)
            self.selected_one.set_sketched_value(0)

    def sketch(self, value):
        if self.selected_one is not None:
            self.selected_one.set_sketched_value(value)


    def place_number(self):
        #only if event.key == pygame.K_enter
        # cannot change preset cells
        if self.original[self.selected_one.row][self.selected_one.col] != 0:
            return
        if self.selected_one:
            self.selected_one.set_cell_value(self.selected_one.sketched)


    def reset_to_original(self):
        self.board = [[Cell(self.answer[i][j], i, j, self.screen) for i in range(9)] for j in range(9)]
        self.draw()

    def is_full(self):
        for i in self.board:
            for j in i:
                if j.value == 0:
                    return False
        return True

    # not sure about this
    def update_board(self):
        self.draw()

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
