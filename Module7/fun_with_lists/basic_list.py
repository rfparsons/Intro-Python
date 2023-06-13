"""
Program: basic_list.py
Author: Bobby Parsons

Contains functions to put 3 user-inputted values into a list
"""

def make_list():
    final_list = []
    for i in range(0, 3):
        num = get_input()
        #print(type(num))
        final_list.insert(i, int(num))
    return final_list


def get_input():
    user_input = input("Enter a number:")
    #user_input_int = int(user_input)
    try:
        str(int(user_input))
        return user_input #_int
    except:
        raise ValueError

if __name__ == "__main__":
    num = get_input()
    print(num)
    #print(type(num))