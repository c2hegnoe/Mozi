import random

print("Írja be kérem, hogy hány jegyet szeretni vásárolni: ")
a = int(input())

while a < 2 or a > 5:
    print("Legyen szíves írja be újra hány jegyet szeretne (2 és 5 között): ")
    a = int(input())

Nezoter_lista = []

def nezoter_feltoltes():
    for i in range(15):
        sor = []

        for n in range(10):
            sor.append(random.randint(0, 3))

        sor.append(' | ')  

        for n in range(10):
            sor.append(random.randint(0, 3))

        print(sor)

        Nezoter_lista.append(sor)


def bevetel(a):

    osszeg = 0
    felnott_ar = 2500
    diak_nyugdijas_ar = 2100
    gyerek_ar = 1300
    szabad_hely_ar = 0

    for i in range(len(Nezoter_lista)):
        for a in range(len(Nezoter_lista[i])):

            if Nezoter_lista[i][a] == 0:
                osszeg += felnott_ar

            if Nezoter_lista[i][a] == 1:
                osszeg += diak_nyugdijas_ar

            if Nezoter_lista[i][a] == 2:
                osszeg += gyerek_ar

            if Nezoter_lista[i][a] == 3:
                osszeg += szabad_hely_ar


    print("Összes bevétel összege: ",osszeg, "Ft")


def egymasMellett(a):
    sor = 0
    if a == 2:
        for i in range(len(Nezoter_lista)):
            for j in range(len(Nezoter_lista[i])):
                if Nezoter_lista[i][j] == 0 and Nezoter_lista[i][j-1] == 0:
                    sor = i+1
                    print("A(z)", sor, ". sorban van 2 hely egymás mellett.")
                    return
                
    if a == 3:
        for i in range(len(Nezoter_lista)):
            for j in range(len(Nezoter_lista[i])):
                if Nezoter_lista[i][j] == 0 and Nezoter_lista[i][j-1] == 0 and Nezoter_lista[i][j-2] == 0:
                    sor = i+1
                    print("A(z)", sor, ". sorban van 3 hely egymás mellett.")
                    return

    if a == 4:
        for i in range(len(Nezoter_lista)):
            for j in range(len(Nezoter_lista[i])):
                if Nezoter_lista[i][j] == 0 and Nezoter_lista[i][j-1] == 0 and Nezoter_lista[i][j-2] == 0 and Nezoter_lista[i][j-3] == 0:
                    sor = i+1
                    print("A(z)", sor, ". sorban van 4 hely egymás mellett.")
                    return
                
    if a == 5:
        for i in range(len(Nezoter_lista)):
            for j in range(len(Nezoter_lista[i])):
                if Nezoter_lista[i][j] == 0 and Nezoter_lista[i][j-1] == 0 and Nezoter_lista[i][j-2] == 0 and Nezoter_lista[i][j-3] == 0 and Nezoter_lista[i][j-4] == 0:
                    sor = i+1
                    print("A(z)", sor, ". sorban van 5 hely egymás mellett.")
                    return
                
    if sor == 0:
        print("Nincs")
        return
                

def kihasznaltsag(nezoter):
    foglalt_ulohelyek = 300

    for i in range(len(nezoter)):
        for a in range(len(nezoter[i])):
            if nezoter [i][a] == 0:
                foglalt_ulohelyek -= 1
    print("A terem kihasználtsága" ,round(foglalt_ulohelyek/300*100, 2), "%.")



def felnott_jegyek(nezoter):
    felnott_jegyek_szama = 0

    for i in nezoter:
        for a in i:
            if a == 3:
                felnott_jegyek_szama += 1
    print(felnott_jegyek_szama, "db teljes áru jegyet vásároltak.")


nezoter_feltoltes()
egymasMellett(a)
kihasznaltsag(Nezoter_lista)
felnott_jegyek(Nezoter_lista)
bevetel(Nezoter_lista)

