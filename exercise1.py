#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2015. Calculating gain or loss

This module prints the amount of money that Lakshmi has remaining
after the stock transactions.
Math expression: (942.75*2000-942.75*2000*0.03)-(900*2000+900*2000*0.03)=-25065
INPUT:      No user input, but variable assignment gives the value
            Buying Price: $900
            Buying Stocks: 2000
            Selling Price: $942.75
            Selling Stocks: 2000
            Buy Sell Commission Rate: 0.03
EXPECTED OUTPUT: -25065
ACTUAL OUTPUT: -25065

"""

__author__ = "Zixiao Yang"
__email__ = "zeke.yang@mail.utoronto.ca"
__copyright__ = "2015 Zeke Yang"
__date__ = "October 09, 2015"

__author__ = "Paniz Pakravan"
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "October 09, 2015"

buying_price = 900.00
buying_shares = 2000
buying_total = buying_price * buying_shares  # calculating total price for buying 2000 stocks
buying_commission = buying_total * 0.03  # calculating commission of buying stocks
buying_cost = buying_total + buying_commission  # calculating the total cost for buying stocks
print "Total cost of buy in is $", buying_cost

selling_price = 942.75
selling_shares = 2000
selling_total = selling_price * selling_shares  # calculating total gain for selling 2000 stocks
selling_commission = selling_total * 0.03  # calculating commission of selling stocks
selling_income = selling_total - selling_commission  # calculating earning by having selling total - commission cost
print "Total earn of selling is $", selling_income

profit = selling_income - buying_cost  # calculating final profit by having total earnings - total cost
print "Profit: $", profit  # print final profit, actual output = expected output
