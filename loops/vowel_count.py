"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

---

We are starting with exercises that require iteration through
the elements of a structure, so it will be good to dedicate
some time to learn how they work
https://www.learnpython.org/en/Loops

Link to codewars exercise
http://www.codewars.com/kata/vowel-count
"""


def get_count(input_str):
    num_vowels = 0
    # your code here

    return num_vowels


# Test methods below
assert get_count("magic") == 2, "Vowel count is not correct"
assert get_count("abracadabra") == 5, "Vowel count is not correct"
assert get_count("let's get lost") == 3, "Vowel count is not correct"
