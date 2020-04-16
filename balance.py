# Malcolm Jeffers
# CS261 Assignment 2
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
    # Search if the character is in open list. If it is then
    # place it on the stack. If a character is in the closing list,
    # call the item at the top of the stack. If it corresponds. Then
    # remove it from the stack.
    for i in input_string:
        if i in open:
            stack.append(i)
        if i in close:
            if len(stack) >= 1:
                if stack[-1] == close[i]:
                    del stack[-1]
            else:
                return False
    # If the stack is empty at the end then return True.
    if stack == []:
        return True
    else:
        return False



if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY
    #_input_string = "4[56]"
    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))
