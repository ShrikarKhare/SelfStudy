'''
Write a function, decompress_braces, that takes in a compressed string as an argument. 
The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.


test_00:
decompress_braces("2{q}3{tu}v")
# -> qqtututuv 
test_01:
decompress_braces("ch3{ao}")
# -> chaoaoao
'''

def decompress_braces(string):
    stack = []
    numbers = '123456789'
    for i in string:
        if i in numbers:
            stack.append(int(i))
        else:
            if i == '}':
                segment = ''
                while isinstance(stack[-1], str):
                    popped = stack.pop()
                    segment = popped + segment 
                num = stack.pop()
                stack.append(segment * num)
            elif i != '{':
                stack.append(i)
    return ''.join(stack)

'''
s: length of string
m: count of brace pairs
Time Complexity: O((9^m) * s)
Space Complexity: O((9^m) * s)
'''