numbers = []
while True:
    number = input()
    if number != '.':
        numbers.append(float(number))
    else:
        print(min(numbers))
        break
