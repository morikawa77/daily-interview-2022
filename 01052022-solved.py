# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given an integer, convert the integer to a roman numeral. You can assume the input will be between 1 to 3999.

# The rules for roman numerals are as following:

# There are 7 symbols, which correspond to the following values.
# I   1
# V   5
# X   10
# L   50
# C   100
# D   500
# M   1000
# The value of a roman numeral are the digits added together. For example the roman numeral 'XX' is V + V = 10 + 10 = 20. Typically the digits are listed from largest to smallest, so X should always come before I. Thus the largest possible digits should be used first before the smaller digits (so to represent 50, instead of XXXXX, we should use L).

# There are a couple special exceptions to the above rule.

# To represent 4, we should use IV instead of IIII. Notice that I comes before V.
# To represent 9, we should use IX instead of VIIII.
# To represent 40, we should use XL instead of XXXX.
# To represent 90, we should use XC instead of LXXXX.
# To represent 400, we should use CD instead of CCCC.
# To represent 900, we should use CM instead of DCCCC.


def integer_to_roman(num):
    ints = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman_num = ''
      
    while num:
        div = num // ints[i]
        num %= ints[i]
  
        while div:
            roman_num += romans[i]
            div -= 1
        i -= 1
    
    return roman_num

print(integer_to_roman(1000))
# M
print(integer_to_roman(48))
# XLVIII
print(integer_to_roman(444))
# CDXLIV