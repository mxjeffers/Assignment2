# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False
def is_balanced(input_string):
    # initialize an empty list as the stack
    stack = []
    open = ["(", "[", "{"]

    close = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    # iterate over each character in the string
    for i in input_string:
        if i in open:
            stack.append(i)
        if i in close:
            if len(stack) >= 1:
                if stack[-1] == close[i]:
                    del stack[-1]
            else:
                return False
    if stack == []:
        return True
    else:
        return False

        return False


if __name__ == '__main__':
    # get input string
    #_input_string = sys.argv[1]  # DO NOT MODIFY
    _input_string = "4[56]"
    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))
