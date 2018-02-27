"""
Create a function that takes an integer as an argument and
returns "Even" for even numbers or "Odd" for odd numbers.

---

The use of conditionals is needed in order to solve this

Small explanation on conditionals
http://www.openbookproject.net/books/bpp4awd/ch04.html

Link to codewars exercise
http://www.codewars.com/kata/even-or-odd
"""


def even_or_odd(number):
    # your solution here
    pass


# Test methods below
assert even_or_odd(2) == "Even", "Did not return 'Even' for even number"
assert even_or_odd(0) == "Even", "Did not return 'Even' for even number"
assert even_or_odd(7) == "Odd", "Did not return 'Odd' for odd number"
assert even_or_odd(1) == "Odd", "Did not return 'Odd' for odd number"
assert even_or_odd(-3) == "Odd", "Did not return 'Odd' for odd number"
