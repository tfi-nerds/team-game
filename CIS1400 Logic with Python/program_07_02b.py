def main():

    do_another = 'Y'

    while do_another == 'Y':
        show_retail()

        print()
        do_another = input('Do you have another item (y/n)? ')

        do_another = do_another.upper()

        while do_another != 'Y' and do_another != 'N':
            print()
            print('You must enter \'y\' or \'n\'.')
            do_another = input('Do you have another item (y/n)? ')
            do_another = do_another.upper()
            print()

def show_retail():
    valid = False

    print()

    wholesale_string = input('Enter an item\'s wholesale cost: ')

    while not valid:
        if is_float(wholesale_string):
            wholesale = float(wholesale_string)

            if wholesale > 0:
                valid = True

        if not valid:
            print()
            print('The cost must be a number greater than 0')
            print('Please re-enter the item\'s wholesale cost: ', end='')
            wholesale_string = input()

    retail = wholesale * 2.5

    print('The retail price is $' + format(retail, ',.2f'))

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

main()
