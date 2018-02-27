"""
The goal of this kata is to write a function that takes two inputs:
a string and a character.

The function will count the number of times that character appears
in the string.

The count is case insensitive.

For example:

count_char("fizzbuzz","z") => 4
count_char("Fancy fifth fly aloof","f") => 5

The character can be any alphanumeric character.

---
A loop should iterate through the string, counting the occurrences

Careful with the case insensitive thingy

Link to codewars exercise
https://www.codewars.com/kata/count-the-characters
"""


def count_char(string, character):
    # your solution here
    pass


# Test methods below
assert count_char("Hello there", "e") == 3, "Incorrect count"
assert count_char("Hello there", "t") == 1, "Incorrect count"
assert count_char("Hello there", "h") == 2, "Incorrect count"
assert count_char("Hello there", "L") == 2, "Incorrect count"
assert count_char("Hello there", " ") == 1, "Incorrect count"
