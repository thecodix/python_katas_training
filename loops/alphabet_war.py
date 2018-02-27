"""
Introduction

There is a war and nobody knows - the alphabet war!

There are two groups of hostile letters.
The tension between left side letters and right side letters was
too high and the war began.

Task

Write a function that accepts fight string consists of only
small letters and return who wins the fight.

When the left side wins return Left side wins!, when the right side
wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1

The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1

The other letters don't have power and are only victims.

Example

alphabet_war("z");        //=> Right side wins!
alphabet_war("zdqmwpbs"); //=> Let's fight again!
alphabet_War("zzzzs");    //=> Right side wins!
alphabet_war("wwwwwwz");  //=> Left side wins!

---

The idea here is to make a loop, and count the number of
left side or right side letter on each iteration

Link to codewars exercise
https://www.codewars.com/kata/alphabet-war
"""


def alphabet_war(fight):
    # your solution here
    pass


# Test methods below
assert alphabet_war("z") == "Right side wins!", "Right side should win here!"
assert alphabet_war("zdqmwpbs") == "Let's fight again!", "Same amount of right and left!"
assert alphabet_war("wq") == "Left side wins!", "Left side should win here!"
assert alphabet_war("zzzzs") == "Right side wins!", "Right side should win here!"
assert alphabet_war("wwwwww") == "Left side wins!", "Left side should win here!"
