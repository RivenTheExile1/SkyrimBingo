import pygame
import sys
import random



def obj_generator():

    ################################ 27 objectives edit this when adding more ####################################################

    objectives = [("Own a Horse", "AA"),("Gain 2 Dragon Souls", "AB"),("Get a Follower", "AC"),("Join the Thieves' Guild", "AD"),("Join the Dark Brotherhood", "AE"),("Get Launched By a Giant", "AF"),("Pick Up the Lusty Argonian", "AG"),("Escape From Jail", "AH"), ("Get One or Two Handed to 40", "AI"),("Join the Civil War", "AJ"),("Acqure one Daedric Artifact", "AK"), ("Eat a Human Heart", "AL"), ("Own a House", "AM"),("Discover 20 Location", "AN"),("Become a Werewolf or Vampire", "AO"),("Learn Bound Bow", "AP"),("Acquire 6000 Gold", "AQ"),("Win a Fist Fight", "AR"),("Go to Jail With a Bounty of 1000+", "AS"),("Unlock 3 Shouts", "AT"),("Discover All Capitals", "AU"),("Kill 2 Giants", "AV"),("Find a Standing Stone (except trio)", "AW"),("Mine 10 Ore Veins", "AX"),("Collect 3 Unusual Gems", "AY"), ("Get Destruction to 40", "AZ"),("Get Archery to 40", "BA"),("Discover High Hrothgar", "BB"),("Full Set of Heavy Armor + Weapon", "BC"),("Join the Companions", "BD"),("Get Two Claws", "BE"),("Join the Mages College", "BF")]


    # list that rando which number in the list gets picked
    x = 0
    chosen_list = []
    while x < 25:
        val = random.randint(0,(len(objectives)-1))
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

    return (objective_list)


def decoder(code):
    
    ################################ 27 objectives edit this when adding more ####################################################
    objectives = [("Own a Horse", "AA"),("Gain 2 Dragon Souls", "AB"),("Get a Follower", "AC"),("Join the Thieves' Guild", "AD"),("Join the Dark Brotherhood", "AE"),("Get Launched By a Giant", "AF"),("Pick Up the Lusty Argonian", "AG"),("Escape From Jail", "AH"), ("Get One or Two Handed to 40", "AI"),("Join the Civil War", "AJ"),("Acqure one Daedric Artifact", "AK"), ("Eat a Human Heart", "AL"), ("Own a House", "AM"),("Discover 20 Location", "AN"),("Become a Werewolf or Vampire", "AO"),("Learn Bound Bow", "AP"),("Acquire 6000 Gold", "AQ"),("Win a Fist Fight", "AR"),("Go to Jail With a Bounty of 1000+", "AS"),("Unlock 3 Shouts", "AT"),("Discover All Capitals", "AU"),("Kill 2 Giants", "AV"),("Find a Standing Stone (except trio)", "AW"),("Mine 10 Ore Veins", "AX"),("Collect 3 Unusual Gems", "AY"), ("Get Destruction to 40", "AZ"),("Get Archery to 40", "BA"),("Discover High Hrothgar", "BB"),("Full Set of Heavy Armor + Weapon", "BC"),("Join the Companions", "BD"),("Get Two Claws", "BE"),("Join the Mages College", "BF")]

    x = 0
    code_list = []
    while x < 25:
        val = code[x*2]  + code[(x*2) + 1]
        code_list.append(val)
        x = x + 1

    print (code_list)

    return_list = []
    for code_val in code_list:
        for obj in objectives:
            if code_val == obj[1]:
                return_list.append(obj)
    
    return (return_list)
    




