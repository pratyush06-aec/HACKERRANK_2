m= int(input())
m= set(map(int, input().split()))

n= int(input())
n= set(map(int, input().split()))

diff= sorted(m.symmetric_difference(n))

for i in diff:
    print(i)