import time
from datetime import datetime


def heure_actuelle():  
    while True:  
        heure = str(datetime.now().time())
        heure = heure[:-7]
        print(heure)
        time.sleep(1)


def afficher_heure():  
    heure_modifier = (16, 30, 0)  
    heure = heure_modifier[0]  
    minute = heure_modifier[1]
    secondes = heure_modifier[2]
    while True:  
        secondes = secondes + 1
        if secondes == 60:
            secondes = 0
            minute = minute + 1
        if minute == 60:
            minute = 0
            heure = heure + 1
        if heure == 24:
            heure = 0

        heure = str(heure)  
        minute = str(minute)
        secondes = str(secondes)
        if len(secondes) < 2:
            secondes = list(secondes)
            secondes.insert(0, "0")
            secondes = "".join(secondes)
        if len(minute) < 2:
            minutes = list(minute)
            minutes.insert(0, "0")
            minutes = "".join(minute)
        if len(heure) < 2:
            heure = list(heure)
            heure.insert(0, "0")
            heure = "".join(heure)

        
        print(heure+":"+minute+":"+secondes)
        heure = int(heure)
        minute = int(minute)
        secondes = int(secondes)
        time.sleep(1)  


def alarme():  
    while True:  
        heure = str(datetime.now().time())
        heure = heure[:-7]
        reveil = "08:48:00"  
        if reveil == heure:
            print("Reveil toi frérot")
            break
        else:
            time.sleep(1)


heure_actuelle()
afficher_heure()
alarme()