"""
Program: employee.py
Author: Bobby Parsons

Contains a class to store information about an employee, plus a driver to demonstrate the class
"""

import datetime


class Employee:
    """Employee Class """

    # Constructor
    def __init__(self, lname, fname, addr, phone, salaried, start_date, salary):
        self._last_name = str(lname)
        self._first_name = str(fname)
        self._address = str(addr)
        self._phone_number = str(phone)
        self._salaried = bool(salaried)
        self._start_date = datetime.datetime.strptime(start_date, '%m-%d-%Y')
        self._salary = float('%.2f' % float(salary))

    def display(self):
        output = self._first_name + " " + self._last_name + "\n"
        output = output + self._address + "\n"
        if self._salaried:
            output = output + "Salaried employee: $" + '%.2f' % self._salary + "/year\n"
        else:
            output = output + "Hourly employee: $" + '%.2f' % self._salary + "/hour\n"
        output = output + "Start date: " + datetime.datetime.strftime(self._start_date, '%m-%d-%Y')
        return output


# Driver
emp = Employee('Patel', 'Sasha', '123 Main Street\nUrban, Iowa', '(515) 555-555', True, '6-28-2019',
               40000)  # call the constructor, needs to have a first and last name in parameter
print(emp.display())  # display returns a str, so print the information
del emp  # clean up!
