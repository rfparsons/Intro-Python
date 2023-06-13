"""
Program: student_driver.py
Author: Bobby Parsons

Tests the Student class and its functions
"""
# Student Driver? Better be careful!
import student
from datetime import datetime

if __name__ == "__main__":
    person_bobby = student.Person("Parsons", "Robert")
    student_bobby = student.Student(person_bobby, "Computer Science", datetime(2019, 1, 7), 4.0)

    print(student_bobby.display())
    print("======================")
    student_bobby.change_major("Being Awesome!")
    student_bobby.update_gpa(3.0)
    print(student_bobby.display())