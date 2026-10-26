def print_rangoli(size):
    # your code goes here
    import string
    a = string.ascii_lowercase

    for i in range(size):
        s = '-'.join(a[size-1:size-i-1:-1] + a[size-i-1:size])
        print(s.center(4*size-3, '-'))

    for i in range(size-2, -1, -1):
        s = '-'.join(a[size-1:size-i-1:-1] + a[size-i-1:size])
        print(s.center(4*size-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