def main(screen, code):

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
    rect6 = pygame.Rect(240, 0, 240, 200)
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

    if code == "":
        objective_list = obj_generator()
    else:
        objective_list = decoder(code)

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if rect1.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))

                    
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

                if rect2.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))

                    #
                    if rect2_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect2)  #
                        text = objective_list[1]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,200)
                        screen.blit(button_text_surface, button_text_rect)
                        rect2_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect2)  #
                        text = objective_list[1]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect2_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect3.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect3_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect3)  #
                        text = objective_list[2]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect3_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect3)  #
                        text = objective_list[2]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect3_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect4.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect4_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect4)  #
                        text = objective_list[3]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect4_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect4)  #
                        text = objective_list[3]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect4_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


            
                if rect5.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect5_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect5)  #
                        text = objective_list[4]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect5_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect5)  #
                        text = objective_list[4]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (0,800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect5_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()



                if rect6.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect6_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect6)  #
                        text = objective_list[5]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect6_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect6)  #
                        text = objective_list[5]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect6_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                
                if rect7.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect7_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect7)  #
                        text = objective_list[6]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect7_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect7)  #
                        text = objective_list[6]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect7_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()



                if rect8.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect8_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect8)  #
                        text = objective_list[7]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect8_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect8)  #
                        text = objective_list[7]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect8_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect9.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect9_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect9)  #
                        text = objective_list[8]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect9_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect9)  #
                        text = objective_list[8]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect9_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                    
                if rect10.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect10_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect10)  #
                        text = objective_list[9]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect10_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect10)  #
                        text = objective_list[9]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (240,800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect10_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                if rect11.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect11_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect11)  #
                        text = objective_list[10]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480, 0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect11_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect11)  #
                        text = objective_list[10]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480,0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect11_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                
                if rect12.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect12_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect12)  #
                        text = objective_list[11]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480, 200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect12_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect12)  #
                        text = objective_list[11]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480,200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect12_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()



                if rect13.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect13_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect13)  #
                        text = objective_list[12]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480, 400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect13_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect13)  #
                        text = objective_list[12]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480,400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect13_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect14.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect14_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect14)  #
                        text = objective_list[13]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480, 600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect14_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect14)  #
                        text = objective_list[13]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480,600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect14_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect15.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect15_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect15)  #
                        text = objective_list[14]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect15_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect15)  #
                        text = objective_list[14]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (480, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect15_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect16.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect16_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect16)  #
                        text = objective_list[15]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect16_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect16)  #
                        text = objective_list[15]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect16_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                if rect17.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect17_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect17)  #
                        text = objective_list[16]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect17_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect17)  #
                        text = objective_list[16]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect17_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                if rect18.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect18_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect18)  #
                        text = objective_list[17]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect18_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect18)  #
                        text = objective_list[17]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect18_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                
                if rect19.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect19_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect19)  #
                        text = objective_list[18]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect19_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect19)  #
                        text = objective_list[18]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect19_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect20.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect20_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect20)  #
                        text = objective_list[19]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect20_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect20)  #
                        text = objective_list[19]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (720, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect20_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                if rect21.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect21_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect21)  #
                        text = objective_list[20]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect21_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect21)  #
                        text = objective_list[20]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 0)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect21_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                if rect22.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect22_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect22)  #
                        text = objective_list[21]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect22_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect22)  #
                        text = objective_list[21]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 200)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect22_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()

                if rect23.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect23_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect23)  #
                        text = objective_list[22]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect23_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect23)  #
                        text = objective_list[22]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 400)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect23_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()



                if rect24.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect24_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect24)  #
                        text = objective_list[23]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect24_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect24)  #
                        text = objective_list[23]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 600)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect24_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()


                if rect25.collidepoint(mouse_pos):#
                    # prints current location of mouse
                    print('button1 was pressed at {0}'.format(mouse_pos))


                    if rect25_color == "blue":#
                        pygame.draw.rect(screen, [255, 0, 0], rect25)  #
                        text = objective_list[24]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect25_color = "red"#
                        pygame.display.update()
                        pygame.display.flip()
                        
                    else:
                        pygame.draw.rect(screen, [0, 0, 255], rect25)  #
                        text = objective_list[24]#
                        button_text_surface = FONT.render(text[0], True, [0,0,0])
                        button_text_rect = button_text_surface.get_rect()
                        button_text_rect.topleft = (960, 800)#
                        screen.blit(button_text_surface, button_text_rect)
                        rect25_color = "blue"#
                        pygame.display.update()
                        pygame.display.flip()
                



            if event.type == pygame.QUIT: 
                running = False


       

        
        


        
       
        

                        

