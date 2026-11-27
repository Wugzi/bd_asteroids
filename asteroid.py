from asyncio.log import logger
import random
import circleshape
import pygame
import constants
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            constants.LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_random_angle = random.uniform(20, 50)
        pos_vector = self.velocity.rotate(new_random_angle)
        neg_vector = self.velocity.rotate(-new_random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = pos_vector * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = neg_vector * 1.2
