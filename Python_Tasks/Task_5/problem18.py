# Problem 18: The Minion Game
# HackerRank Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    kevin = 0
    stuart = 0

    for i in range(len(s)):
        if s[i] in "AEIOU":
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
