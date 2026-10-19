# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ""
    run_length = 0

    for char in s:
        if char == previous:
            run_length += 1
        else:
            previous = char
            run_length = 1
        weights.add((ord(char) - ord("a") + 1) * run_length)

    return ["Yes" if query in weights else "No" for query in queries]


if __name__ == "__main__":
    s = input().strip()
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    print("\n".join(weightedUniformStrings(s, queries)))
