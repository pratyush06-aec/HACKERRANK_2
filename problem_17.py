from collections import Counter

number_of_shoes= int(input())
sizes= Counter(map(list(int, input().split())))
number_of_customers= int(input())
total_earning= 0

for _ in range(number_of_customers):
    size, price= map(int, input().split())
    if(sizes[size]>0):
        total_earning+= price
        sizes[size]-= 1

print(total_earning)
