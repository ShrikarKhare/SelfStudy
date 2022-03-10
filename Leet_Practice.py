# def twoSum(nums, target):
#         holder = {}
#         for key, value in enumerate(nums):
#             complement = target - value
#             if complement in holder:
#                 return [holder[complement] , key]
#             else:
#                 holder[value] = key
#         return []

# print(twoSum([2,7,11,15],9))

#Linked list

# count the number of nodes in a linked list
# class Node :
#     def __init__(self, dataval = None):
#         self.data = dataval
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self, new_data): # inserting a new node at the beginning of linked list
#         new_node = Node(new_data)

#         new_node.next = self.head
#         self.head = new_node
#     def getCount(self): #counting total nodes 
#         #start at the head
#         temp = self.head
#         #initialize counter
#         count = 0 
#         #while temp is not null
#         while(temp):
#             #icnrement count and temp node
#             count+=1
#             temp = temp.next
#         return count

#     def reverseList(self):
#         prev = None 
#         while self.head:
#             temp = self.head.next
#             self.head.next = prev
#             prev = self.head
#             self.head = temp
#         return prev
        
# list = LinkedList()
# list.push(2)
# list.push(22)
# list.push(3)
# list.push("Lol")
# list.push(True)
# list.push("Hello")
# list.push(122)
# list.push(1)

# print('Count of nodes is ' + str(list.getCount()))

def ValidPalindrome(s):
    left = 0
    right = len(s)-1

    while left <= right:
        if s[left] != s[right]:
            str1 = s[:left] + s[left+1:]
            str2 = s[:right] + s[right+1:]
            return str1 == str1[::-1] or str2 == str2[::-1]
        left+=1
        right-=1
    return True 

def ValPal(s):
    for i in range(len(s)):
        print(i)
        if s[:i] + s[i+1:] == s[:i-1] + s[i:0] :
            return True
    return False
# print(ValidPalindrome('abba'))
# print(ValidPalindrome('abeqwdsadcba'))
# print(ValidPalindrome('abwqba'))
print(ValPal('abcde'))
# print(ValPal('abba'))
# print(ValPal('abeqwdsadcba'))
# print(ValPal('abwqba'))