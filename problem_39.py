a= int(input())
num_1= set(map(int, input().split()))

n= int(input())
num_2= set(map(int, input().split()))

diff= num_1.difference(num_2)
print(len(diff))