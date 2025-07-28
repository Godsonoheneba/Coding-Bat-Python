# Exercise 3

# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True


def cat_dog(str):
  count_cat = str.count('cat')
  count_dog = str.count('dog')
  return count_cat == count_dog

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
