# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

def reverse_integer(num):
    reverse_num = 0

    if num > 0:
      while num > 0:
          reverse_num = reverse_num * 10 + num % 10
          num //= 10
    
    elif num < 0:
      num *= -1
      while num > 0:
          reverse_num = reverse_num * 10 + num % 10
          num //= 10
      reverse_num *= -1

    return reverse_num

  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123