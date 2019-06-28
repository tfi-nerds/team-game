

number1 = 1

while number1 != -1:
    number1 = int(input('Enter a number greater than zero (or -1 to exit): '))

    number2 = int(input('Enter a different number greater than zero: '))

if number1 > number2:
    print()
    print('The first number is greater than the second')
else:
    print()
    print('The second number is greater than the first')

print()