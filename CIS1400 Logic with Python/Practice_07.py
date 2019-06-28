#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Practice #7 (Summer 2019)
# File:       Practice_07.py
# Purpose:    Calculate Gross Pay for Worker
#######################################################

MIN_HOURS = 0  # Set Minimum Hours
MAX_HOURS = 40  # Set Maximum Hours

MIN_PAY_RATE = 7.50  # Set Minimum Pay Rate
MAX_PAY_RATE = 18.25  # Set Maximum Pay Rate


def main():  # start main procedure
    print('\n** Justin Pawlarczyk **\n')  # Display user name

    hours = get_hours()  # variable stated to retrieve hours entered by user
    rate = get_rate()  # variable stated to retrieve pay rate entered by user

    gross_pay = hours * rate  # Formula for calculating gross pay

    print()  # Blank line
    print('Gross Pay: $', format(gross_pay, ',.2f'))  # Display gross calculated gross pay to user


# Function that retrieves hours from user if entered properly, if not scold user and start again
def get_hours():

    print()  # Blank line

    hours_worked = float(input('Enter hours worked: '))  # Prompt user to enter hours
    while hours_worked < MIN_HOURS or hours_worked > MAX_HOURS:  # Set conditions for sucess or error
        print()  # Blank line
        print('ERROR - Invalid number of hours!')  # Display error prompt to re-enter valid number

        hours_worked = float(input('Enter hours worked: '))  # Prompt user to enter hours

        print()  # Blank line
    return hours_worked  # Restart function


# Function that retrieves pay rate from user if entered properly, if not scold user and start again
def get_rate():

    print()  # Blank line

    rate_paid = float(input('Enter hourly rate: '))  # Prompt user to enter pay
    while rate_paid < MIN_PAY_RATE or rate_paid > MAX_PAY_RATE:  # Set conditions for sucess or error
        print()  # Blank line

        print('ERROR- Invalid number of hourly rate!')  # Display error prompt to re-enter valid number

        rate_paid = float(input('Enter hourly rate: '))  # Prompt user to enter pay

    print()  # Blank line
    return rate_paid  # Restart function


main()  # End main procedure