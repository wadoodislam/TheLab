import random
import time
from os import system


class Animal:
    position = 1

    def __init__(self, name):
        self.name = name

    def generatenumber(self):
        return random.randint(1, 10)

    def move(self):
        raise NotImplementedError()

    def display(self):
        print(self.name * self.position)

    def has_won(self):
        if self.position >= 70:
            return True
        return False


class Tortoise(Animal):

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


class Hare(Animal):
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


class Simulation:
    tortoise = Tortoise("T")
    hare = Hare("H")

    def run(self):
        while not (self.tortoise.has_won() or self.hare.has_won()):
            system("clear")
            time.sleep(1)
            self.tortoise.move()
            self.hare.move()
            self.tortoise.display()
            self.hare.display()

        if self.hare.has_won() and self.tortoise.has_won():
            print("Its a Tie")
        elif self.tortoise.has_won():
            print("\nTortoise Winss..")
        elif self.hare.has_won():
            print("\nHare Winss..")


if __name__ == '__main__':
    Simulation().run()

