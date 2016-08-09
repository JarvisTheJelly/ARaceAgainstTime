import pygame
import GameHandler

def main():
    pygame.init()

    screen_size = width, height = (640, 480)
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("A Race Against Time")

    handler = GameHandler.GameHandler(screen_size)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        handler.update()
        handler.render(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
