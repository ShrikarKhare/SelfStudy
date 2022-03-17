'''
Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. 
The function should return the maximum sum of non-adjacent items in the list. 
There is no limit on how many items can be taken into the sum as long as they are not adjacent.

For example, given:

[2, 4, 5, 12, 7]

The maximum non-adjacent sum is 16, because 4 + 12. 
4 and 12 are not adjacent in the list.
test_00:
nums = [2, 4, 5, 12, 7]
non_adjacent_sum(nums) # -> 16
test_01:
nums = [7, 5, 5, 12]
non_adjacent_sum(nums) # -> 19
'''

def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
    if i in memo: return memo[i]
    if i >= len(nums): return 0

    include = nums[i] + _non_adjacent_sum(nums, i+2, memo)
    exclude = _non_adjacent_sum(nums, i+1, memo)

    memo[i] = max(include,exclude)
    return memo[i]


nums = [7, 5, 5, 12]
print(non_adjacent_sum(nums))
nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums))
'''
n: length of nums
Time Complexity: O(n)
Space Complexity: O(n)
'''