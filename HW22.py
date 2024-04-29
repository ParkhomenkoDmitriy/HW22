import time


def load():
    time.sleep(1)
    print("load")
    time.sleep(1)


def stop():
    print("stop")
    time.sleep(1)


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def perform_actions(self):
        self.move()
        load()
        self.show_info()
        stop()

    def move(self):
        print("move")

    def show_info(self):
        print(f"Brand = {self.brand}, Age = {self.age}, Mark = {self.mark}, Color = {self.color}, "
              f"Weight = {self.weight}")


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def show_info(self):
        print(f"Truck: Brand = {self.brand}, Age = {self.age}, Max Load = {self.max_load}, Color = {self.color}, "
              f"Weight = {self.weight}")


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")

    def show_info(self):
        print(f"Car: Brand = {self.brand}, Age = {self.age}, Mark = {self.mark}, Max Speed = {self.max_speed},"
              f" Color = {self.color}, Weight = {self.weight}")


truck1 = Truck("Volvo", 5, "FH16", 40000, color="Blue", weight=12000)
truck2 = Truck("Scania", 3, "R450", 45000, color="White", weight=12500)

car1 = Car("BMW", 2, "320i", 250, color="Black", weight=1400)
car2 = Car("Audi", 1, "A4", 240, color="Silver", weight=1450)

truck1.perform_actions()
truck2.perform_actions()

car1.perform_actions()
car2.perform_actions()
