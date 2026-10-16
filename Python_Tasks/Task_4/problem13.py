# Problem: Symmetric Difference
# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
set_m = set(map(int, input().split()))

n = int(input())
set_n = set(map(int, input().split()))

for value in sorted(set_m.symmetric_difference(set_n)):
    print(value)
