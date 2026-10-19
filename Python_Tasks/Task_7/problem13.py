# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter


def isValid(s):
    frequencies = Counter(Counter(s).values())
    if len(frequencies) == 1:
        return "YES"
    if len(frequencies) != 2:
        return "NO"

    (freq1, count1), (freq2, count2) = frequencies.items()

    # One character occurs once and can be removed.
    if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
        return "YES"

    # One character occurs exactly one time more than all others.
    if freq1 == freq2 + 1 and count1 == 1:
        return "YES"
    if freq2 == freq1 + 1 and count2 == 1:
        return "YES"

    return "NO"


if __name__ == "__main__":
    print(isValid(input().strip()))
