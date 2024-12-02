import pygame
import sys

from Board import Board

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 630
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
                    x, y = event.pos
                    row = x // (SCREEN_HEIGHT // 9)
                    col = y // (SCREEN_WIDTH // 9)
                    board.select(row, col)

                if event.type == pygame.KEYDOWN:
                    if board.selected_one:
                        if event.key == pygame.K_1:
                            board.sketch(1)
                        elif event.key == pygame.K_2:
                            board.sketch(2)
                        elif event.key == pygame.K_3:
                            board.sketch(3)
                        elif event.key == pygame.K_4:
                            board.sketch(4)
                        elif event.key == pygame.K_5:
                            board.sketch(5)
                        elif event.key == pygame.K_6:
                            board.sketch(6)
                        elif event.key == pygame.K_7:
                            board.sketch(7)
                        elif event.key == pygame.K_8:
                            board.sketch(8)
                        elif event.key == pygame.K_9:
                            board.sketch(9)

                        elif event.type == pygame.K_RETURN:
                            board.place_number()




            # game_success = False
            # game_over_action = game_over_screen(game_success)
            # if game_over_action == "restart":
            #     playing = False


if __name__ == "__main__":
    main()
