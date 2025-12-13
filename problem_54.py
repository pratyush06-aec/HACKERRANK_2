cube= lambda n: n**3

def fibonacci(n):
    if(n==0):
        return []

    if(n==1):
        return [0]

    prev= fibonacci(n-1)
    if(len(prev)==1):
        prev.append(1)

    else:
        prev.append(prev[-1]+prev[-2])

    return prev

a= int(input())
print(list(map(cube, fibonacci(a))))