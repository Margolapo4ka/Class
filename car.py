class Car():

    def __init__(self, mark, model, color, distance=0, liters=0):
        self.mark = mark
        self.model = model
        self.color = color
        self.distance = distance
        self.liters = liters

    def __str__(self):
        return  self.mark + " " + self.model + " " + self.color + ' ' + str(self.distance)

    def go(self, speed):
        print(f"{self.mark} едет {speed} км/ч" )

    def left(self):
        print(f'{self.mark} повернула налево')

    def right(self):
        print(f'{self.mark} повернула направо')


    def __add__(self, other):
        dist = self.distance + other.distance
        return Car(self.mark, self.model, self.color, dist)

    def fuel_con(self):
        kilometer = self.liters / self.distance * 100
        print(f'{self.mark} {self.model} расходует {round(kilometer, 2)} литров на 100 километров')