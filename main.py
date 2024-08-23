import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    print("Screen width: ", SCREEN_WIDTH)
    print("Screen height: ", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
