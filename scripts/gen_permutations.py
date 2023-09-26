import itertools

# Define the input elements
elements = ["A", "O", "C", "S", "I"]

# Generate all permutations of the elements
permutations = itertools.permutations(elements)

# Initialize a list to store the formatted combinations
formatted_combinations = []

# Iterate through the permutations and format them as strings
for perm in permutations:
    formatted_combination = "[" + "] [".join(perm) + "]"
    formatted_combinations.append(formatted_combination)

# Print out the formatted combinations
for combination in formatted_combinations:
    print(combination)
