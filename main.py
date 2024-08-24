import pygame

from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from groups import asteroids, drawable, updatable
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width: ", SCREEN_WIDTH)
    print("Screen height: ", SCREEN_HEIGHT)

    # INITIALIZATION
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # GAME OBJECTS
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, [updatable, drawable])
    _ = AsteroidField([updatable])

    # UTIL VARIABLES
    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # UPDATE
        for u in updatable:
            u.update(dt)

        # CHECK COLISSIONS
        for a in asteroids:
            if a.collides_with(player):
                print("GAME OVER")
                running = False

        # DRAW
        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
