from People.person import *
import datetime
from People.child import *

# num1 = Fraction(1, 15)
# num2 = Fraction(2, 5)
# car = Car("BMW", 'X6','black', 6163.787 , 716.346 )
# num = "2 + 3"
# car.fuel_con()
# num3 = num1 + num2
# num4 = num1 - num2
# num5 = num1 * num2
# num6 = num1 / num2
# print(num3)
# print(num4)
# print(num5)
# print(num6)
# employee = Employee("Макс", "Котькин", 26, "38298950", 666, "Менеджер")
# client = Client("Марго", "Шварц", 20, "432525", 999, 100000)
# product = Product("Samsung", "D100", 100000)
# purchase = [Purchase(client, employee, product, datetime.datetime.today())]
# Employee.hello()
# print(Report.get_report(purchase))
# mother = Mother("Мария", "Новикова", 43, "Русская", "Женский")
# father = Father("Nick", "Dark", 45, "American", "Male")
# child = Child("Иван", "Dark", 16, "American", "Male")
# mothers = str(mother).split()
# print(mother)
# print(father)
# family = [mother, father, child]
# for person in family:
#     person.cooking(mothers[0])

import datetime
data1 = "2012-10-12"
data2 = "2012-10-12"
day = str(datetime.date.fromisoformat(data1) - datetime.date.fromisoformat(data2)).split()
print(day[0])