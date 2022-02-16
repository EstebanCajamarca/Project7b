# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/15/2022

# Write a function named reverse_list that takes as a parameter a list and reverses the order of the elements in that
# list. It should not return anything - it should mutate the original list. This can be done trivially using slices,
# but your function must not use any slicing.

def reverse_list(vals):
    """Takes a list as a parameter and reverses it."""
    vals = vals.reverse()  # reversing list.


"""Testing
vals = [7, -3, 12, 9]
reverse_list(vals)
print(vals)  # This should print [9, 12, -3, 7]"""
