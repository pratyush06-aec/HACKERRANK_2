n= int(input())

for i in range(1, n+1):
    left= "".join(str(x) for x in range(1, i+1))
    right= "".join(str(x) for x in range(i-1, 0, -1))
    print(left+right)
