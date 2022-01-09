# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a list of strings, find the longest common prefix between all strings.

def longest_common_prefix(strs):
  strs.sort()
  result = ""
  # Compare the first and the last string character
  # by character.
  for i in range(len(strs[0])):
      #  If the characters match, append the character to
      #  the result.
      if strs[0][i] == strs[-1][i]:
          result += strs[0][i]
      # Else, stop the comparison
      else:
          break
  return result
  
print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''