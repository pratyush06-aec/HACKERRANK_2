from collections import OrderedDict

n= int(input())
item= OrderedDict()

for _ in range(n):
    line= input().split()
    items= " ".join(line[:-1])
    price= int(line[-1])

    if items in item:
        item[items]+= price

    else:
        item[items]= price

for items, price in item.items():
    print(items, price)