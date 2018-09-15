# WAP to create scitific calculator?


import math


class Calculate():
    def __init__(self, num_1, operator, num_2):
        self.num_1 = num_1
        self.operator = operator
        self.num_2 = num_2

    def simple_clac(self):

        if self.operator == '+':
            add = self.num_1 + self.num_2
            return add

        elif self.operator == '-':
            sub = self.num_1 - self.num_2
            return sub

        elif self.operator == '*':
            mul = self.num_1 * self.num_2
            return mul

        elif self.operator == '/':
            div = self.num_1 / self.num_2
            return div

        elif self.operator == '%':
            percent = (self.num_1 * self.num_2) / 100
            return percent

        else:
            print('This is not an Operator sign.')


class Sci():
    def __init__(self, num_3, oper):
        self.num_3 = num_3
        self.oper = oper

    def sci_calc(self):

        if self.oper == 'sqrt':
            sqrt = math.sqrt(self.num_3)
            return sqrt

        elif self.oper == 'sq':
            sq = self.num_3 ** 2
            return sq

        elif self.oper == 'cube':
            cube = self.num_3 ** 3
            return cube

        elif self.oper == 'power':
            enter = int(input("Enter the power: "))
            power = self.num_3 ** enter
            return power

        elif self.oper == 'log':
            # base = int(input("Enter the base value: "))
            log = math.log10(self.num_3)
            return log

        elif self.oper == 'sin':
            deg_rad = raw_input("Enter Deg or rad: ")
            if deg_rad.lower() == 'rad':
                sin = math.sin(self.num_3)
                return sin

            elif deg_rad.lower() == 'deg':
                degree = math.radians(self.num_3)
                # print(degree)
                sin = math.sin(degree)
                return sin

        elif self.oper == 'cos':
            deg_rad = raw_input("Enter Deg or rad: ")
            if deg_rad.lower() == 'rad':
                cos = math.cos(self.num_3)
                return cos

            elif deg_rad.lower() == 'deg':
                degree = math.radians(self.num_3)
                # print(degree)
                cos = math.cos(degree)
                return cos

        elif self.oper == 'tan':
            deg_rad = raw_input("Enter Deg or rad: ")
            if deg_rad.lower() == 'rad':
                tan = math.tan(self.num_3)
                return tan

            elif deg_rad.lower() == 'deg':
                degree = math.radians(self.num_3)
                # print(degree)
                tan = math.tan(degree)
                return tan

        elif self.oper == 'sinh':
            deg_rad = raw_input("Enter Deg or rad: ")
            if deg_rad.lower() == 'rad':
                sinh = math.sinh(self.num_3)
                return sinh

            elif deg_rad.lower() == 'deg':
                degree = math.radians(self.num_3)
                # print(degree)
                sinh = math.sinh(degree)
                return sinh

        elif self.oper == 'cosh':
            deg_rad = raw_input("Enter Deg or rad: ")
            if deg_rad.lower() == 'rad':
                cosh = math.cosh(self.num_3)
                return cosh

            elif deg_rad.lower() == 'deg':
                degree = math.radians(self.num_3)
                # print(degree)
                cosh = math.cosh(degree)
                return cosh

        elif self.oper == 'tanh':
            deg_rad = raw_input("Enter Deg or rad: ")
            if deg_rad.lower() == 'rad':
                tanh = math.tanh(self.num_3)
                return tanh

            elif deg_rad.lower() == 'deg':
                degree = math.radians(self.num_3)
                # print(degree)
                tanh = math.tanh(degree)
                return tanh

        elif self.oper == 'deg':
            degree = math.degrees(self.num_3)
            return degree

        elif self.oper == 'rad':
            radiance = math.radians(self.num_3)
            return radiance

        elif self.oper == 'exp':
            exp = math.exp(self.num_3)
            return exp

        else:
            print('This is not an Operator sign.')


# Sci.sci_calc(25, 'sqrt')
# Calculate.simple_clac(2, '+', 3)




