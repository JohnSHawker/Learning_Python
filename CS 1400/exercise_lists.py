# """ Exercise 10.1 """
# def nested_sum(t):
#     total = 0
#     for nested in t:
#         total += sum(nested)
#     return total

# """Exercise 10.2 """
# def cumsum(t):
#     total = 0
#     res = []
#     for x in t:
#         total += x
#         res.append(total)
#     return res

# """Exercise 10.3 """
# def middle(t):
#     return t[1:-1]

# """Exercise 10.4 """
# def chop(t):
#     del t[0]
#     del t[-1]

# """Exercise 10.5 """
# def is_sorted(t):
#     return t ==sorted(t)

# """Exercise 10.6 """
# def is_anagram(word1, word2):
#     return sorted(word1) == sorted(word2)

# """Exercise 10.7 """
# def has_duplicates(s):
#     t = list(s)
#     t.sort()
#     for i in range(len(t)-1):
#         if t[i] == t[i+1]:
#             return True
#     return False

# """Exercise 10.8"""
# """This module contains a code example related to
# Think Python, 2nd Edition
# by Allen Downey
# http://thinkpython2.com
# Copyright 2015 Allen Downey
# License: http://creativecommons.org/licenses/by/4.0/
# """

from __future__ import print_function, division

import random


def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.
    t: list
    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.
    n: int
    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.
    num_students: how many students in the group
    num_samples: how many groups to simulate
    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()

"""Exercise 10.9"""

"""Exercise 10.11"""
