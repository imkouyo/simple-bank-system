numbers = []
while True:
    number = input()
    if number != '.':
        numbers.append(int(number))
    else:
        print(sum(numbers) / len(numbers))
        break

