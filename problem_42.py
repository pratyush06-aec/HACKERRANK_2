n, m= map(int, input().split())

group_a= []
for _ in range(n):
    group_a.append(input().strip())

for _ in range(m):
    words= input().strip()
    indices= []
    for i in range(n):
        if group_a[i]== words:
            indices.append(words)

    if indices:
        print(*indices)

    else:
        print("-1")