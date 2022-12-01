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
#         print(i, end="")
import datetime
import random
with open('test.txt', "r") as input:
    with open('output.txt', "w") as output:

        for num, text in enumerate(input.readlines()):

            print(f"{num+1}) {text}",  end="")