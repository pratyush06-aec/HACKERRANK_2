a= set(map(int, input().split()))

n= int(input())

strict_check= True

for _ in range(n):
    other= set(map(int, input().split()))
    if(not(a>other)):
        strict_check= False
        break

print(strict_check)