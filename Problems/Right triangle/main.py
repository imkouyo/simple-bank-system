class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def calculate(self):
        print(round((self.a * self.b) / 2, 1))


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if input_c ** 2 == input_a ** 2 + input_b ** 2:
    triangle = RightTriangle(input_c, input_a, input_b)
    triangle.calculate()
else:
    print("Not right")
