# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:19:37 2021

@author: Lenovo
"""


##user is player1
n_sticks = int(input("How many sticks (N) in the pile:"))
print("There are",n_sticks,"sticks in the pile.")
if n_sticks > 0:
    print("Great! Let's play.")
    player1 = input("WHAT IS YOUR NAME:") 
    t_sticks = int(input("How max sticks you can take in pile:"))

while n_sticks > 0: 
    if n_sticks == 1: 
        print(f"{player1}, take the last sticks. \nI, smart computor win!!!")
        break
    ###player 1 is myself
    player1_take = int(input(f"{player1},how many sticks you will take:"))
    a = t_sticks 
    b = t_sticks - t_sticks
    if player1_take <= b or player1_take > a: 
       print (f"you can select only 1 or {a} !!!")
    else: 
        n_sticks = n_sticks - player1_take 
        if n_sticks > 1: 
           print("There are",n_sticks,"sticks in the pile.") 
        else: 
           print("There is",n_sticks,"stick in the pile.")
        
    ###player 2 is computer
        if n_sticks == 1:
           print(f"I, smart computor, take the last sticks. \n{player1} win (I,smart computor, am sad T_T)")
           break
        
        if n_sticks%(t_sticks + 1) == 0:
            com = t_sticks 
            if n_sticks%3 == 0:
                com = 2
        elif n_sticks%(t_sticks + 1) == 1:
            com = t_sticks - 1
        elif n_sticks%(t_sticks + 1) == 2:
            if n_sticks == 2:
                com = 1
            else:
                com = t_sticks - 2
        elif n_sticks%3 == 0:
            com = 2
        elif n_sticks%(t_sticks - 1) == 1:
            com = t_sticks - 1
        elif n_sticks%(t_sticks - 1) == 2:
            if n_sticks == 2:
                com =1
            else:
                com = t_sticks - 2
        else:
            com = t_sticks - 2
        
        ###output of computor
        n_sticks = n_sticks - com 
        print(f"I, smart computor, take : {com}")
        if n_sticks > 1: 
           print("There are",n_sticks,"sticks in the pile.") 
        else: 
           print("There is",n_sticks,"stick in the pile.")
else:
    print("You can take number more 0")
       
        
        