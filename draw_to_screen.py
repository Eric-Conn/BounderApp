#App to highlight on screen

# Example file showing a basic pygame "game loop"
from tkinter import *
import pygame
import os, random
from tkinter import ttk

# root = tk.Tk()
# button_win = tk.Frame(root, width = 500, height = 25)
# button_win.pack(side = tk.TOP)

# embed_pygame.pack(side = tk.TOP)


root = Tk()
root.title("Feet to Meters")

embed_pygame = Frame(root, width = 500, height = 500)

mainframe = ttk.Frame(root, padding="3 3 12 12")


# embeded_tk_window = tk.Frame(root, width = 720, height=720)



mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)


#Where we take in a variable
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

os.environ['SDL_WINDOWID'] = str(embed_pygame.winfo_id())

# os.environ['SDL_VIDEODRIVER']

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

#colors

BLACK = (0,0,0)
BLACK2 = None

pos_list = []
pressed_list = []

pos1_list = []
pos2_list = []

prev_pos = None

screen.fill("white")



surface = pygame.Surface((720,720), pygame.SRCALPHA)
surface2 = pygame.Surface((720,720))


# surface.fill('white')
surface2.fill('white')

while running:
    # poll for events
    pos = pygame.mouse.get_pos()
    pos_list.append(pos)
    pressed_list.append(pygame.mouse.get_pressed(3))


    pressed_keys = pygame.key.get_pressed()

    
    # pos1 = pygame.mouse.get_pos()
    # pos2 = pygame.mouse.get_pos()

    # pos1_list.append(pos1)
    # pos2_list.append(pos2)


    




    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        




    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("white")

    # RENDER YOUR GAME HERE
    # for i in range(len(pos_list)):
    #     if pressed_list[i][0] == True:
    #         pygame.draw.circle(screen,BLACK,pos_list[i],5)

    

        # if pressed_list[i][0] == True:
        #     pygame.draw.circle(screen,BLACK,pos_list[i],5)
    curr_pos =  pygame.mouse.get_pos()
    if (prev_pos is not None) and pygame.mouse.get_pressed(3)[0] == True:
        pygame.draw.line(surface2 , BLACK , prev_pos, curr_pos)

        if not BLACK2:
            BLACK2 = (0,0,0,50)


        pygame.draw.circle(surface , BLACK2 , curr_pos,40)

        # I = pygame.surfarray.pixels_alpha(surface)
        # print(I)
        # I[: ,:] =  (I > 0)

        # I = 0

        # surface.unlock()

        # screen.fill("white")

        
        screen.blit(surface2, (0,0))

        screen.blit(surface, (0,0))


    prev_pos = curr_pos

    

    
    # flip() the display to put your work on screen


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        screen.fill('white')
        surface.fill('white')
        surface2.fill('white')
  


    # if pressed_keys[pygame.KEYDOWN] == True:
    #     display.fill('white')

    pygame.display.flip()
    # print(screen)

    

    clock.tick(60)  # limits FPS to 60

pygame.quit()
# print(pressed_list)

