#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Homework #2
# File:       homework_02.py
# Purpose:    Grocery List
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # Display author's name

# User enters values in formula for solving a trapezoid strarting with base a. User is prompted to enter base a
item1 = float(input('Enter the length of the first base: '))
print()

# Prompt user to enter base b in the formula for solving a trapezoid.
item2 = float(input('Enter the length of the second base: '))
print()

# Prompt user to enter height value in the formula for solving a trapezoid.
item3 = float(input('Enter the height of the trapezoid: '))
print()

# How the formula for solving a trapezoid is written using python.
area = (item1 + item2) / 2 * item3

# Display the solution to the formula using user's entered values.
print('The area of the trapezoid is: ',  area)