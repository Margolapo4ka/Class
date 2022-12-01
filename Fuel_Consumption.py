
class fuel_consumption:

    def __init__(self, mark, model, liters, kilometers):
        self.mark = mark
        self.model = model
        self.liters = liters
        self.kilometers = kilometers


    def __str__(self):
        return self.mark + " " + self.model + " " + str(self.liters) + ' ' + str(self.kilometers)

    def fuel_con(self):
        kilometer = self.liters / self.kilometers * 100
        print(f'{self.mark} {self.model} расходует {round(kilometer, 2)} литров на 100 километров')