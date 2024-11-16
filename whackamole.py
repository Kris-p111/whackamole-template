import pygame
from random import randrange

BOARD_ROWS, BOARD_COLS, SQUARE_SIZE, LINE_WIDTH = 16, 20, 32, 1

def draw_grid(screen):
        pygame.draw.line(
            screen,
            "dark green",
            (0, i*SQUARE_SIZE),
            (640, i*SQUARE_SIZE),
            LINE_WIDTH
        )
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            "dark green",
            (i*SQUARE_SIZE, 0),
            (i*SQUARE_SIZE, 512),
            LINE_WIDTH
        )




def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((640, 512))
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect()

        def randomize_mole():
            mole_rect.topleft = (randrange(0, BOARD_COLS) * SQUARE_SIZE,
                                randrange(0, BOARD_ROWS) * SQUARE_SIZE)
            return mole_rect.topleft

        randomize_mole()
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_col = event.pos[0] // SQUARE_SIZE
                    clicked_row = event.pos[1] // SQUARE_SIZE

                    mole_col = mole_rect.topleft[0] // SQUARE_SIZE
                    mole_row = mole_rect.topleft[1] // SQUARE_SIZE

                    if clicked_col == mole_col and clicked_row == mole_row:
                        randomize_mole()

            screen.fill("light green")

            screen.blit(mole_image, mole_rect.topleft)
            draw_grid(screen)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
