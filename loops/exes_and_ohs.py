"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

---

In this exercise, loops are required again, and we have to take
into account two separate variables to count elements

Be careful to take into account uppercase and lowercase

Link to codewars exercise
http://www.codewars.com/kata/exes-and-ohs
"""


def xo(s):
    # your solution here
    pass


# Test methods below
assert xo('XO') is True
assert xo('xo0') is True
assert xo('xxxoo') is False
assert xo('oooxxxo') is False
assert xo('Lord Skrillex') is True



