class Person:
    def __init__(self, name, surname, age, number, id):
        self._name = name
        self._surname = surname
        self._age = age
        self._number = number
        self._id = id

    def __str__(self):
        return self._name + " " + self._surname + " " + str(self._age) + " " + self._number + " " + str(self._id)


    def _check_2(self):
        print("Фигня")
class Employee(Person):


    def __init__(self, name, surname, age, number, id, post):
        super().__init__(name, surname, age, number, id)
        self.__post = post

    def __str__(self):
        return super().__str__() + " " + self.__post

    @staticmethod  #статическкие методы, делает обычную функцию внутри класса
    def hello():
        pass


    def check(self):
        print(self._number)


class Client(Person):
    def __init__(self, name, surname, age, number, id, money):
        super().__init__(name, surname, age, number, id)
        self.__money = money

    def __str__(self):
        return super().__str__() + " " + str(self.__money)


    def search(self):
        print("Ищу товар")

    def buy(self):
        print("Покупаю!")

class Product():
    def __init__(self, mark, model, price):
        self.mark = mark
        self.model = model
        self.price = price

    def __str__(self):
        return self.mark + ' ' + self.model + ' ' + str(self.price)

class Purchase():
    def __init__(self, employee, client, product, time):
        self.employee = employee
        self.client = client
        self.product = product
        self.time = time
    def __str__(self):
        return "Employee: " + str(self.employee) + "\nClient: " + str(self.client) + "\nProduct: " + str(self.product) + '\nTime: ' + str(self.time)

class Report:
    @staticmethod
    def get_report(purchases):
        purchase = ""
        summa = 0
        for i in purchases:
            purchase += str(i)
            purchase += "\n"
            summa += i.product.price

        return purchase + "\n" + f"Сумма всех товаров: {summa}"
