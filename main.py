# This allows us to use code from the open-source pygame library
# throughput this file
import pygame
import constants


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
