for _ in range(int(input())):
    n = int(input())
    a = set(input().split())
    m = int(input())
    b = set(input().split())
    print(a.issubset(b))
