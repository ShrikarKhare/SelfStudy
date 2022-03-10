'''
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.

test_00:
compress('ccaaatsss') # -> '2c3at3s'
test_01:
compress('ssssbbz') # -> '4s2bz'
test_02:
compress('ppoppppp') # -> '2po5p
'''

def compress(s):
    s += "!"
    i = 0 
    j = 0
    result = []

    while j  < len(s):
        number = j - i
        if s[i] == s[j]:
            j += 1
        else:
            if number == 1:
                result.append(s[i])
            else:
                result.append(str(number))
                result.append(s[i])
            i=j
    print(result)
    return ''.join(result)

print(compress('ccaaatsss')) # -> '2c3at3s'
print(compress('ssssbbz')) # -> '4s2bz'

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''