from itertools import product

lists= []
n, m= map(int, input().split())

for _ in range(n):
    num= list(map(int, input().split()))
    lists.append(num[1:])

max_value= 0

for i in product(*lists):
    s= sum(x**2 for x in i)%m
    total= max(max_value, s)

print(total)