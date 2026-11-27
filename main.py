import logger
import pygame
from pygame.display import update
from asteroid import Asteroid
import constants
from logger import log_event, log_state
from shot import Shot
from player import Player
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(
        f"Screen width: {constants.SCREEN_WIDTH}\n" 
        f"Screen height: {constants.SCREEN_HEIGHT}"
    )
    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, 
         constants.SCREEN_HEIGHT)
    )
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(
        constants.SCREEN_WIDTH / 2,
        constants.SCREEN_HEIGHT / 2
    )
    asteroid_field = AsteroidField()
    while True:
        logger.log_state()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for object in asteroids:
            if object.collides_with(player):
                logger.log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for object in asteroids:
            for shot in shots:
                if object.collides_with(shot):
                    logger.log_event("asteroid_shot")
                    object.split()
                    shot.kill()
        for object in drawable:
            object.draw(screen)  
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
