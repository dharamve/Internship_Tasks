# Problem 19: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

s = input().strip()
counts = Counter(s)

for char, count in sorted(
    counts.items(),
    key=lambda item: (-item[1], item[0])
)[:3]:
    print(char, count)
