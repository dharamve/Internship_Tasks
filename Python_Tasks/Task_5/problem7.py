# Problem 7: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))

for number in sorted(set_a.symmetric_difference(set_b)):
    print(number)
