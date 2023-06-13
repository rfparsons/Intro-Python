"""
Program: student_driver.py
Author: Bobby Parsons

Tests the Student class and its functions
"""
# Student Driver? Better be careful!
import student2 as student
from datetime import datetime

if __name__ == "__main__":
    # student_bobby = student.Student("Parsons", "Robert", "Computer Science", datetime(2019, 1, 7), 4.0)

    # print(student_bobby.display())
    # print("======================")
    # student_bobby.change_major("Being Awesome!")
    # student_bobby.update_gpa(3.0)
    # print(student_bobby.display())
    
    # Driver
    my_student = student.Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = student.Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = student.Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student