import sys

odd, even = [], []
for i in range(7):
    num = int(sys.stdin.readline())
    if (num % 2 == 1):
        odd.append(num)
    else:
        even.append(num)
if (odd == []):
    print(-1)
elif (len(odd) >= 1):
    print(sum(odd))
    print(min(odd))