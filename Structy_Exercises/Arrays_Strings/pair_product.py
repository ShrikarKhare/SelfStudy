'''
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

test_00:
pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
test_01:
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
test_02:
pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
'''

def pair_product(numbers,target):
    seen = {}
    for  i, num in enumerate(numbers):
        complement = target/num 
        if complement in seen:
            return (i, seen[complement])
        seen[num] = i 

print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)
print(pair_product([3, 2, 5, 4, 1], 10))
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''