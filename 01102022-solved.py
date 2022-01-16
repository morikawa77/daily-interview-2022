# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a list of numbers and a target number, find all possible unique subsets of the list of numbers that sum up to the target number. The numbers will all be positive numbers.

from itertools import combinations

def sum_combinations(nums, target):

  nums.sort()

  combinations_list = []

  def valid(val):
        return sum(val) == target

  for i in range(1, len(nums) + 1):
    size = i
    combinations_list.append(list(filter(valid, list(combinations(nums, size)))))

  # convert list of lists to a flat list
  combinations_list = [item for sublist in combinations_list for item in sublist]

  return list(set(combinations_list))


print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]