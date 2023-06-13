"""
Program: file_io.py
Author: Bobby Parsons

Allows a user to enter test scores, have them placed into a file and then read back from the file
"""
FILE_NAME = "student_info.txt"

def write_to_file(student_info, filename):
    with open(filename, 'a') as f:
        f.write(str(student_info) + "\n")
        f.close()

def get_student_info(name):
    num_scores = int(input("How many test scores for " + name + "? "))
    student_tuple = name, []

    for i in range (0, num_scores):
        score = int(input("Enter score #" + str(i+1) + ": "))
        student_tuple[1].append(score)
    #print(student_tuple)
    write_to_file(student_tuple, FILE_NAME)

def read_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()
        for line in lines:
            print(line)

if __name__ == "__main__":
    open(FILE_NAME,"w").close() #blanks the file to reset after every time
    get_student_info("Bobby")
    get_student_info("Robert")
    get_student_info("Bob")
    get_student_info("Rob")
    read_from_file(FILE_NAME)