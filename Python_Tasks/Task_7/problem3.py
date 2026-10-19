# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    return sum(a != b for a, b in zip(s, expected))


if __name__ == "__main__":
    s = input().strip()
    print(marsExploration(s))
