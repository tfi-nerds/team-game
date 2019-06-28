#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400(Summer 2019)
# Assignment: Pracitce 03
# File:       Practice_03.py
# Purpose:    Calculate ticket price of 3 different tickets
#######################################################

CLASS_A = 15.25  # global variable for ticket price A
CLASS_B = 11.50  # global variable for ticket price B
CLASS_C = 9.00  # global variable for ticket price C


def main():

    print('\n**  Justin Pawlarczyk  **\n')  # Display author's name

    # user enter number of tickets for class A
    a_tickets = int(input('Enter number of class A tickets: '))

    # user enter number of tickets for class B
    b_tickets = int(input('Enter number of class B tickets: '))

    # user enter number of tickets for class C
    c_tickets = int(input('Enter number of class C tickets: '))

    print()  # Blank Line

    total_tickets(a_tickets, b_tickets, c_tickets)  # display total price


# Defines total ticket price by calculating user entered values times global values
def total_tickets(a_price, b_price, c_price):
    total_price = CLASS_A * a_price + CLASS_B * b_price + CLASS_C * c_price

    print('Total: $', total_price)  # Display total price


main()