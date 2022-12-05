# raise ValueError("Что-нибудь")
# try:
#     pass
#
# except ZeroDivisionError as error:
#     print("На ноль делить нельзя:(")
# # except ValueError:
# #     print("Программа принимает только целые числа")
# except Exception as  error:
#     print(f"Возникла неизвестная ошибка: {error}")

# import sys
# line = sys.stdin
# count = 0
# u = ""
# for i in line:
#     u = i
#     u = u.strip()
#     if len(u) > 0 and u[0] == "#":
#         continue
#     else:
#         print(i, en

class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.dims = square

class Agency(list):
    def __init__(self, name):
        self.name = name
        # super().__init__(name)

    def add_object(self, obj):
        super().append(obj)

    def remove_object(self, obj):
        super().remove(obj)

    def get_objects(self):

        return super().copy()
ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов