# Problem 18: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
a = set(map(int, input().split()))
operations = int(input())

for _ in range(operations):
    operation, length = input().split()
    other = set(map(int, input().split()))

    if operation == "intersection_update":
        a.intersection_update(other)
    elif operation == "update":
        a.update(other)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(other)
    elif operation == "difference_update":
        a.difference_update(other)

print(sum(a))
