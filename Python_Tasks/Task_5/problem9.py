# Problem 9: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
word_counts = {}

for _ in range(n):
    word = input().strip()
    word_counts[word] = word_counts.get(word, 0) + 1

print(len(word_counts))
print(*word_counts.values())
