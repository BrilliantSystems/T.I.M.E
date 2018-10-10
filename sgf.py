#Text Interplacer Movement Engine (TIME) V0.15
#side-on gameplay functions (SGF)
#By John Stubblefield

import random, keyboard, time
from platform import system as system_name 
from os import system as system_call
import efm

#random platform generator function (plat_output requires a list, and will make plat_amount platforms, and plat ratio is input:gap.)
def rand_plats(plat_amount, plat_output, plat_length, plat_ratio):
    global platoutput
    plat_index = 0
    for i in range(plat_amount):
        for i in range(plat_length-1):
                r = random.randint(0,plat_ratio)
                if r == 0:
                    plat_output[plat_index] = plat_output[plat_index] + " "
                if r != 0:
                    plat_output[plat_index] = plat_output[plat_index] + "_"
        plat_index += 1


plats = ["","","","",""]
rand_plats(5,plats,30,3)
print(plats)
            
        
    
 
