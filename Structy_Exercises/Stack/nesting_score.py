'''
Write a function, nesting_score, that takes in a string of brackets as an argument. 
The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
You may assume that the input only contains well-formed square brackets.

test_00:
nesting_score("[]") # -> 1
test_01:
nesting_score("[][][]") # -> 3
'''

def nesting_score(string):
    stack = [0]

    for i in string:
        if i == '[':
            stack.append(0)
        else:
            popped = stack.pop()
            if popped == 0:
                stack[-1] += 1
            else:
                stack[-1] += 2* popped 
    return stack[0]

'''
n: length of string
Time Complexity: O(n)
Space Complexity: O(n)
'''