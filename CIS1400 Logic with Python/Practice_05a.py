#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Practice_05a
# File:       Practice_05a.py
# Purpose:    Ask user for positve number then add sum
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # Display author's name
print()  # Blank Space

number = 1  # Initialize the number variable to the start the loop
total = 0  # Start total at 0

# Iterate the loop while the number is greater than 0
while number != 0:
    number = float(input('Enter a positive number (or zero when done): '))  # Prompt user to enter number
    total += number  # Add total of user numbers entered unless user enters 0

print()  # Blank Line
print('Sum:', total)  # Display total