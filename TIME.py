#Text Interplacer Movement Engine (TIME) V0.17
#By John Stubblefield

#perhaps these two game settings will be two seperate scripts, and the games use functions from here. (time.sideon(foo,foo,foo))

#imports (put these before each module script)
import random, keyboard, time
from platform import system as system_name 
from os import system as system_call
import efm, sgf

#parameters for game
#0 = side-on, 1 = top-down
gametype = 0

#I think lines beyond this point should be exported as a library for side-on games. later i can repurpose this for top-down 4-way moving games.

plats = []
space1 = "                              "
space2 = "                              "
posx = 3
posy = 5
player = "p"

sgf.rand_plats(3,plats,30,3)

#game loop
while gametype == 0:
    #variable refresh
    stand = posx-1
    space1 = "                              "
    space2 = "                              "

    #clears previous frame
    efm.refresh()

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
        if posx >= 28:
            time.sleep(0.015)
        else:
            posx = posx + 1
            time.sleep(0.015)

    #gapping
    elif keyboard.is_pressed("Ctrl"):
        if player == "p":
            if posy == 5:
                if plats[0][posx+1] != "_":
                    if plats[0][posx+2] == "_":
                        posx = posx + 2
            if posy == 3:
                if plats[1][posx+1] != "_":
                    if plats[1][posx+2] == "_":
                        posx = posx + 2
            if posy == 1:
                if plats[2][posx+1] != "_":
                    if plats[2][posx+2] == "_":
                        posx = posx + 2
        if player == "q":
            if posy == 5:
                if plats[0][posx-1] != "_":
                    if plats[0][posx-2] == "_":
                        posx = posx - 2
            if posy == 3:
                if plats[1][posx-1] != "_":
                    if plats[1][posx-2] == "_":
                        posx = posx - 2
            if posy == 1:
                if plats[2][posx-1] != "_":
                    if plats[2][posx-2] == "_":
                        posx = posx - 2
                
    #falling physics
    if posy == 5:
        if plats[0][posx] != "_":
            posy = posy-1
    if posy == 4:
        time.sleep(0.025)
        posy = posy-1 
    if posy == 3:
        if plats[1][posx] != "_":
            posy = posy-1
    if posy == 2:
        time.sleep(0.025)
        posy = posy-1 
    
    #height draw routines
    if posy == 5:
        efm.insert_str(plats[0], player, posx)
        print(space1)
        print(plats[1])
        print(space2)
        print(plats[2])
    if posy == 4:
        print(plats[0])
        efm.insert_str(space1, player, posx)
        print(plats[1])
        print(space2)
        print(plats[2])
    if posy == 3:
        print(plats[0])
        print(space1)
        efm.insert_str(plats[1],player, posx)
        print(space2)
        print(plats[2])
    if posy == 2:
        print(plats[0])
        print(space1)
        print(plats[1])
        efm.insert_str(space2, player, posx)
        print(plats[2])
    if posy == 1:
        print(plats[0])
        print(space1)
        print(plats[1])
        print(space2)
        efm.insert_str(plats[2],player, posx)

    #ending sleep (reduce gameplay speed, make this a variable with frontend)
    time.sleep(0.025)

#end side-on code here


#start top-down code here

#default variables (these will be referenced to by script when frontend is added)
posx = 3
posy = 5
posxmin = 0
posxmax = 14
posymin = 1
posymax = 8
player = "O"
row8 = "+++++++++++++++"
row7 = "+             +"
row6 = "+             +"
row5 = "+             +"
row4 = "+             +"
row3 = "+             +"
row2 = "+             +"
row1 = "+++++++++++++++"

#gameloop (frontend will allow for modification of this loop)
while gametype == 1:

    efm.refresh()

    #input (make inputs variables in the frontend.)
    if keyboard.is_pressed("up"):
        if posy < posymax:
            posy = posy + 1
        time.sleep(0.015)
    if keyboard.is_pressed("down"):
        if posy > posymin:
            posy = posy - 1
        time.sleep(0.015)
    if keyboard.is_pressed("left"):
        if posx > posxmin:
            posx = posx - 1
        time.sleep(0.015)
    if keyboard.is_pressed("right"):
        if posx < posxmax:
            posx = posx + 1
        time.sleep(0.015)

    #drawing (add more if statements for more rows of text. you will also need to add more row variables.)
    if posy == 1:
        print(row8)
        print(row7)
        print(row6)
        print(row5)
        print(row4)
        print(row3)
        print(row2)
        efm.insert_str(row1, player, posx)
    if posy == 2:
        print(row8)
        print(row7)
        print(row6)
        print(row5)
        print(row4)
        print(row3)
        efm.insert_str(row2, player, posx)
        print(row1)
    if posy == 3:
        print(row8)
        print(row7)
        print(row6)
        print(row5)
        print(row4)
        efm.insert_str(row3, player, posx)
        print(row2)
        print(row1)
    if posy == 4:
        print(row8)
        print(row7)
        print(row6)
        print(row5)
        efm.insert_str(row4, player, posx)
        print(row3)
        print(row2)
        print(row1)
    if posy == 5:
        print(row8)
        print(row7)
        print(row6)
        efm.insert_str(row5, player, posx)
        print(row4)
        print(row3)
        print(row2)
        print(row1)
    if posy == 6:
        print(row8)
        print(row7)
        efm.insert_str(row6, player, posx)
        print(row5)
        print(row4)
        print(row3)
        print(row2)
        print(row1)
    if posy == 7:
        print(row8)
        efm.insert_str(row7, player, posx)
        print(row6)
        print(row5)
        print(row4)
        print(row3)
        print(row2)
        print(row1)
    if posy == 8:
        efm.insert_str(row8, player, posx)
        print(row7)
        print(row6)
        print(row5)
        print(row4)
        print(row3)
        print(row2)
        print(row1)

    #ending sleep (frontend variable as well)
    time.sleep(0.025)
        

        
    
    










    
