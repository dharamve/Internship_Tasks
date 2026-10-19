# Problem 9: Beautiful Binary String
# HackerRank: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

def beautifulBinaryString(b):
    changes = 0
    i = 0
    while i <= len(b) - 3:
        if b[i:i + 3] == "010":
            changes += 1
            i += 3
        else:
            i += 1
    return changes


if __name__ == "__main__":
    n = int(input())
    b = input().strip()
    print(beautifulBinaryString(b))
