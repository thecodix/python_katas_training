"""
Write a function called repeat_str which repeats
the given string string exactly n times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

---
We have two parameters and we need to combine them to
produce the expected result

Link to codewars exercise
http://www.codewars.com/kata/string-repeat
"""


def repeat_str(repeat, string):
    # your solution here
    pass


# Test methods below
assert repeat_str(6, 'I') == 'IIIIII'
assert repeat_str(5, 'Hello') == 'HelloHelloHelloHelloHello'
assert repeat_str(4, 'a') == 'aaaa'
assert repeat_str(3, 'hello ') == 'hello hello hello '
assert repeat_str(2, 'abc') == 'abcabc'
