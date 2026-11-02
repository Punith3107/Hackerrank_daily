from collections import Counter
n=int(input())
c=Counter(map(int,input().split()))
s=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    if c[a]: s+=b; c[a]-=1
print(s)
