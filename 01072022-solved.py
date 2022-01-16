# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a list of numbers, and a target number n, find all unique combinations of a, b, c, d, such that a + b + c + d = n.

from itertools import combinations

def fourSum(nums, target):
    
    nums.sort()
    
    def valid(val):
        return sum(val) == target

    # combinations list with elementos who sum is target - 4 is for quadruple
    combinations_list = list(set(list(filter(valid, list(combinations(nums, 4))))))

    # convert list of tuples to list of lists
    result = [list(i) for i in combinations_list]
          
    return result



print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])


