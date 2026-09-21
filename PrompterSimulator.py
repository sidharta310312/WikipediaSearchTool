import pygame
import pywhatkit
import time
import os
import sys
import string

#init functions
def killmyself():
    pygame.quit()
    sys.exit()

app_name = "WikiPrompt [BETA]"

pygame.init()

pygame.display.set_caption(app_name)

#init colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,0)

#init screen
screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)

#init fonts
title_font = pygame.font.SysFont("cambriamath", 50)
start_font = pygame.font.SysFont("couriernew", 20)
input_font = pygame.font.SysFont("Consolas", 30)

#init hahafunni effect
hahafunni_Y = 0
hahafunni_rect = pygame.Rect(0, hahafunni_Y, screen_size[0], 1)
hahafunni_trailmargin = 10

#init user input
letters = string.ascii_uppercase + string.digits
typable_keys = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
user_prompt = ""
answer = "placeholder"
info_reveal = 4

loop = True
TitleScreen = True
outputting = False

while loop:
    screen.fill(black)

    hahafunni_rect = pygame.Rect(0, hahafunni_Y, screen_size[0], 10)
    pygame.draw.rect(screen, green, hahafunni_rect)

    #make hahafunni trails
    for i in range(10):
        pygame.draw.rect(screen, green, pygame.Rect(0, hahafunni_Y - (i * hahafunni_trailmargin), screen_size[0], 10 - i))

    hahafunni_Y += 5

    time.sleep(0.01)
    
    if hahafunni_Y >= screen_size[1]:
        hahafunni_Y = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            killmyself()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and TitleScreen:
            TitleScreen = False
            user_prompt = ""
        if event.type == pygame.KEYDOWN and not TitleScreen and not outputting:
            if event.key in typable_keys:
                keyindex = typable_keys.index(event.key)
                user_prompt = user_prompt + letters[keyindex]
            elif event.key == pygame.K_SPACE:
                user_prompt = user_prompt + " "
            elif event.key == pygame.K_BACKSPACE and len(user_prompt) > 0:
                user_prompt = user_prompt[:-1]
            elif event.key == pygame.K_RETURN and user_prompt != "":
                outputting = True
        if event.type == pygame.KEYDOWN and outputting and not TitleScreen:
            if event.key == pygame.K_SPACE:
                info_reveal += 4
        
        

    if TitleScreen:
        title = title_font.render(f"Welcome to {app_name}", True, green)
        titlerect = title.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))
        screen.blit(title, titlerect)

        start_text = start_font.render("Press E to start", True, green)
        start_rect = start_text.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2 + 50))
        screen.blit(start_text,start_rect)
    else:
        if not outputting:
            input_text = input_font.render(user_prompt, True, green)
            input_rect = input_text.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))
            #input_box = pygame.Rect(input_rect.x, input_rect.y, input_rect.size[0], input_rect.size[1])
            #pygame.draw.rect(screen, green, input_box)
            screen.blit(input_text, input_rect)

            desc = start_font.render("What would you like to know today?", True, green)
            desc_rect = desc.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2 - 30))
            screen.blit(desc, desc_rect)
        elif outputting:
            if answer == "placeholder":
                try:
                    answer = pywhatkit.info(user_prompt, lines=info_reveal, return_value=True)
                except:
                    answer = "<Whoops! Failed to get response>"
            n = 100
            new_answer = "\n".join([answer[i:i+n] for i in range(0, len(answer), n)])
            userask = start_font.render(f"You asked : {user_prompt} \n\n{app_name} answered : {new_answer}", True, green)
            userask_rect = userask.get_rect()
            userask_rect.topleft = (20,20)
            screen_rect = screen.get_rect()

            if not screen_rect.contains(userask_rect):
                print("text is off screen!")
            
            screen.blit(userask, userask_rect)
            
    
            
                
        
    
    pygame.display.update()
