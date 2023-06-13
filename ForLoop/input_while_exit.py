"""
Program: input_while_exit.py
Author: Bobby Parsons

Gets 3 numbers from the user and prints them back out, this time you can quit if you want
"""
if __name__ == "__main__":
    NEEDED_INPUTS = 3
    input_list = []
    correct_inputs = 0
    user_input = -1
    end_program = False

    print("Type 'Quit' at any time to quit")
    while correct_inputs != NEEDED_INPUTS:
        while user_input > 100 or user_input < 1:
            try:
                input_str = input(f"Input a number between 1 and 100: ({correct_inputs + 1} of {NEEDED_INPUTS}) ")
                user_input = int(input_str)
                if user_input > 100 or user_input < 1:
                    print("Invalid value! Please only enter numbers between 1 and 100")
            except:
                if input_str.lower() == "quit":
                    end_program = True
                    break
                print("Invalid value! Please only enter integers")
        if end_program:
            break
        input_list.append(user_input)
        correct_inputs = correct_inputs + 1
        user_input = -1
            
    print()
    for num in input_list:
        if num != input_list[-1]: #check to make sure it's not the last item in the list
            print(f"{num}, ", end='')
        else:
            print(num)


# declare a list variable
# declare a sentinel value for user input
# prompt get the user input (indicating sentinel value to stop)
# while sentinel value is not stopping value 
#       while user input is not good (in range)
#             prompt user for good input
#       store in list
#       prompt and get the next user input

# print the list using a for loop