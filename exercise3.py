#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Zixiao Yang'
__email__ = "zeke.yang@mail.utoronto.ca"
__copyright__ = "2015 Zeke Yang"
__license__ = "MIT License"

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__date__ = "October 09, 2015"
__program__ = "Information Systems & Design"

def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: None

    Expected Outputs: Y or y, N or n

    Outputs: Instructed responses such as "Replace your battery", or "Error"

    """
    respond = raw_input("Is the car silent when you turn the key?")
    if respond == 'y' or respond == 'Y': # letters are case-sensitive
        respond = raw_input("Are the battery terminals corroded?")
        if respond == 'y' or respond == 'Y':
            print("Clean terminals and try starting again")
        elif respond == 'n' or respond == 'N': # "else if", creates a branch under the original "if"
            print ("Replace cables and try again.")
        else:
            print ("Error") # a different inputted letter, or a space after the question, will result in an error
    elif respond == 'n' or respond == 'N':
        respond = raw_input("Does the car make a clicking noise?")
        if respond == 'y' or respond == 'Y':
            print ("Replace the battery.")
        elif respond == 'n' or respond == 'N':
            respond = raw_input("Does the car crank up but fail to start")
            if respond == 'y' or respond == 'Y':
                print ("Check spark plug connections.")
            elif respond =='n' or respond == 'N':
                respond = raw_input("Does the engine start and then die?")
                if respond == 'y' or respond =='Y':
                    respond = raw_input("Does your car have fuel injection?")
                    if respond == 'n' or respond == 'N':
                        print("Check to ensure the choke is opening and closing")
                    elif respond == 'y' or respond == 'Y':
                        print("Get it in for service.")
                    else:
                        print("Error")
                elif respond == 'n' or respond == 'N':
                    print("Engine is not getting enough fuel. Clean fuel pump.")
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")

diagnose_car()