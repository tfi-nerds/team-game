#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Project 01 (Summer 2019)
# File:       Project_01.py
# Purpose:    Calculate factorial of integer entered by user
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # Display author's name

INTEGER_INPUT = int(input('Enter an integer: '))  # User enters integer
increment_value, total = 1, 1  # defines increment of 1 and total as 1, total can't = 0

print(INTEGER_INPUT, '! = ', end='', sep='')  # Start of print statement to match screenshot

for user_integer in range(0, INTEGER_INPUT):  # For loop running user's input
    total = total * increment_value  # Formula for displaying how fractal is calculated
    if (increment_value < INTEGER_INPUT):  # Defines stopping point for above line
        print(increment_value, 'x ', end='')  # Continuation of first print statement to display on same line
        increment_value += 1  # Defines increment value used in formula of line 17
    else:
        print(increment_value, '=', total)  # Final line of first print statement to display on same line