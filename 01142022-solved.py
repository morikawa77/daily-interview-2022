# Hi, here's your problem today. This problem was recently asked by AirBNB:

# A majority element is an element that appears more than half the time. Given a list with a majority element, find the majority element.


def majority_element(nums):
  sources = set(nums)
  element = {}

  for source in sources:
    indices = [i for i, x in enumerate(nums) if x == source]
    element[source] = len(indices)

  return max(element, key=element.get)

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3