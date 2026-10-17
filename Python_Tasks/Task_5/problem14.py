# Problem 14: Finding the Percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}

for _ in range(n):
    data = input().split()
    student_marks[data[0]] = list(map(float, data[1:]))

name = input()
marks = student_marks[name]
print(f"{sum(marks) / len(marks):.2f}")
