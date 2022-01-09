# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a list of numbers, and a target number n, find all unique combinations of a, b, c, d, such that a + b + c + d = n.


def fourSum(nums, target, partial=[]):
    nums.sort(reverse = False)

    sum = 0
    counter = 0

    if sum > target:
        return partial

    for i in range(counter, len(nums), 1):
 
        # Check if the sum exceeds K
        if (sum + nums[i] > target):
            continue
 
        # Check if it is repeated or not
        if (i > counter and nums[i] == nums[i - 1]):
            continue
 
        # Take the element into the combination
        partial.append(nums[i])
 
        # Recursive call
        fourSum(nums[i+1], sum + nums[i], partial)
 
        # Remove element from the combination
        partial.remove(partial[len(partial) - 1])



print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])