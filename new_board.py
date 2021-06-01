import pygame
import sys
import random

class board_generation:


    def main(self, screen):
        self.screen = screen

        random.seed()
        pygame.init()
        
        FONT = pygame.font.Font(None, 20)


        size = (1200, 1000)
        bg = (255, 255, 255)
        screen = pygame.display.set_mode(size)
        
        screen.fill(bg)
        pygame.display.update()
        pygame.display.flip()


        rect1 = pygame.Rect(0, 0, 240, 200)
        rect2 = pygame.Rect(0, 200, 240, 200)
        rect3 = pygame.Rect(0, 400, 240, 200)
        rect4 = pygame.Rect(0, 600, 240, 200)
        rect5 = pygame.Rect(0, 800, 240, 200)
        rect6 = pygame.Rect(240, 0, 240, 2000)
        rect7 = pygame.Rect(240, 200, 240, 200)
        rect8 = pygame.Rect(240, 400, 240, 200)
        rect9 = pygame.Rect(240, 600, 240, 200)
        rect10 = pygame.Rect(240, 800, 240, 200)
        rect11 = pygame.Rect(480, 0, 240, 200)
        rect12 = pygame.Rect(480, 200, 240, 200)
        rect13 = pygame.Rect(480, 400, 240, 200)
        rect14 = pygame.Rect(480, 600, 240, 200)
        rect15 = pygame.Rect(480, 800, 240, 200)
        rect16 = pygame.Rect(720, 0, 240, 200)
        rect17 = pygame.Rect(720, 200, 240, 200)
        rect18 = pygame.Rect(720, 400, 240, 200)
        rect19 = pygame.Rect(720, 600, 240, 200)
        rect20 = pygame.Rect(720, 800, 240, 200)
        rect21 = pygame.Rect(960, 0, 240, 200)
        rect22 = pygame.Rect(960, 200, 240, 200)
        rect23 = pygame.Rect(960, 400, 240, 200)
        rect24 = pygame.Rect(960, 600, 240, 200)
        rect25 = pygame.Rect(960, 800, 240, 200)


        objectives = [("Own a Horse", "AA"),("Gain 2 Dragon Souls", "AB"),("Get a Follower", "AC"),("Join the Thieves' Guild", "AD"),("Join the Dark Brotherhood", "AE"),("Get Launched By a Giant", "AF"),("Pick Up the Lusty Argonian", "AG"),("Escape From Jail", "AH"), ("Get One or Two Handed to 40", "AI"),("Join the Civil War", "AJ"),("Acqure one Daedric Artifact", "AK"), ("Eat a Human Heart", "AL"), ("Own a House", "AM"),("Discover 20 Location", "AN"),("Become a Werewolf or Vampire", "AO"),("Learn Bound Bow", "AP"),("Acquire 6000 Gold", "AQ"),("Win a Fist Fight", "AR"),("Go to Jail With a Bounty of 1000+", "AS"),("Unlock 3 Shouts", "AT"),("Discover All Capitals", "AU"),("Kill 2 Giants", "AV"),("Find a Standing Stone (except trio)", "AW"),("Mine 10 Ore Veins", "AX"),("Collect 3 Unusual Gems", "AY"), ("Get Destruction to 40", "AZ"),("Get Archery to 40", "BA")]


        # list that rando which number in the list gets picked
        x = 0
        chosen_list = []
        while x < 25:
            val = random.randint(0,26)
            if val in chosen_list:
                x = x 
            else:
                chosen_list.append(val)
                x = x + 1

        #gets the list of objectives in random order
        objective_list = []
        print(chosen_list)
        for val in chosen_list:
            obj = objectives[val]
            objective_list.append(obj)
        print(objective_list)

        #generates code
        lt_code = ""
        for val in objective_list:
            lt_code = lt_code + val[1]
    
        print("code: ", lt_code)    

        pygame.draw.rect(screen, [255, 0, 0], rect1)  

        text = objective_list[0]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (0,0)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect2)  

        text = objective_list[1]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (0,200)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect3)  

        text = objective_list[2]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (0,400)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect4)  

        text = objective_list[3]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (0,600)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect5)  

        text = objective_list[4]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (0,800)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect6)  

        text = objective_list[5]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (240,0)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect7)  

        text = objective_list[6]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (240,200)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect8)  

        text = objective_list[7]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (240,400)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect9)  

        text = objective_list[8]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (240,600)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect10)  

        text = objective_list[9]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (240,800)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect11)  

        text = objective_list[10]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (480,0)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect12)  

        text = objective_list[11]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (480,200)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect13)  

        text = objective_list[12]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (480,400)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect14)  

        text = objective_list[13]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (480,600)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect15)  

        text = objective_list[14]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (480,800)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect16)  

        text = objective_list[15]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (720,0)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect17)  

        text = objective_list[16]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (720,200)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect18)  

        text = objective_list[17]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (720,400)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect19)  

        text = objective_list[18]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (720,600)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect20)  

        text = objective_list[19]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (720,800)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect21)  

        text = objective_list[20]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (960,0)
        screen.blit(button_text_surface, button_text_rect)
        
        pygame.draw.rect(screen, [255, 0, 0], rect22)  

        text = objective_list[21]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (960,200)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect23)  

        text = objective_list[22]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (960,400)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect24)  

        text = objective_list[23]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (960,600)
        screen.blit(button_text_surface, button_text_rect)

        pygame.draw.rect(screen, [255, 0, 0], rect25)  

        text = objective_list[24]
        button_text_surface = FONT.render(text[0], True, [0,0,0])
        button_text_rect = button_text_surface.get_rect()
        button_text_rect.topleft = (960,800)
        screen.blit(button_text_surface, button_text_rect)


        

        pygame.display.update()
        pygame.display.flip()

        rect1_color = "red"
        rect2_color = "red"
        rect3_color = "red"
        rect4_color = "red"
        rect5_color = "red"
        rect6_color = "red"
        rect7_color = "red"
        rect8_color = "red"
        rect9_color = "red"
        rect10_color = "red"
        rect11_color = "red"
        rect12_color = "red"
        rect13_color = "red"
        rect14_color = "red"
        rect15_color = "red"
        rect16_color = "red"
        rect17_color = "red"
        rect18_color = "red"
        rect19_color = "red"
        rect20_color = "red"
        rect21_color = "red"
        rect22_color = "red"
        rect23_color = "red"
        rect24_color = "red"
        rect25_color = "red"


        running = True
        while running:
           
            for event in pygame.event.get():
                print(rect1_color, "test1")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position

                    # checks if mouse position is over the button
 
                    if rect1.collidepoint(mouse_pos):
                        # prints current location of mouse
                        print('button1 was pressed at {0}'.format(mouse_pos))

                        print (rect1_color)
                        if rect1_color == "blue":
                            pygame.draw.rect(screen, [255, 0, 0], rect1)  
                            text = objective_list[0]
                            button_text_surface = FONT.render(text[0], True, [0,0,0])
                            button_text_rect = button_text_surface.get_rect()
                            button_text_rect.topleft = (0,0)
                            screen.blit(button_text_surface, button_text_rect)
                            rect1_color = "red"
                            print("in if", rect1_color)
                            pygame.display.update()
                            pygame.display.flip()
                            
                        else:
                            pygame.draw.rect(screen, [0, 0, 255], rect1)  
                            text = objective_list[0]
                            button_text_surface = FONT.render(text[0], True, [0,0,0])
                            button_text_rect = button_text_surface.get_rect()
                            button_text_rect.topleft = (0,0)
                            screen.blit(button_text_surface, button_text_rect)
                            rect1_color = "blue"
                            pygame.display.update()
                            pygame.display.flip()

                    #copy the above if event for all 24 things. there are alot of minor shits to edits. its 4 am i am not doing anynmore



                if event.type == pygame.QUIT: 
                    running = False

       

        
        


        
       
        

                        

