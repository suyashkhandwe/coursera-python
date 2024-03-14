"""Module for assignment 4.6."""

# Problem Statement
# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

def computepay(hours_worked_str, rate_per_hour_str):
    hours_worked = float(hours_worked_str)
    rate_per_hour = float(rate_per_hour_str)
    
    gross_pay = hours_worked * rate_per_hour
    
    if hours_worked > 40:
        gross_pay = gross_pay + (hours_worked - 40) * rate_per_hour / 2 # 1x rate is already computed. Add 0.5x rate for the number of hours over 40
    
    return gross_pay


hours_worked_str = input('Enter the total number of hours worked: ')
rate_per_hour_str = input('Enter the hourly rate: ')

print('Pay', computepay(hours_worked_str, rate_per_hour_str))