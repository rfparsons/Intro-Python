"""
Program: function_assignment.py
Author: Bobby Parsons

Program to calculate pay for a number of hours worked
"""

def hourly_employee_input():
    """Asks the user for an employee name, hours worked, and an hourly rate and prints a calculation of the weekly pay"""
    name = input("Employee name: ")
    hours_str = input("Hours worked: ") 
    try:
        hours = int(hours_str)
        if hours < 0:
            raise ValueError
    except:
        print("Invalid input! Please enter a positive integer number of hours.")
        raise ValueError #raises error anyway to end the program
    rate_str = input("Rate per hour: ")
    try:
        rate = float(rate_str)
        if rate < 0:
            raise ValueError
    except:
        print("Invalid input! Please enter a positive decimal rate per hour.")
        raise ValueError
    earned = hours * rate
    print(name + " worked " + hours_str + " hours to earn ${0:.2f}".format(earned))

if __name__ == "__main__":
    try:
        hourly_employee_input()
    except:
        pass #Had to add the except or I got an unexpected EOF error
