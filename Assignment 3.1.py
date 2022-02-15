"""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
"""

hrs = float(input("Enter Hours:"))

pay_rate = float(input("Enter Pay Rate:"))

pay = 0
overtime_pay = 0

if hrs > 40.0:
    pay = 40 * pay_rate
    overtime_pay = (hrs - 40.0) * (pay_rate * 1.5)
    pay += overtime_pay
else:
    pay = (hrs * pay_rate)


print(pay)

# 420 + 78.75 
