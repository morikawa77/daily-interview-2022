# Hi, here's your problem today. This problem was recently asked by Apple:

# Given a number n, generate all possible combinations of n well-formed brackets.

def generate_brackets(n: int) -> set:
    combinations = set()
    if n == 1:
        combinations.add('()')
    else:
        previous_sets = generate_brackets(n - 1)
        for previous_set in previous_sets:
            for i, c in enumerate(previous_set):
                temp_string = "{}(){}".format(previous_set[:i+1], previous_set[i+1:])
                combinations.add(temp_string)

    return combinations
  
print(generate_brackets(1))
# ['()']

print(generate_brackets(3))
# ['((()))', '(()())', '()(())', '()()()', '(())()']