# Problem 16: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    k %= 26
    result = []
    for char in s:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + k) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + k) % 26 + ord("A")))
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    n = int(input())
    s = input().rstrip("\n")
    k = int(input())
    print(caesarCipher(s, k))
