#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Zixiao Yang'
__email__ = "zeke.yang@mail.utoronto.ca"
__copyright__ = "2015 Zeke Yang"
__date__ = "October 09, 2015"

__author__ = "Paniz Pakravan"
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "October 09, 2015"

buying_price = 900.00
buying_shares = 2000
buying_total = buying_price * buying_shares
buying_commission = buying_total * 0.03
buying_cost = buying_total + buying_commission
print "Total cost of buy in is $", buying_cost

selling_price = 942.75
selling_shares = 2000
selling_total = selling_price * selling_shares
selling_commission = selling_total * 0.03
selling_income = selling_total - selling_commission
print "Total earn of selling is $", selling_income

profit = selling_income - buying_cost # Negative amount; money has been lost
print "Profit: $", profit
