#######################################################
# Name:       Justin Pawlarczyk
# Class:      CIS-1400
# Assignment: Practice 05b
# File:       Practice_05b.py
# Purpose:    Draw increasing square pattern
#######################################################

print('\n**  Justin Pawlarczyk  **\n')  # Display author's name

import turtle  # Turtle is used for this program

# starting length of square is 50 pixels
length = 50
turtle.speed(0)
# square is incresed by 5 pixels and turned 10 degrees for each drawn square
for squares_counted in range(0, 37):
    length += 5
    for squares_counted in range(0, 4):  # Starting length of each side turned 90 degrees
        turtle.forward(length)
        turtle.right(90)
    turtle.right(10)  # Turn turtle right 10 degrees