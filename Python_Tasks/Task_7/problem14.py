# Problem 14: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter


def anagram(s):
    if len(s) % 2:
        return -1
    half = len(s) // 2
    first = Counter(s[:half])
    second = Counter(s[half:])
    return sum((first - second).values())


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(anagram(input().strip()))
