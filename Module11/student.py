"""
Program: student.py
Author: Bobby Parsons

Contains the Student and Person classes to store informtion about students
"""
import datetime

class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):  # Constructor sets all to no value
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return self.last_name + ", " + self.first_name + " lives at " + self.address

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return self.last_name + ", " + self.first_name + "\n" + self.address

class Student:
    def __init__(self, person, major, start_date, gpa):
        self.person = person
        self.major = major
        self.start_date = start_date
        self.gpa = gpa
    def change_major(self, new_major):
        self.major = new_major
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
    def display(self):
        output = self.person.display() + "\n"
        output = output + "Started on: " + datetime.datetime.strftime(self.start_date, '%m-%d-%Y') + "\n"
        output = output + "Majoring in " + self.major + " with a GPA of " + str(self.gpa)
        return output
    def __str__(self):
        return str(self.person) + ", a " + self.major + "major with a GPA of " + str(self.gpa)

    def __repr__(self):
        return str(self.person) + ": " + self.major + "," + str(self.gpa)

