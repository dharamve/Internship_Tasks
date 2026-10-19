# Problem 8: Gemstones
# HackerRank: https://www.hackerrank.com/challenges/gem-stones/problem

n = int(input())
common = set(input().strip())

for _ in range(n - 1):
    common.intersection_update(set(input().strip()))

print(len(common))
