import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from groups import asteroids, drawable, updatable


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius, groups=()):
        super().__init__(x, y, radius, groups)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        r_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a = self.velocity.rotate(r_angle)
        b = self.velocity.rotate(-r_angle)

        _ = Asteroid(
            self.position.x,
            self.position.y,
            new_radius,
            [asteroids, updatable, drawable],
        ).velocity = a * 1.2
        _ = Asteroid(
            self.position.x,
            self.position.y,
            new_radius,
            [asteroids, updatable, drawable],
        ).velocity = b * 1.2

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
