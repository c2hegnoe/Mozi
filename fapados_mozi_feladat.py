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

print("Hello")