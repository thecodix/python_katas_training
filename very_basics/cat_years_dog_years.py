"""
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,cat_ears,dog_years]

NOTES:

    human_years >= 1

Cat Years

    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that

Dog Years

    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that


---

Link to codewars exercise
https://www.codewars.com/kata/cat-years-dog-years/train/python
"""


def human_years_cat_years_dog_years(human_years):
    # your solution here
    pass


# Test methods below
assert human_years_cat_years_dog_years(1) == [1, 15, 15], "Wrong result for 1"
assert human_years_cat_years_dog_years(2) == [2, 24, 24], "Wrong result for 2"
assert human_years_cat_years_dog_years(10) == [10, 56, 64], "Wrong result for 10"
