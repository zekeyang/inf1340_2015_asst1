#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

Inputs: None

Expected outputs: Number of sides

Outputs: Name of shape

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

    side_number = raw_input("How many sides?")
    prefix = 'The shape is named ' # Develops a formal statement
    if side_number == '3':
        print(prefix + "triangle")
    elif side_number == '4':
        print(prefix + "quadrangle") # Easily labels squares, rectangles, and parallelograms
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
        print("Error") # occurs if there is a space after the question or a number between 3 and 10 is not inputted
    return
name_that_shape()

