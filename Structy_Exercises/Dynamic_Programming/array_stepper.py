'''
Write a function, array_stepper, that takes in a list of numbers as an argument. 
You start at the first position of the list. 
The function should return a boolean indicating whether or not it is possible to reach the last position of the list. 
When situated at some position of the list, you may take a maximum number of steps based on the number at that position.

For example, given:

    idx =  0  1  2  3  4  5
numbers = [2, 4, 2, 0, 0, 1]

The answer is True.
We start at idx 0, we could take 1 step or 2 steps forward.
The correct choice is to take 1 step to idx 1.
Then take 4 steps forward to the end at idx 5.
test_00:
array_stepper([2, 4, 2, 0, 0, 1]) # -> True
test_01:
array_stepper([2, 3, 2, 0, 0, 1]) # -> False
'''

def array_stepper(numbers):
    return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i ,memo):
    if i in memo: return memo[i]
    if i >= len(numbers)-1: return True 
    if numbers[i] == 0: return False
    max_steps = numbers[i]

    for step in range(1, max_steps+1):
        if _array_stepper(numbers, i+step, memo):
            memo[i] = True
            return memo[i]
    memo[i] = False 
    return memo[i]

print(array_stepper([2, 4, 2, 0, 0, 1])) # -> True
print(array_stepper([2, 3, 2, 0, 0, 1])) # -> False

'''
n: len numbers
Time Complexity: O(n^2)
Space Complexity: O(n)
'''