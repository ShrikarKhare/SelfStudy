'''
Write a function, befitting_brackets, that takes in a string as an argument. 
The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }

test_00:
befitting_brackets('(){}[](())') # -> True
test_01:
befitting_brackets('({[]})') # -> True
test_02:
befitting_brackets('[][}') # -> False
'''

def befitting_brackets(string):
    stack = []
    brackets = {
        '(':')',
        '[':']',
        '{':'}'
    }

    for i in string:
        if i in brackets:
            stack.append(brackets[i])
        else:
            if i in stack:
                stack.pop()
            else:
                return False 
    return len(stack) == 0