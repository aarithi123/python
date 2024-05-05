import pygame
import sudoku_generator
from sudoku_generator import SudokuGenerator
from board import Board
from cell import Cell


def main():
    grid_test = sudoku_generator.generate_sudoku(9, 30)
    print(grid_test)
    for x in range(9):
        for y in range(9):
            print(grid_test[x][y], end=" ")
        print()

if __name__ == "__main__":
    # PROJECT INFO
    '''
    main code: run the game(game start, game over, and game in progress
        opens window w/ difficulty options
            easy: 30 empty cells out of 81
            medium: 40
            hard: 50
        cell selection:
            - can select any cell but only edit empty ones
            - if cell has sketched val, press [enter] to  submit guess
            - select different cels through arrow keys OR mouse
            - when all cells full, but incorrect, GAME OVER
        game buttons:
            - [Reset] = set brd to initial state
            - [Restart] = go to Game Start Screen
            = [Exit] = end program'''

    # constants
    pygame.init()
    screen = pygame.display.set_mode((600, 750))
    pygame.display.set_caption('Sudoku')
    clock = pygame.time.Clock()
    game_page = '1'
    difficulty = 'easy'
    sketch_val = 0
    # texts
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    font = pygame.font.Font(None, 50)
    title_txt = title_font.render('Welcome to Sudoku', True, (255, 255, 255))
    difficulty_txt = title_font.render('Select Game Mode', True, (255, 255, 255))
    win_txt = title_font.render('Game Won', True, (255, 255, 255))

    # button txt
    easy_text = font.render('easy', True, (255, 255, 255), (255, 128, 0))
    medium_text = font.render('medium', True, (255, 255, 255), (255, 128, 0))
    hard_text = font.render('hard', True, (255, 255, 255), (255, 128, 0))
    reset_text = font.render('reset', True, (255, 255, 255), (255, 128, 0))
    restart_text = font.render('restart', True, (255, 255, 255), (255, 128, 0))
    exit_text = font.render('exit', True, (255, 255, 255), (255, 128, 0))

    running = True
    while running:
        #  testing tools
        mouse_pos = pygame.mouse.get_pos()

        # exits window
        for event in pygame.event.get():
            #  exit windows
            if event.type == pygame.QUIT:
                running = False

        #  CHANGES SCREENS
        #  opening screen
        if game_page == '1':
            count = 0
            screen.fill((72, 158, 109))
            screen.blit(title_txt, (300-(315/2), 144))
            screen.blit(difficulty_txt, (150, 344))
            screen.blit(easy_text, (75, 450))
            screen.blit(medium_text, (240, 450))
            screen.blit(hard_text, (450, 450))

            # buttons
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                #  if button pressed, go to board screen
                if 75 < mouse_pos[0] < 150 and 450 < mouse_pos[1] < 530:
                    level = 'easy'
                    game_page = '2'
                    sudoku = SudokuGenerator(9, 30)
                    sudoku.fill_values()
                    player_board = sudoku.get_board()
                    sudoku.remove_cells()
                    board = Board(600, 600, screen, difficulty)
                    board.update_board(player_board)
                if 225 < mouse_pos[0] < 375 and 450 < mouse_pos[1] < 530:
                    level = 'medium'
                    game_page = '2'
                    sudoku = SudokuGenerator(9, 40)
                    sudoku.fill_values()
                    player_board = sudoku.get_board()
                    sudoku.remove_cells()
                    board = Board(600, 600, screen, difficulty)
                if 400 < mouse_pos[0] < 500 and 450 < mouse_pos[1] < 530:
                    level = 'hard'
                    game_page = '2'
                    sudoku = SudokuGenerator(9, 50)
                    sudoku.fill_values()
                    player_board = sudoku.get_board()
                    sudoku.remove_cells()
                    board = Board(600, 600, screen, difficulty)
        # game board
        elif game_page == '2':
            screen.fill((160, 214, 223))
            board.draw()
            # printing numbers
            for col in range(0, 9):
                for row in range(0, 9):
                    pass
                    cell = Cell(player_board[row][col], row, col, screen)
                    cell.draw()
            key = pygame.key.get_pressed()
            if pygame.mouse.get_pressed()[0] and mouse_pos[1] < 600:
                row, col = board.click(mouse_pos[0], mouse_pos[1])
                if row is not None and col is not None:
                    board.select(int(row), int(col))
                    # place_number when user (displays)
                    # clear when sketch del by user
                print(board.selected_cell)
            if key[pygame.K_BACKSPACE]:
                sketch_val = 0
                board.place_number(0) # maybe?
                player_board[board.selected_cell[0]][board.selected_cell[1]] = 0
                board.update_board(player_board)
                #update board
                # print_debug_board(board.cells)
                print(player_board)
            if key[pygame.K_RETURN]:
                board.place_number(sketch_val)
                # player_board[board.selected_cell[0]][board.selected_cell[1]] = sketch_val
                player_board[board.selected_cell[0]][board.selected_cell[1]] = sketch_val
                board.update_board(player_board)
                print(player_board)
                # print_debug_board(board.cells)
                board.sketch(0)

            if key[pygame.K_1]:
                sketch_val = 1
                board.sketch(1)
            if key[pygame.K_2]:
                sketch_val = 2
                board.sketch(2)
            if key[pygame.K_3]:
                sketch_val = 3
                board.sketch(3)
            if key[pygame.K_4]:
                sketch_val = 4
                board.sketch(4)
            if key[pygame.K_5]:
                sketch_val = 5
                board.sketch(5)
            if key[pygame.K_6]:
                sketch_val = 6
                board.sketch(6)
            if key[pygame.K_7]:
                sketch_val = 7
                board.sketch(7)
            if key[pygame.K_8]:
                sketch_val = 8
                board.sketch(8)
            if key[pygame.K_9]:
                sketch_val = 9
                board.sketch(9)
            if key[pygame.K_LEFT] and col > 0:
                col -= 1
            if key[pygame.K_RIGHT] and col < 9:
                col += 1
            if key[pygame.K_UP] and row > 0:
                row -= 1
            if key[pygame.K_DOWN] and row < 9:
                row += 1

            # buttons
            screen.blit(reset_text, (120, 660))
            screen.blit(restart_text, (250, 660))
            screen.blit(exit_text, (400, 660))
            if pygame.mouse.get_pressed()[0]:
                # exit
                if 400 < mouse_pos[0] < 460 and 660 < mouse_pos[1] < 700:
                    running = False
                # restart
                if 250 < mouse_pos[0] < 360 and 660 < mouse_pos[1] < 700:
                    game_page = '1'
                if 120 < mouse_pos[0] < 200 and 660 < mouse_pos[1] < 700:
                    # board.reset_to_original()
                    game_page = '2'
                    if level == 'easy':
                        sudoku = SudokuGenerator(9, 30)
                    elif level == 'medium':
                        sudoku = SudokuGenerator(9, 40)
                    elif level == 'hard':
                        sudoku = SudokuGenerator(9, 50)
                    sudoku.fill_values()
                    player_board = sudoku.get_board()
                    sudoku.remove_cells()
                    board = Board(600, 600, screen, difficulty)
                    board.update_board(player_board)


            if board.is_full():
                print('solved?')
                game_page = '3'

                '''
                #if win_condition: #add the conditions to win
                    game_page = '3'
                #if lose_condition: #add the conditions to loose
                    game_lose = '4'
                    pass'''

        # win
        elif game_page == '3':
            print("a")
            #if win_condition: #add the conditions to win
            if board.check_board(player_board):
                color = (72, 158, 109)
                screen.fill(color)
                # Fonts
                title_font = pygame.font.Font('freesansbold.ttf', 70)
                button_font = pygame.font.Font('freesansbold.ttf', 50)
                # Render the "GAME WON" text in white + center
                surface = title_font.render("Game Won", True, pygame.Color('white'))
                title_area = surface.get_rect(center=(300, 200))
                screen.blit(surface, title_area)
                # Render the "Exit" text in white + center
                surface = button_font.render("Exit", True, pygame.Color('white'))
                button_area = surface.get_rect(center=(300, 600))
                screen.blit(surface, button_area)
                if pygame.mouse.get_pressed()[0]:
                    if 250 < mouse_pos[0] < 350 and 550 < mouse_pos[1] < 650:
                        running = False

            #if lose_condition: #add the conditions to loose
            else:
                color = (72, 158, 109)
                screen.fill(color)
                # Fonts
                title_font = pygame.font.Font('freesansbold.ttf', 70)
                button_font = pygame.font.Font('freesansbold.ttf', 50)
                # Render the "Game Over" text in white + center
                surface = title_font.render("Game Over :(", True, pygame.Color('white'))
                title_area = surface.get_rect(center=(300, 200))
                screen.blit(surface, title_area)
                # Render the "Restart" text in white + center
                surface = button_font.render("Restart", True, pygame.Color('white'))
                button_area = surface.get_rect(center=(300, 600))
                screen.blit(surface, button_area)
                if pygame.mouse.get_pressed()[0]:
                    if 250 < mouse_pos[0] < 350 and 550 < mouse_pos[1] < 650:
                         game_page = '1'

        # testing ctrls
        button = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0]:
            print(mouse_pos)

        # updates screen
        pygame.display.flip()
        #  limits fps = 60
        clock.tick(60)
    pygame.quit()
