# Hi, here's your problem today. This problem was recently asked by Apple:

# Given a sorted list of size n, with m unique elements (thus m < n), modify the list such that the first m unique elements in the list will be sorted, ignoring the rest of the list. Your solution should have a space complexity of O(1). Instead of returning the list (since you are just modifying the original list), you should return what m is.

def remove_dups(nums):   
  global removed_dups_nums
  removed_dups_nums = list(set(nums))
  return len(removed_dups_nums)
    

nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8

print(removed_dups_nums)
# [1, 2, 3, 4, 5, 6, 7, 9]



nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
# 1
print(removed_dups_nums)
# [1]
