import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float, groups=()):
        super().__init__(x, y, radius, groups)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)
