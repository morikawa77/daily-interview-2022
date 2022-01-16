# Hi, here's your problem today. This problem was recently asked by Google:

# Given an integer, find the number of 1 bits it has.


def one_bits(num):
  return bin(num).count('1')

print(one_bits(23))
# 4
# 23 = 0b10111