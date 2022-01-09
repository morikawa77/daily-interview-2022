# Hi, here's your problem today. This problem was recently asked by Google:

# Given a list of numbers and a target number n, find 3 numbers in the list that sums closest to the target number n. There may be multiple ways of creating the sum closest to the target number, you can return any combination in any order.

import sys

def closest_3sum(nums, target):
    # Sort the array 
    nums.sort()
    
    # To store the closest sum
    closestSum = sys.maxsize

    # 3sum list
    sumList = [0, 0, 0]

    # Fix the smallest number among 
    # the three integers 
    for i in range(len(nums)-2): 

        # Two pointers initially pointing at 
        # the last and the element 
        # next to the fixed element 
        ptr1 = i + 1
        ptr2 = len(nums) - 1

        # While there could be more pairs to check 
        while (ptr1 < ptr2):

            # Calculate the sum of the current triplet 
            sum = nums[i] + nums[ptr1] + nums[ptr2]

            # If the sum is more closer than 
            # the current closest sum 
            if (abs(target - sum) < abs(target - closestSum)):
                closestSum = sum

                sumList[0] = nums[i]
                sumList[1] = nums[i+1]
                sumList[2] = nums[i+2] 

            # If sum is greater then x then decrement 
            # the second pointer to get a smaller sum 
            if (sum > target):
                ptr2 -= 1

            # Else increment the first pointer 
            # to get a larger sum 
            else :
                ptr1 += 1
                     

    # Return the sum list
    return sumList
    
  
print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]