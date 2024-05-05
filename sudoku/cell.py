import pygame


class Cell():
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0
        self.cell_size = 600/9

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 36)
        cell_x = self.col * self.cell_size
        cell_y = self.row * self.cell_size
        # i just made the color for the rectangle beige just so i could actually see the boxes
        #  pygame.draw.rect(self.screen, (245, 245, 220), (cell_x, cell_y, self.cell_size, self.cell_size))
        #  pygame.draw.rect(self.screen, (0, 0, 0), (cell_x, cell_y, self.cell_size, self.cell_size), 2)
        # draws a red outline for the selected cell
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (cell_x, cell_y, self.cell_size, self.cell_size), 2)
        # draws the cell value
        if self.value != 0:
            text = font.render(str(self.value), True, (0,0,0))
            text_rect = text.get_rect(center=(cell_x + self.cell_size // 2, cell_y + self.cell_size // 2))
            self.screen.blit(text, text_rect)
        if self.sketched_value != 0:
            sketched_text = font.render(str(self.sketched_value), True, (128, 128, 128))
            sketched_rect = sketched_text.get_rect(topleft=(cell_x + 5, cell_y + 5))
            self.screen.blit(sketched_text, sketched_rect)



'''pygame.init()
screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cell = Cell(6, 1, 1, screen)
    cell.draw()
    pygame.display.flip()
    clock.tick(60)'''

