import random
import time


class Animal:
    position = 1

    def generatenumber(self):
        num = random.randint(1, 10)
        return num

    def move(self):
        raise NotImplementedError()

    def prints(self):
        raise NotImplementedError()

    def has_won(self):
        if self.position >= 70:
            return True
        return False


class TortoiseClass(Animal):

    def move(self):
        tnum = super().generatenumber()
        if tnum in range(1, 6):
            self.position += 3
        elif tnum in range(6, 8):
            self.position -= 6
        elif tnum in range(8, 11):
            self.position += 1
        if self.position < 1:
            self.position = 1
        return self.position

    def prints(self):
        print("T" * self.position)


class HareClass(Animal):
    def move(self):
        hnum = super().generatenumber()
        if hnum in range(1, 3):
            self.position += 0
        elif hnum in range(3, 5):
            self.position += 9
        elif hnum == 5:
            self.position -= 12
        elif hnum in range(6, 9):
            self.position += 1
        elif hnum in range(9, 11):
            self.position -= 2
        if self.position < 1:
            self.position = 1
        return self.position

    def prints(self):
        print("H" * self.position)


class Simulation(TortoiseClass, HareClass):
    tortoiseMove = TortoiseClass()
    HareMove = HareClass()
    count = 0
    while not (tortoiseMove.has_won() or HareMove.has_won()):
        time.sleep(1)
        count = count + 1
        print("iterations ", count)
        tortoiseMove.move()
        HareMove.move()
        tortoiseMove.prints()
        HareMove.prints()

    if tortoiseMove.has_won():
        print("\nTortoise Winss..")
    elif HareMove.has_won() and tortoiseMove.has_won():
        print("Its a Tie")
    else:
        print("\nHare Winss..")


Simulation()