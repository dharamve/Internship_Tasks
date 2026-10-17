# Problem 17: No Idea!
# HackerRank Link: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = sum((x in A) - (x in B) for x in arr)
print(happiness)
