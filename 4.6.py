"""
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
Do not name your variable sum or use the sum() function.
"""

def computepay(hours_worked, rate_of_pay):
    # Used for holding overtime hours worked
    total_pay = None
    overtime_hours = None
    
    # If overtime was worked
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        # 40 hours worked at the standard rate of pay + overtime hours worked at the overtime rate of pay
        total_pay = (40 * rate_of_pay) + (overtime_hours * (rate_of_pay * 1.5))
    # If no overtime was worked
    else:
        total_pay = hours_worked * rate_of_pay
        
    
    return total_pay

# Use 45 hours
# Use Pay Rate of 10.50
hours = float(input("Enter Hours: "))
pay_rate = float(input("Enter Rate of Pay: "))

pay = computepay(hours, pay_rate)
print("Pay", pay)
