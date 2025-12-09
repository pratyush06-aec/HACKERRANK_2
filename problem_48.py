t= int(input())

for _ in range(t):
    a= int(input())
    line_a= set(map(int, input().split()))
    b= int(input())
    line_b= set(map(int, input().split()))
    print(line_a.issubset(line_b))