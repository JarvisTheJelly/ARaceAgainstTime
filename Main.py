import pygame
import Menu
from gametools.vector2 import Vector2 as vec2
import GameHandler

def main():
    pygame.init()

    screen_size = width, height = (1280, 720)
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("A Race Against Time")

    handler = GameHandler.GameHandler(screen_size)
    handler.current_state = "GAME"
    main_menu = Menu.Menu(width, height)

    boost_speed = 50

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
                if option == 0:
                    """Start"""
                    print "Start"

                elif option == 1:
                    """Quit"""
                    done = True

            main_menu.render(screen)

            pygame.display.update()

        if handler.current_state == "GAME":

            if pygame.key.get_pressed()[pygame.K_w]:
                boost_speed += 0.5
            elif pygame.key.get_pressed()[pygame.K_s]:
                boost_speed -= 0.5

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                handler.update(boost_speed)
            else:
                handler.update()

            handler.render(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
