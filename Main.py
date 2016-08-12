import pygame
import Menu
from gametools.vector2 import Vector2 as vec2
import GameHandler

def main():
    pygame.init()

    width,height = (1280,720)
    screen_size = width, height = (width,height)
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("A Race Against Time")

    handler = GameHandler.GameHandler(screen_size)
    main_menu = Menu.Menu(width,height)

    done = False
    while not done:

        pos = pygame.mouse.get_pos()
        mouse_pos = vec2(pos[0], pos[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        if handler.current_state == "MENU":
            handler.update()
            handler.render(screen)
            option = main_menu.handle_mouse_input(mouse_pos, pygame.mouse.get_pressed())
            if option is not None:
                if option == 1:
                    """Start"""

                elif option == 2:
                    """Quit"""
                    done = True



            main_menu.render(screen)

            pygame.display.update()

        if handler.current_state == "GAME":
            handler.update()
            handler.render(screen)


        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
