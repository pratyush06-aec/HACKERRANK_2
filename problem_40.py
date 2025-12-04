a= int(input())
num_1= set(map(int, input().split()))

n= int(input())
num_2= set(map(int, input().split()))

sym_diff= num_1.symmetric_difference(num_2)
print(len(sym_diff))