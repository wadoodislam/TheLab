import random
import time


class Animal:

    def generatenumber(self):
        num = random.randint(1, 10)
        return num

    def move(self):
        return self.generatenumber()


class TortoiseClass(Animal):
    def move(self,tortoise):
        tnum = super().move()
        if tnum in range(1, 6):
            tortoise = int(tortoise + 3)
        elif tnum in range(6, 8):
            tortoise = tortoise - 6
        elif tnum in range(8, 11):
            tortoise = tortoise + 1
        if tortoise < 1:
            tortoise = 1
        return tortoise


class HareClass(Animal):
    def move(self,hare):
        hnum = super().move()
        if hnum in range(1, 3):
            hare = hare + 0
        elif hnum in range(3, 5):
            hare = hare + 9
        elif hnum == 5:
            hare = hare - 12
        elif hnum in range(6, 9):
            hare = hare + 1
        elif hnum in range(9, 11):
            hare = hare - 2
        if hare < 1:
            hare = 1
        return hare

tortoiseMove = TortoiseClass()
HareMove = HareClass()
tonum = 1
hanum = 1
count = 0
while tonum < 70 and hanum < 70:
    time.sleep(1)
    count = count + 1
    print("iterations ", count)
    tortoiseMove = TortoiseClass()
    HareMove = HareClass()
    tonum = tortoiseMove.move(tonum)
    hanum = HareMove.move(hanum)
    t1 = tonum
    while t1 >= 0:
        print("T", end="")
        t1 = t1 - 1
    print("\b")
    h1 = hanum
    while h1 >= 0:
        print("H", end="")
        h1 = h1 - 1
    print("\b")

if tonum > hanum:
    print("\nTortoise Winss..")
elif hanum > tonum:
    print("\nHare Winss..")
else:
    print("Its a Tie")
