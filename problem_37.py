n= int(input())
num_1= set(map(int, input().split()))

a= int(input())
num_2= set(map(int, input().split()))

total= num_1.intersection(num_2)
print(len(total))