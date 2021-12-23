#  DATE : 24/06/2021 


import random

a=["snake","water","gun"]

print("choose from snake , water ,gun and enter your choice")

def winner(a1,a2):
    if a1==a2:
        return 0
    if a1=="snake" and a2=="water":
        return 1
    elif a2=="snake" and a1=="water":
        return -1
    if a1=="water" and a2=="gun":
        return -1
    elif a2=="water" and a1=="gun":
        return 1
    if a1=="gun" and a2=="snake":
        return -1
    elif a2=="gun" and a1=="snake":
        return 1

#print(winner(a1,a2),a1,a2)
i=0
t=0
t1=0
while i<10:
    a1=random.choice(a)
    a2=(input())
    b=winner(a1,a2)
    if b==0:
        print(f"game draw comp:{a1} you:{a2}")
    elif b==1:
        print(f"you won comp:{a1} you:{a2}")
        t=t+1
    else :
        print(f"you lose comp:{a1} you:{a2}") 
        t1=t1+1
    i=i+1 
if t>t1:
    print("YOU WON")
else:
    print("COMP WON ")
