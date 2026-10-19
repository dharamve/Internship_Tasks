# Problem 6: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    return "pangram" if set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz") else "not pangram"


if __name__ == "__main__":
    print(pangrams(input().rstrip("\n")))
