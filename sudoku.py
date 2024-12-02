import pygame
import sys

from pygame import K_RETURN, K_BACKSPACE

from Board import Board

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")
font = pygame.font.Font(None, 40)


def start_screen():
    screen.fill(BACKGROUND_COLOR)
    title = font.render("Welcome to Sudoku!", True, FONT_COLOR)
    easy_button = font.render("Easy", True, FONT_COLOR)
    medium_button = font.render("Medium", True, FONT_COLOR)
    hard_button = font.render("Hard", True, FONT_COLOR)

    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))
    screen.blit(easy_button, (SCREEN_WIDTH // 2 - easy_button.get_width() // 2, 200))
    screen.blit(medium_button, (SCREEN_WIDTH // 2 - medium_button.get_width() // 2, 300))
    screen.blit(hard_button, (SCREEN_WIDTH // 2 - hard_button.get_width() // 2, 400))

    pygame.display.flip()
    difficulty = None

    while not difficulty:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 <= y <= 250:
                    difficulty = "easy"
                elif 300 <= y <= 350:
                    difficulty = "medium"
                elif 400 <= y <= 450:
                    difficulty = "hard"

    return difficulty


def game_over_screen(success):
    screen.fill(BACKGROUND_COLOR)
    if success:
        message = font.render("Congratulations, You Won!", True, FONT_COLOR)
    else:
        message = font.render("Game Over. Try Again!", True, FONT_COLOR)

    screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    restart_button = font.render("Restart", True, FONT_COLOR)
    exit_button = font.render("Exit", True, FONT_COLOR)

    screen.blit(restart_button, (SCREEN_WIDTH // 2 - restart_button.get_width() // 2, 400))
    screen.blit(exit_button, (SCREEN_WIDTH // 2 - exit_button.get_width() // 2, 500))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 400 <= y <= 450:
                    return "restart"
                elif 500 <= y <= 550:
                    pygame.quit()
                    sys.exit()



def main():
    """ Main function to run the Sudoku game."""
    running = True

    while running:

        difficulty = start_screen()

        removed_cells = {"easy": 30, "medium": 40, "hard": 50}.get(difficulty, 30)

        board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, screen, difficulty)

        playing = True
        while playing:
            screen.fill(BACKGROUND_COLOR)
            board.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    cell_col, cell_row = board.click(x,y)
                    # BUTTONS
                    if cell_row == 9:
                        # RESET
                        if cell_col < 3:
                            board.reset_to_original()
                        # RESTART
                        elif cell_col < 6:
                            main()
                        # EXIT
                        else:
                            quit()
                    else:
                        board.select(cell_row, cell_col)

                if event.type == pygame.KEYDOWN:
                    r = board.selected_one.row
                    c = board.selected_one.col
                    if event.key == pygame.K_RIGHT:
                        if r != 8:
                            board.select(r, c+1)
                    elif event.key == pygame.K_LEFT:
                        if board.selected_one.row != 0:
                            board.select(r, c-1)
                    elif event.key == pygame.K_UP:
                        if board.selected_one.row != 0:
                            board.select(r-1, c)
                    elif event.key == pygame.K_DOWN:
                        if board.selected_one.row != 8:
                            board.select(r+1, c)


                    # Enter
                    if event.key == K_RETURN:
                        board.place_number()
                    # Backspace
                    elif event.key == K_BACKSPACE:
                        board.clear()
                    # Numbers
                    key_to_num = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5,
                                  pygame.K_6: 6, pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9}
                    value = key_to_num.get(event.key, 0) # 0 if random key is pressed
                    board.sketch(value)

            # Win Checking
            if board.is_full():
                game_success = board.check_board()
                game_over_action = game_over_screen(game_success)
                if game_over_action == "restart":
                    main()


if __name__ == "__main__":
    main()
