import time

class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")

truck1 = Truck("Volvo", 5, "FH16", 40000, color="Blue", weight=12000)
truck2 = Truck("Scania", 3, "R450", 45000, color="White", weight=12500)

car1 = Car("BMW", 2, "320i", 250, color="Black", weight=1400)
car2 = Car("Audi", 1, "A4", 240, color="Silver", weight=1450)

print(f"Truck 1: Brand = {truck1.brand}, Age = {truck1.age}, Max Load = {truck1.max_load}")
truck1.move()
truck1.load()

print(f"Truck 2: Brand = {truck2.brand}, Age = {truck2.age}, Max Load = {truck2.max_load}")
truck2.move()

print(f"Car 1: Brand = {car1.brand}, Age = {car1.age}, Max Speed = {car1.max_speed}")
car1.move()

print(f"Car 2: Brand = {car2.brand}, Age = {car2.age}, Max Speed = {car2.max_speed}")
car2.move()
