#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400(Summer 2019)
# Assignment: Homework 05
# File:       Homework_05.py
# Purpose:    Calculate distance of moving train
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # Display author's name

# User is prompted to input speed and time
speed = float(input('Speed of train in MPH: '))
time = float(input('Number of hours traveled: '))

print()  # Blank line
print()  # Blank line

# Define variables used in table
hour = time / time
distance = hour * speed

print('Hour   Distance')  # Displays each column
print('____   ________')  # Displays lines under column
while hour <= 12:  # set while loop to 12 hour max to match screen shot
    print(int(hour), '    ', int(distance), '    ')  # print hours and distance
    hour += 1  # increment of 1 set to provide each hour x distance
    distance = hour * speed  # formula for calculating distance