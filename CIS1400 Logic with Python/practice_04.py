#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Practice 04
# File:       practice_04.py
# Purpose:    Calculate amount of change in pocket
#######################################################

# Prompt user to enter amount of each coin in pocket.
number_of_pennies = int(input('Enter number of pennies: '))
number_of_nickels = int(input('Enter number of nickels: '))
number_of_dimes = int(input('Enter number of dimes: '))
number_of_quarters = int(input('Enter number of quarters: '))

print()  # Blank line.

total = number_of_pennies * 1 + number_of_nickels * 5 + number_of_dimes * 10 + number_of_quarters * 25

if total == 100:
    print('You win!! That\'s exactly a dollar ')
else:
    print('Sorry, that\'s', total, 'cents. ')



