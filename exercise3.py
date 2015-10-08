#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues. This program take "Y" and "y" as yes, "N" and "n" as no.
The following test cases had been tested with both upper cases and lower cases

TEST CASE 1
Input:              y
                    y
Expected Output:    Are the battery terminals corroded?
                    Clean terminals and try start.
Actual Output:      Are the battery terminals corroded?
                    Clean terminals and try start.

TEST CASE 2
Input:              y
                    n
Expected Output:    Are the battery terminals corroded?
                    Replace cables and try again.
Actual Output:      Are the battery terminals corroded?
                    Replace cables and try again.

TEST CASE 3
Input:              n
                    y
Expected Output:    Does the car make a clicking noise?
                    Replace the battery.
Actual Output:      Does the car make a clicking noise?
                    Replace the battery.

TEST CASE 4
Input:              n
                    n
                    y
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Check spark plug connections.
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Check spark plug connections.

TEST CASE 5
Input:              n
                    n
                    n
                    n
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Engine is not getting enough fuel. Clean fuel pump.
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Engine is not getting enough fuel. Clean fuel pump.

TEST CASE 6
Input:              n
                    n
                    n
                    y
                    n
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Does your car have fuel injection?
                    Check to ensure the choke is opening and closing.
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Does your car have fuel injection?
                    Check to ensure the choke is opening and closing.

TEST CASE 7
Input:              n
                    n
                    n
                    y
                    y
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Does your car have fuel injection?
                    Get it in for service.
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Does your car have fuel injection?
                    Get it in for service.

TEST CASE 8
Input:              a
Expected Output:    Error
Actual Output:      Error

TEST CASE 9
Input:              y
                    a
Expected Output:    Are the battery terminals corroded?
                    Error
Actual Output:      Are the battery terminals corroded?
                    Error

TEST CASE 10
Input:              n
                    b
Expected Output:    Does the car make a clicking noise?
                    Error
Actual Output:      Does the car make a clicking noise?
                    Error

TEST CASE 11
Input:              n
                    n
                    c
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Error
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Error

TEST CASE 12
Input:              n
                    n
                    n
                    d
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Error
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Error

TEST CASE 13
Input:              n
                    n
                    n
                    y
                    e
Expected Output:    Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Does your car have fuel injection?
                    Error
Actual Output:      Does the car make a clicking noise?
                    Does the car crank up but fail to start?
                    Does the engine start and then die?
                    Does your car have fuel injection?
                    Error
"""

__author__ = 'Zixiao Yang'
__email__ = "zeke.yang@mail.utoronto.ca"
__copyright__ = "2015 Zeke Yang"
__date__ = "October 09, 2015"

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "October 09, 2015"


def diagnose_car():

    respond = raw_input("Is the car silent when you turn the key?")  # gather input by assigning variable the value
    if respond == 'y' or respond == 'Y':
        respond = raw_input("Are the battery terminals corroded?")
        if respond == 'y' or respond == 'Y':  # User input is case-sensitive, accepting "y" or "Y"
            print("Clean terminals and try starting again")
        elif respond == 'n' or respond == 'N':  # User input is case-sensitive, accepting "n" or "N"
            print ("Replace cables and try again.")
        else:
            print ("Error")  # any input other than "y", "Y", "n" or "N" will generate "Error"
    elif respond == 'n' or respond == 'N':
        respond = raw_input("Does the car make a clicking noise?")
        if respond == 'y' or respond == 'Y':
            print ("Replace the battery.")
        elif respond == 'n' or respond == 'N':
            respond = raw_input("Does the car crank up but fail to start")
            if respond == 'y' or respond == 'Y':
                print ("Check spark plug connections.")
            elif respond == 'n' or respond == 'N':
                respond = raw_input("Does the engine start and then die?")
                if respond == 'y' or respond == 'Y':
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

diagnose_car()  # calling the function