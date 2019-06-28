#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Homework 03 (Summer 2019)
# File:       Homework_03.py
# Purpose:    Calculate BMI
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # Display author's name

pounds = float(input('Weight: '))  # User enters weight in pounds
feet = float(input('Feet: '))  # User enters height in feet
inches = float(input('Inches: '))  # User enters inches
total_inches = feet * 12 + inches  # Formula for converting feet and inches into total inches


def main():  # main protocol

    def display_bmi(total_inches, pounds):  # Display BMI procedure

        display_bmi = pounds / (total_inches)**2 * 703  # Formula for calculating BMI
        print()  # Blank line
        print()  # Blank line
        print('Your BMI is', display_bmi)  # Displays calculated BMI to user
    display_bmi(total_inches, pounds)  # End BMI procedure


main()  # End main protocol