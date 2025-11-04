from itertools import product

list_1= list(map(int, input().split()))
list_2= list(map(int, input().split()))

result= list(product(list_1, list_2))

for i in result:
    print(i, end=" ")