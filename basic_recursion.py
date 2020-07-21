'''
Example
'''

# def countdown_to_one(n):
#     if n == 0: # base case
#         return
#     countdown_to_one(n-1) # recursive call and moving towards a "base case"
#     print(n)

# countdown_to_one(5)


"""
Example
"""

# def countdown(n):
#     if n == 0:
#         return
#     countdown(n-1)
#     countdown(n-1)
#     print(n)

# countdown(3)

'''
Example
'''

# [1, 2, 3, 4, 5]
# def sum_list(items):
#     if len(items) == 1: # base case
#         return items[0]
#     else:
#         return items[0] + sum_list(items[1:]) # recursive case


'''
Example:  Recursive Factorial

            1 = fac(0)
            1 = fac(1) = 1 * fac(0) => n * fac(n-1)
        2 * 1 = fac(2) = 2 * fac(1) => n * fac(n-1)
    3 * 2 * 1 = fac(3) = 3 * fac(2) => n * fac(n-1)
4 * 3 * 2 * 1 = fac(4) = 4 * fac(3) => n * fac(n-1)
'''

# def recursive_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * recursive_factorial(n -1)

# recursive_factorial(5)

'''
Example: Recursive Count "st"

-Your function should take in a signle parameter (a string)
-Your function should return a count of how many occurences of ***"st"***
occur with the input string. Case matters.
-Your function must utilize recursion. It cannot contain any loops
'''

# def count_st(word):
#     pass
#     # base case
#     if len(word) < 2:
#         return 2
#     else:
#         # recursive case
#         if word[:2] == "st":
#             return 1 + count_st(word[2:])
#         else:
#             return count_st(word[1:])

# count_st("stepstool")


'''
Example: Out-of-place Quick Sort
'''
def partition(data):
    pivot = data[0]
    left = []
    right = []

    for current in data[1:]:
        if current <= pivot:
            left.append(current)
        else:
            right.append(current)

    return left, right, pivot


def quicksort(data):
    if len(data) <= 1:
        return data
    left, right, pivot = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([2,5,7,1,3,4,6,9,8]))



"""
Example: In-place Quicksort
"""

