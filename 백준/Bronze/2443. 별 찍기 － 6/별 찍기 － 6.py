import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print(" " * (i - 1) + "*" * (2 * N - (2 * i - 1)))