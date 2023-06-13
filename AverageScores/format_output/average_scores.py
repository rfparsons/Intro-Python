'''
Program to average the scores of a student
Author: Bobby Parsons
'''
def average(number_of_scores):
    total = 0
    for i in range(0 , number_of_scores):
        score = input("Enter score #" + str(i+1) + ": ")
        total = total + int(score)
    return total / number_of_scores

if __name__ == "__main__":
    firstname = input("Enter student first name: ")
    lastname = input("Enter student last name: ")
    age = input("Enter student age:")
    average = average(3)

    print(lastname + ", " + firstname)
    print("Age: " + age)
    print("Average test score: {0:.2f}".format(average))

# Enter student first name: Bobby
# Enter student last name: Parsons
# Enter student age:21
# Enter score #1: 89
# Enter score #2: 91
# Enter score #3: 85
# Parsons, Bobby
# Age: 21
# Average test scores: 88.33

# Enter student first name: Robert
# Enter student last name: Parsons
# Enter student age:21
# Enter score #1: 98
# Enter score #2: 77
# Enter score #3: 82
# Parsons, Robert
# Age: 21
# Average test scores: 85.67