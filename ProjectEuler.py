# def multiples_of_3_or_5(n):
#     #return the sum of all the multiples of 3 or 5 below n
#     total = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total

# print(multiples_of_3_or_5(1000))

def even_fibonacci_numbers(n):
    #first create a list of fibonacci numbers
    fib = [1,2]
    for i in range(2, n):
        next_num = fib[-1] + fib[-2]
        if next_num >= 4e6:
            break
        fib.append(next_num)
    evenfib =[]
    for i in fib:
        if i % 2 == 0: 
            evenfib.append(i)
    return sum(evenfib)
    
print(even_fibonacci_numbers(1000))

