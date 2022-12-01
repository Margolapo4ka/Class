class Person:
    def __init__(self, name, surname, age, nationality, sex):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__nationality = nationality
        self.__sex = sex
    def __str__(self):
        return f"{self.__name} {self.__surname} {self.__age} {self.__nationality} {self.__sex}"
class Mother(Person):
    def __init__(self, name, surname, age, nationality, sex):
        super().__init__(name, surname, age, nationality, sex)

    def cooking(self, name):
        print(f"{name} приготовила кушать")
class Father(Person):
    def __init__(self, name, surname, age, nationality, sex):
        super().__init__(name, surname, age, nationality, sex)
    def cooking(self, name):
        print(f"{name} приготовила кушать, я все съел")
    def work(self):
        print(f"{self.__name} пошел на работу")

class Child(Mother, Father):
    def __init__(self, name, surname, age, nationality, sex):
        super().__init__(name, surname, age, nationality, sex)

    def cooking(self, name):
        print(f"{name} приготовила еду, я иду кушать")

    def work(self):
        super().work()