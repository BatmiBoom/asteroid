import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float, groups):
        super().__init__(groups)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other) -> bool:
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: float):
        pass
