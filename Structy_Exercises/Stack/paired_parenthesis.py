'''
Write a function, paired_parentheses, that takes in a string as an argument. 
The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.

test_00:
paired_parentheses("(david)((abby))") # -> True
test_01:
paired_parentheses("()rose(jeff") # -> False
'''

def paired_parenthesis(string):
    counter = 0

    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
            if counter < 0:
                return False
    return counter == 0

print(paired_parenthesis("(david)((abby))"))

'''
n: length of string
Time Complexity: O(n)
Space Complexity: O(1)
'''