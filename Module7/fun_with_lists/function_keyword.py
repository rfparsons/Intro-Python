"""
Program: function_keyword.py
Author: Bobby Parsons

Has a function to average scores and output other information entered
"""

def average_scores(*args, **kwargs):
    # Use *args for average calculation
    total = 0
    for key, value in kwargs.items():
        print("%s: %s" % (key, value))
    for score in args:
        total = score + total
    return total / len(args)
    
if __name__ == '__main__':
    print("Average: " + str(average_scores(4, 3, 2, 4, name="Michelle Ruse", course="DMACC Sample Code Writing", gpa="Immeasurable")))
    print()
    print("Average: " + str(average_scores(10, 8.5, 9, 10, 10, 8, 9, 7, name="Bobby Parsons", status="Pretty alright", languages_taken=["C++", "C#", "Python"])))
    print()
    print("Average: " + str(average_scores(100, 30, 30, 30, 20, name="Guy Who Got Overconfident and Stopped Studying", attendance="Marginal", panic="starting soon")))

# if __name__ == '__main__':
#     print(average_scores(4, 3, 2, 4, name='Michelle Ruse', course="DMACC Sample Code Writing", gpa="Immeasurable") #something weird in this line making the code not work...
    # Retyping it fixed it
#     print(f"average: {average_scores(10, 10, 10, 10, 10, 10, 10, 4, name="Bobby Parsons", course="Introduction to Introductions", gpa="3")}")
