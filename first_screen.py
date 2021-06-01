
import pygame
import new_board
import sys


def main():
    pygame.init()

    FONT = pygame.font.Font(None, 20)


    size = (600, 600)
    bg = (255, 255, 255)
    button_topleft = (100,100)
    button2_topleft = (400,100)
    screen = pygame.display.set_mode(size)
    screen.fill(bg)
    pygame.display.flip()

    button1 = pygame.Rect(100, 100, 100, 50)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom
    

    button2 = pygame.Rect(400, 100, 100, 50) 

    print("If you are using a code enter it in the command line.")


    pygame.draw.rect(screen, [255, 0, 0], button1)  # draw button1

    button_text_surface = FONT.render("Make New Board", True, [0,0,0])
    button_text_rect = button_text_surface.get_rect()
    button_text_rect.topleft = button_topleft
    screen.blit(button_text_surface, button_text_rect)


    pygame.draw.rect(screen, [0, 255, 0], button2)  # draw button1

    button2_text_surface = FONT.render("Enter Code", True, [0,0,0])
    button2_text_rect = button2_text_surface.get_rect()
    button2_text_rect.topleft = button2_topleft
    screen.blit(button2_text_surface, button2_text_rect)


    running = True
    while running:
        
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button1.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    screen.fill(bg)
                    pygame.display.flip()
                    code = ""
                    rando_board = new_board.main(screen, code)

        
                if button2.collidepoint(mouse_pos):
                    print("button2 was pressed, enter your code")

                    code = input("Enter your code here: ")

                    rando_board = new_board.main(screen, code)


            if event.type == pygame.QUIT: 
                running = False

        pygame.display.update()

sys.exit

main()