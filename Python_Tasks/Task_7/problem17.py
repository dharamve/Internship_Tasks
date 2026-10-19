# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = s[:length]
        if first.startswith("0"):
            continue

        current = int(first)
        built = ""
        while len(built) < len(s):
            built += str(current)
            current += 1
        if built == s:
            return f"YES {first}"

    return "NO"


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(separateNumbers(input().strip()))
