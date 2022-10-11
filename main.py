import pygame

# display constant
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space war")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()  # always update display whenever made changes


def main():
    clock = pygame.time.Clock()
    run = True
    # game loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # press X on the top of the pygame window
                run = False
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
