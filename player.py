import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: float, y: float, groups=()):
        super().__init__(x, y, PLAYER_RADIUS, groups)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def rotate(self, dt: float) -> None:
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def move(self, dt: float) -> None:
        mov_vector = pygame.Vector2(0, 1).rotate(self.rotation) * (PLAYER_SPEED * dt)
        self.position += mov_vector

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # MOVEMENT
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # ROTATE
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            self.rotate(dt)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle())
