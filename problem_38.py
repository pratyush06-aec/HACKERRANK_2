a= int(input())
num_1= set(map(int, input().split()))

n= int(input())
num_2= set(map(int, input().split()))

total= num_1.union(num_2)
print(len(total))