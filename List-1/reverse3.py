# Exercise 7
# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 5, 11]
# reverse3([7, 0, 0]) → [0, 0, 7]


def reverse3(nums):
  return nums[::-1]

print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))