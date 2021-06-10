#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 5, 2021
# This program asks the user to input two points and displays the midpoint,
# distance and line equation of those two points

import math


def midpoint(x1, y1, x2, y2):
    # calculates the midpoint of two points
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    # display the midpoint as a coordinate
    midpoint = "({0:.4f}, {1:.4f})". format(midpoint_x, midpoint_y)
    return midpoint


def distance(x1, y1, x2, y2):
    # calculates the distance of two points
    distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return distance


def line(x1, y1, x2, y2):
    # calculates the line equation of two points
    m_value = ((y2-y1) / (x2-x1))
    b_value = round((y1 - (x1 * m_value)), 4)
    m_value_round = round(m_value, 4)

    # display the line equation in 'y = mx + b' form
    line_equation = "y = {0} * x + {1}". format(m_value_round, b_value)
    return line_equation


def main():
    # greet the user
    print("This program tells you the midpoint, distance and line equation of\
 two points.")
    print()
    while True:
        # get the x-coordinate of the first point
        user_point1_x_string = input("Enter the x-coordinate\
 of the first point: ")
        try:
            # check that it is a number
            user_point1_x_float = float(user_point1_x_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a number, try again.\
". format(user_point1_x_string))
    print()

    while True:
        # get the y-coordinate of the first point
        user_point1_y_string = input("Enter the y-coordinate\
 of the first point: ")
        try:
            # check that it is a number
            user_point1_y_float = float(user_point1_y_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a number, try again.\
". format(user_point1_y_string))
    print()

    while True:
        # get the x-coordinate of the second point
        user_point2_x_string = input("Enter the x-coordinate\
 of the second point: ")
        try:
            # check that it is a number
            user_point2_x_float = float(user_point2_x_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a number, try again.\
". format(user_point2_x_string))
    print()

    while True:
        # get the y-coordinate of the second point
        user_point2_y_string = input("Enter the y-coordinate\
 of the second point: ")
        try:
            # check that it is a number
            user_point2_y_float = float(user_point2_y_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a number, try again.\
". format(user_point2_y_string))
    print()

    # call functions to calculate the midpoint, distance and line equation
    midpoint_result = midpoint(user_point1_x_float, user_point1_y_float,
                               user_point2_x_float, user_point2_y_float)
    distance_result = distance(user_point1_x_float, user_point1_y_float,
                               user_point2_x_float, user_point2_y_float)
    line_result = line(user_point1_x_float, user_point1_y_float,
                       user_point2_x_float, user_point2_y_float)

    # display the midpoint, distance and line equation
    print("The midpoint of those two points is {}.". format(midpoint_result))
    print("The distance between those two points is {:.4f} units\
.". format(distance_result))
    print("The line equation of those two points is: {}.". format(line_result))
    print()


if __name__ == "__main__":
    main()
