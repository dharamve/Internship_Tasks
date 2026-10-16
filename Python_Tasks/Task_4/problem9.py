# Problem: Mutations
# Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == "__main__":
    string = input()
    position, character = input().split()
    result = mutate_string(string, int(position), character)
    print(result)
