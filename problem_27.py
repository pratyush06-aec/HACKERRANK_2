import itertools

s, k= input().split()
k= int(k)

for i in range(1, k+1):
    for combo in itertools.combinations(sorted(s), i):
        print("".join(combo))