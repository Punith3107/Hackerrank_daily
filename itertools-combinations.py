# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S, K = input().split()
K = int(K)
S = sorted(S)
for i in range(1, K + 1):
    for j in combinations(S, i):
        print(''.join(j))
