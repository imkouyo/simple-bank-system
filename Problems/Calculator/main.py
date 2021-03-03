# put your python code here
class Calculator:
    def __init__(self, num_one, num_two):
        self.number_one = num_one
        self.number_two = num_two


class Add(Calculator):
    def calculate(self):
        print(self.number_one + self.number_two)


class Sub(Calculator):
    def calculate(self):
        print(self.number_one - self.number_two)


class Mul(Calculator):
    def calculate(self):
        print(self.number_one * self.number_two)


class Div(Calculator):
    def calculate(self):
        if self.number_two == 0:
            print("Division by 0!")
        else:
            print(self.number_one / self.number_two)


class Mod(Calculator):
    def calculate(self):
        if self.number_two == 0:
            print("Division by 0!")
        else:
            print(self.number_one % self.number_two)


class Pow(Calculator):
    def calculate(self):
        print(pow(self.number_one, self.number_two))


class Divide(Calculator):
    def calculate(self):
        if self.number_two == 0:
            print("Division by 0!")
        else:
            print(self.number_one // self.number_two)


one = float(input())
two = float(input())
arithmetic = input()

if arithmetic == '+':
    Add(one, two).calculate()
elif arithmetic == '-':
    Sub(one, two).calculate()
elif arithmetic == '*':
    Mul(one, two).calculate()
elif arithmetic == '/':
    Div(one, two).calculate()
elif arithmetic == 'mod':
    Mod(one, two).calculate()
elif arithmetic == 'pow':
    Pow(one, two).calculate()
elif arithmetic == 'div':
    Divide(one, two).calculate()
