#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400(Summer 2019)
# Assignment: Homework 04
# File:       Homework_04.py
# Purpose:    Convert seconds into days/hours/minutes/nothing
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # display author's name

# user defined variables depending on amount of seconds entered
seconds = int(input('Enter the number of seconds: '))
minutes = seconds / 60
hours = minutes / 60
days = hours / 24

if seconds >= 86400:  # displays number of days if user enters 86400 or more
        print()  #Blank Line
        print(seconds, 'seconds is equal to', days, 'days.')
else:
    if seconds >= 3600:  # displays number of hours if user enters 3600 or more
        print()  #Blank Line
        print(seconds, 'seconds is equal to', hours, 'hours.')
    else:
        if seconds >= 60:  # displays number of hours if user enters 60 or more
            print()  #Blank Line
            print(seconds, 'seconds is equal to', minutes, 'minutes.')