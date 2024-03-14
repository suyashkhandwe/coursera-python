"""Module for assignment 2.3."""

# Problem Statement
# 2.3 Write a program to prompt the user for hours and 
# rate per hour using input to compute gross pay.
#
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking or bad user data.

hours_worked = input('Enter the number of hours worked: ')
rate_per_hour = input('Enter the rate per hour: ')
gross_pay = float(hours_worked) * float(rate_per_hour)
print('Pay:', gross_pay)
