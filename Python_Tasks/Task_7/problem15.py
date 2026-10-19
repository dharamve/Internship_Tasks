# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter


def gameOfThrones(s):
    odd_counts = sum(count % 2 for count in Counter(s).values())
    return "YES" if odd_counts <= 1 else "NO"


if __name__ == "__main__":
    print(gameOfThrones(input().strip()))
