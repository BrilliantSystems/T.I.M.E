#Text Interplacer Movement Engine (TIME) V0.02
#By John Stubblefield

#imports
import random, keyboard, time
from platform import system as system_name 
from os import system as system_call       

#system functions
#screen clear (do not modify idiot)
def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if system_name().lower()=="windows" else "clear"

    # Action
    system_call(command)

#character replacer
def insert_str(string, str_to_insert, index):
    print(string[:index] + str_to_insert + string[index+1:])

#random platforms
plat1 = ""
plat2 = ""
plat3 = ""
d = 0
for i in range(29):
    d = random.randint(0,3)
    if d == 0:
        plat1 = plat1 + " "
    if d != 0:
        plat1 = plat1 + "_"
plat1 = plat1 + " "
plat1base = plat1

for i in range(29):
    d = random.randint(0,3)
    if d == 0:
        plat2 = plat2 + " "
    if d != 0:
        plat2 = plat2 + "_"
plat2 = plat2 + " "
plat2base = plat2
    
for i in range(29):
    d = random.randint(0,3)
    if d == 0:
        plat3 = plat3 + " "
    if d != 0:
        plat3 = plat3 + "_"
plat3 = plat3 + " "
plat3base = plat3


clear_screen()


#initial variable declaration
plat1 = plat1base
plat2 = plat2base
plat3 = plat3base
space1 = "                              "
space2 = "                              "
posx = 3
posy = 5
player = "p"


#game loop
while True:
    #variable refresh
    stand = posx-1
    plat1 = plat1base
    plat2 = plat2base
    plat3 = plat3base
    space1 = "                              "
    space2 = "                              "


    
    #clears previous frame
    clear_screen()

    #input
    if keyboard.is_pressed('left'):
        player = "q"
        if posx <= 0:
            time.sleep(0.15)
        else:
            posx = posx - 1
            time.sleep(0.015)
            
    elif keyboard.is_pressed("right"):
        player = "p"
        if posx >= 30:
            time.sleep(0.015)
        else:
            posx = posx + 1
            time.sleep(0.015)

    #gapping
    elif keyboard.is_pressed("Ctrl"):
        if player == "p" and posx < 26 and posx > 2:
            if posy == 5:
                if plat1base[posx+1] != "_":
                    if plat1base[posx+2] == "_":
                        posx = posx + 2
            if posy == 3:
                if plat2base[posx+1] != "_":
                    if plat2base[posx+2] == "_":
                        posx = posx + 2
            if posy == 1:
                if plat3base[posx+1] != "_":
                    if plat3base[posx+2] == "_":
                        posx = posx + 2
        if player == "q":
            if posy == 5:
                if plat1base[posx-1] != "_":
                    if plat1base[posx-2] == "_":
                        posx = posx - 2
            if posy == 3:
                if plat2base[posx-1] != "_":
                    if plat2base[posx-2] == "_":
                        posx = posx - 2
            if posy == 1:
                if plat3base[posx-1] != "_":
                    if plat3base[posx-2] == "_":
                        posx = posx - 2
                
                        
                

    #falling physics
    if posy == 5:
        if plat1base[posx] != "_":
            posy = posy-1
    if posy == 4:
        time.sleep(0.025)
        posy = posy-1 
    if posy == 3:
        if plat2base[posx] != "_":
            posy = posy-1
    if posy == 2:
        time.sleep(0.025)
        posy = posy-1 
    
    #height draw routines
    if posy == 5:
        insert_str(plat1, player, posx)
        print(space1)
        print(plat2+"_")
        print(space2)
        print(plat3+"_")
    if posy == 4:
        print(plat2+"_")
        insert_str(space1, player, posx)
        print(plat2+"_")
        print(space2)
        print(plat3+"_")
    if posy == 3:
        print(plat1+"_")
        print(space1)
        insert_str(plat2,player, posx)
        print(space2)
        print(plat3+"_")
    if posy == 2:
        print(plat2+"_")
        print(space1)
        print(plat2+"_")
        insert_str(space2, player, posx)
        print(plat3+"_")
    if posy == 1:
        print(plat1+"_")
        print(space1)
        print(plat2+"_")
        print(space2)
        insert_str(plat3,player, posx)

    #ending sleep (reduce gameplay speed)
    time.sleep(0.025)

        
    
    










    
