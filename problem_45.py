a= int(input())
line_1= set(map(int, input().split()))

n= int(input())

for _ in range(n):
    operation, _= input().split()
    line_2= set(map(int, input().split()))

    if(operation== "intersection_update"):
        line_1.intersection_update(line_2)

    elif(operation== "update"):
        line_1.update(line_2)

    elif(operation=="symmetric_difference_update"):
        line_1.symmetric_difference_update(line_2)

    elif(operation== "difference_update"):
        line_1.difference_update(line_2)

print(sum(line_1))