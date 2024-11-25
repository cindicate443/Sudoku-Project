import pygame
from sudoku_generator import SudokuGenerator
from Cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None


    def draw(self):

    def select(self, row, col):


    def click(self, row, col):



    def clear(self):
        if self.selected:
            self.selected.set_cell_value(0)

    def sketch(self, value):
        if self.selected:
            self.selected.set_sketched_value(value)

    def place_number(self, value):
        if self.selected:
            self.selected.set_cell_value(value)

    def reset_to_original(self):