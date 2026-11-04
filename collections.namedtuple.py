# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
S = namedtuple('S', input())
print(f"{sum(int(S(*input().split()).MARKS) for _ in range(n))/n:.2f}")
