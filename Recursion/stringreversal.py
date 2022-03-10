def reverseString(input):
    #What is the base case
    '''
        What is the smallest amount of work I can do
        in each iteration?
    '''

    if input == '' : return ''
    return reverseString(input[1:]) + input[0]

# print(reverseString("Hello"))

def is_Palindrome(input):
    if len(input) == 0 or len(input) == 1:
        return True 
    if input[0] == input[-1]:
        return is_Palindrome(input[1:-1])
    return False

# print(is_Palindrome('kayak'))