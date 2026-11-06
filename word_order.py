# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}
for _ in range(n):
    w = input()
    d[w] = d.get(w, 0) + 1
print(len(d))
print(*d.values())
