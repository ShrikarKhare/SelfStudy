'''
Write a function, uncompress, that takes in a string as an argument. 
The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times 
consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

test_00:
uncompress("2c3a1t") # -> 'ccaaat'
test_01:
uncompress("4s2b") # -> 'ssssbb'
'''

def uncompress(s):
    numbers = '0123456789'
    i = 0
    j = 0
    result = []

    for char in s:
        if char in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j]*num)
            j += 1
            i = j 
    return ''.join(result)

print(uncompress("2c3a1t"))
print(uncompress("4s2b"))
print(uncompress("127y"))

'''
n : number of groups
m = max num for any group
Time Complexity: O(n*m)
Space Complexity: O(n*m)
'''