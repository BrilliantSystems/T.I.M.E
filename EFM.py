#Text Interplacer Movement Engine (TIME) V0.1
#Engine Functions Module (EFM)
#By John Stubblefield

#imports (put these before each module script)
import random, keyboard, time
from platform import system as system_name 
from os import system as system_call

#screen refresh
def refresh():
    command = "cls" if system_name().lower()=="windows" else "clear"
    system_call(command)

#character replacer
def insert_str(string, str_to_insert, index):
    print(string[:index] + str_to_insert + string[index+1:])
