import pygame
from cell import Cell


class Board():
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_size = 50
        # creates an array to represent the sudoku board with Cell objects
        self.cells = []
        for row in range(0, 9):
            row_cells = []
            for col in range(0, 9):
                cell = Cell(0, row, col, self.screen)
                row_cells.append(cell)
            self.cells.append(row_cells)
        # this will be used in other methods
        self.selected_cell = None

    def draw(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.draw()
        # draws bold lines for the 3x3 boxes
        # draw horizontal bold lines
        line_width = 1
        for i in range(0, 10):
            if i % 3 == 0:
                line_width = 5
            else:
                line_width = 1
            pygame.draw.rect(self.screen, 'black', (0 + (i * (self.width / 9)), 0, line_width, self.width))
            pygame.draw.rect(self.screen, 'black', (0, 0 + (i * (self.width / 9)), self.width, line_width))

    def select(self, row, col):
        # marks the cell at (row, col) as the current selected cell
        self.selected_cell = (row, col)

    def click(self, x, y):
        # returns a tuple of the (row, cell) that was clicked on
        cell_size = self.cells[0][0].cell_size
        col = x // cell_size
        row = y // cell_size
        if 0 <= row < 9 and 0 <= col < 9:
            return row, col
        else:
            return None

    def clear(self):
        # clears the value of the current selected cell
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_cell_value(0)

    def sketch(self, value):
        # sets the sketched value of the current selected cell
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        # sets the value of the current selected cell
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_cell_value(value)

    def reset_to_original(self):
        # resets all cells to their original values
        for row in range(0, 9):
            for col in range(0, 9):
                cell = self.cells[row][col]
                cell.set_cell_value(0)
                cell.set_sketched_value(0)

    def is_full(self):
        # returns True if the board is full and False if not
        for row in range(0, 9):
            for col in range(0, 9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self, underlying_board):
        # updates the underlying 2D board with the values in all cells
        for row in range(0, 9):
            for col in range(0, 9):
                cell = self.cells[row][col]
                # I'm not really sure what the underlying board is so this is probably wrong
                cell.value = underlying_board[row][col]

    def find_empty(self):
        # finds an empty cell and returns its row and col as a tuple (x,y)
        for row in range(0, 9):
            for col in range(0, 9):
                if self.cells[row][col].value == 0:
                    return row, col

    def check_board(self):
        # checks whether the Sudoku board is solved correctly
        for row in range(9):
            for col in range(9):
                # I don't know what to do from here since i don't know what the solution for the Sudoku board is or where we are storing that yet
                pass
