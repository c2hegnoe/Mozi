import random

nezoter = []

def nezoter_feltoltes():
    for i in range(15):

        for n in range(10):
            nezoter.append(random.randint(0, 3))

        nezoter.append(' | ')  

        for n in range(10):
            nezoter.append(random.randint(0, 3))

    print(nezoter)


def bevetel(a):

    osszeg = 0
    felnott_ar = 2500
    diak_nyugdijas_ar = 2100
    gyerek_ar = 1300
    szabad_hely_ar = 0

    for i in range(len(nezoter)):
        
        if a == 0:
            osszeg += felnott_ar
        if a == 1:
            osszeg += diak_nyugdijas_ar
        if a == 2:
            osszeg += gyerek_ar
        if a == 3:
            osszeg += szabad_hely_ar