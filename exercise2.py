#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

TEST CASE 1
Inputs:             2
Expected outputs:   Error
Actual Outputs:     Error

TEST CASE 2
Inputs:             3
Expected outputs:   triangle
Actual Outputs:     triangle

TEST CASE 3
Inputs:             4
Expected outputs:   quadrangle
Actual Outputs:     quadrangle

TEST CASE 4
Inputs:             5
Expected outputs:   pentagon
Actual Outputs:     pentagon

TEST CASE 5
Inputs:             6
Expected outputs:   hexagon
Actual Outputs:     hexagon

TEST CASE 6
Inputs:             7
Expected outputs:   heptagon
Actual Outputs:     heptagon

TEST CASE 7
Inputs:             8
Expected outputs:   octagon
Actual Outputs:     octagon

TEST CASE 8
Inputs:             9
Expected outputs:   enneagon
Actual Outputs:     enneagon

TEST CASE 9
Inputs:             10
Expected outputs:   decagon
Actual Outputs:     decagon

TEST CASE 10
Inputs:             11
Expected outputs:   Error
Actual Outputs:     Error

"""

__author__ = 'Zixiao Yang'
__email__ = "zeke.yang@mail.utoronto.ca"
__copyright__ = "2015 Zeke Yang"
__date__ = "October 09, 2015"

__author__ = "Paniz Pakravan"
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "October 09, 2015"


def name_that_shape():

    side_number = raw_input("How many sides?")  # Gather user input
    prefix = "The shape is named "  # Assigning a string value
    if side_number == '3':  # Using if...elif...else statement to check user input and have correct output
        print(prefix + "triangle")
    elif side_number == '4':
        print(prefix + "quadrangle")
    elif side_number == '5':
        print(prefix + "pentagon")
    elif side_number == '6':
        print(prefix + "hexagon")
    elif side_number == '7':
        print(prefix + "heptagon")
    elif side_number == '8':
        print(prefix + "octagon")
    elif side_number == '9':
        print(prefix + "enneagon")
    elif side_number == '10':
        print(prefix + "decagon")
    else:
        print("Error")  # occurs if user NOT input a number between 3 and 10
    return
name_that_shape()  # calling the function

