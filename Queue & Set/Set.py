import os


class Toy:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name
  

class Kindergarten:
    toys = set()

    def __init__(self):
        pass

    def add_toy(self, toy):
        self.toys.add(toy)

    def contains_toy(self, toy) -> bool:
        return toy in self.toys


if __name__ == "__main__":
    toys = {Toy("car"), Toy("fluffy cat"), Toy("fluffy dog"), Toy("doll"), Toy("taddy bear")}

    n = int(input())
    os.system('clear')
    kindergartens = []
    for i in range(n):
        print("enter count of toys: ", end='')
        k = int(input())
        os.system('clear')

        kindergarten = Kindergarten()
        print("Enter toy names:")
        for _ in range(k):
            kindergarten.add_toy(Toy(input().rstrip()))
        kindergartens.append(kindergarten)
        os.system('clear')
    
    toys_that_no_kindergarten_has = toys
    for kindergarten in kindergartens:
        toys_that_no_kindergarten_has = toys_that_no_kindergarten_has.difference(kindergarten.toys)
    
    print("Toys that no kindergarten has: ")
    for _ in toys_that_no_kindergarten_has:
        print(_.name)
    print()
    
    toys_that_every_kindergarten_has = toys
    for kindergarten in kindergartens:
        toys_that_every_kindergarten_has = toys_that_every_kindergarten_has.intersection(kindergarten.toys)

    print("Toys that every kindergarten has: ")
    for _ in toys_that_every_kindergarten_has:
        print(_.name)

