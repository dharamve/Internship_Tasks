# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]
        line = "-".join(left + right)
        lines.append(line.center(4 * size - 3, "-"))
    print("\n".join(lines + lines[-2::-1]))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
