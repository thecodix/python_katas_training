"""
Given an array of integers, remove the smallest value.
Do not mutate the original array/list.

If there are multiple elements with the same value,
remove the one with a lower index.

If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples

remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]

---

The problem has many small coditions to take into account

Be sure to test properly

Link to codewars exercise
https://www.codewars.com/kata/remove-the-minimum
"""


def remove_smallest(numbers):
    # your solution here
    pass


# Test methods below
assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]"
assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]"
assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]"
assert remove_smallest([]) == [], "Wrong result for []"
