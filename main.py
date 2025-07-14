import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


run = True

def main():
    
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    c = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    play = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        updatable.update(dt)
        for i in asteroids:
            if i.collide(play) == True:
                print("Game over!")
                return
            for j in shots:
                if j.collide(i) == True:
                    j.kill()
                    i.split()

        pygame.display.flip()
        dt = c.tick(60)/1000


if __name__ == "__main__":
    main()

