def solve(s):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split(' '))

if __name__ == '__main__':
    s = input()
    print(solve(s))
