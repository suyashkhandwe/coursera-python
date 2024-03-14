"""Module for assignment 3.1."""

# Problem Statement
# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# 
# Pay the hourly rate for the hours up to 40 
# and 1.5 times the hourly rate for all hours worked above 40 hours.
# 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# 
# You should use input to read a string and float() to convert the string to a number.
# 
# Do not worry about error checking the user input - assume the user types numbers properly.

hours_worked_str = input('Enter the total number of hours worked: ')
rate_per_hour_str = input('Enter the hourly rate: ')

hours_worked = float(hours_worked_str)
rate_per_hour = float(rate_per_hour_str)

gross_pay = hours_worked * rate_per_hour

if hours_worked > 40:
    # 1x rate is already computed. Add 0.5x rate for the number of hours over 40
    gross_pay = gross_pay + (hours_worked - 40) * rate_per_hour / 2

print(gross_pay)
