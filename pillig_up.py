# Enter your code here. Read input from STDIN. Print output to STDOUT

def pile_up(cubes):
    left = 0
    right = len(cubes) - 1
    last = float('inf')

    while left <= right:
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1

        if current > last:
            return "No"

        last = current

    return "Yes"


t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    print(pile_up(cubes))
