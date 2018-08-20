value = input('Enter the number for calculating factorial: ')
fact = 1
if value.isnumeric():
    value = int(value)
    while value > 0:
        fact = fact * value
        value = value - 1
    print(fact)
else:
    print('Value entered is not a number')
