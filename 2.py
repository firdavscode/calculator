







import pygame
import sys
import time
  
  
# pygame.init() will initialize all
# imported module
pygame.init()

color1 = (255,255,255)
plus = pygame.image.load("plus.png")
minus = pygame.image.load("minus.png")
kopaytirish = pygame.image.load("ko'paytirish.png")
bolish = pygame.image.load("bo'lish.png") 

  
# it will display on screen
screen = pygame.display.set_mode([1000, 1000])
  
# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(1000, 1000, 1000, 32)
plus_rect = pygame.Rect(70,70,70,70)
minus_rect = pygame.Rect(70,70,70,70)
kop_rect = pygame.Rect(70,70,70,70)
bol_rect = pygame.Rect(70,70,70,70)
# box positions
input_rect.x = input_rect.x-760
input_rect.y = input_rect.y-760

plus_rect.y = 350
plus_rect.x = 110

minus_rect.y = 350
minus_rect.x = 210

kop_rect.y = 350
kop_rect.x = 310

bol_rect.y = 350
bol_rect.x = 410

  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False
  
while True:
    for event in pygame.event.get():
  
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
      
    # it will set background color of screen
    screen.fill((255, 255, 255))
  
    if active:
        color = color_active
    else:
        color = color_passive
          
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, (0,0,0), plus_rect)
    pygame.draw.rect(screen, (0,0,0), minus_rect)
    pygame.draw.rect(screen, (0,0,0), kop_rect)
    pygame.draw.rect(screen, (0,0,0), bol_rect)
  
    text_surface = base_font.render(user_text, True, (0, 0, 0))
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(plus, (110, 350))
    screen.blit(minus, (210, 350))
    screen.blit(kopaytirish, (310, 350))
    screen.blit(bolish, (410, 350))
    
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(1000, text_surface.get_width()+10)
    
      
    # display.flip() will update only a portion of the
    pygame.display.flip()
    son = user_text.split()
    if len(son)>2:
        if son[2]=='q':
            break
        else:
            continue
    else:
        continue
    















while True:
    text1 = str(chr(int(son[0])))
    text2 = str(chr(int(son[1])))
    

    for event in pygame.event.get():
        #+
        if event.type == pygame.MOUSEBUTTONDOWN:
            if plus_rect.collidepoint(pygame.mouse.get_pos()): 
                text11 = base_font.render('='+str(ord(text1)+ord(text2)), True, (0, 0, 0))
                screen.blit(text11,(input_rect.x+(text_surface.get_width()+10), input_rect.y+5))  
                pygame.display.flip()
                

        #-
        if event.type == pygame.MOUSEBUTTONDOWN:
            if minus_rect.collidepoint(pygame.mouse.get_pos()): 
                text11 = base_font.render('='+str(ord(text1)-ord(text2)), True, (0, 0, 0))
                screen.blit(text11,(input_rect.x+(text_surface.get_width()+10), input_rect.y+5))  
                pygame.display.flip()
                


        #*
        if event.type == pygame.MOUSEBUTTONDOWN:
            if kop_rect.collidepoint(pygame.mouse.get_pos()): 
                text11 = base_font.render('='+str(ord(text1)*ord(text2)), True, (0, 0, 0))
                screen.blit(text11,(input_rect.x+(text_surface.get_width()+10), input_rect.y+5))  
                pygame.display.flip()
                



        #/
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bol_rect.collidepoint(pygame.mouse.get_pos()): 
                text11 = base_font.render('='+str(ord(text1)/ord(text2)), True, (0, 0, 0))
                screen.blit(text11,(input_rect.x+(text_surface.get_width()+10), input_rect.y+5))  
                pygame.display.flip()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

          
        
              
                  

      
    
