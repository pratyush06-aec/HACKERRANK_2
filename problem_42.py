from collections import defaultdict

positions= defaultdict(list)
n, m= map(int, input().split())

for i in range(1, n+1):
    words= input().strip()
    positions[words].append(i)

for _ in range(m):
    words= input().strip()
    if positions[words]:
        print(*positions[words])

    else:
        print(-1)