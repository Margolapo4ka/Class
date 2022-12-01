def reduction(num, deno):
    number = 1

    for i in range(2, abs(deno)+1):
        if num % i == 0 and deno % i == 0:
            number = i
            break
    num = int(num / number)
    deno = int(deno / number)
    fraction = Fraction(num, deno)
    if deno % num == 0 and abs(num) != 1:
        fraction = reduction(num, deno)
    return fraction


class Fraction():

    def __init__(self, num , deno):
        self.num = num
        self.deno = deno




    def __str__(self):

        return str(self.num) + '/' + str(self.deno)


    def __add__(self, other):
       deno = self.deno * other.deno
       num = self.num * other.deno + other.num * self.deno
       return reduction(num, deno)



    def __sub__(self, other):
        deno = self.deno * other.deno
        num = self.num * other.deno - other.num * self.deno
        return reduction(num, deno)

    def __mul__(self, other):
        num = self.num * other.num
        deno = self.deno * other.deno
        return reduction(num, deno)

    def __truediv__(self, other):
        num = self.num * other.deno
        deno = self.deno * other.num
        return reduction(num, deno)
