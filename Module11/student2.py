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

class Student(Person):
    def __init__(self, id_no, lname, fname, major='Computer Science', gpa=0.0):
        self._id = id_no
        super().__init__(lname, fname)
        self._major = major
        self._gpa = gpa
    def change_major(self, new_major):
        self._major = new_major
    def update_gpa(self, new_gpa):
        self._gpa = new_gpa
    def display(self):
        output = str(self._id) + ": " + self.last_name + ", " + self.first_name + "\n"
        #output = output + "Started on: " + datetime.datetime.strftime(self.start_date, '%m-%d-%Y') + "\n"
        output = output + "Majoring in " + self._major + " with a GPA of " + str(self._gpa)
        return output
    def __str__(self):
        return self.first_name + " " + self.last_name + ", a " + self._major + "major with a GPA of " + str(self._gpa)

    def __repr__(self):
        return self.first_name + " " + self.last_name + ": " + self._major + "," + str(self._gpa)

