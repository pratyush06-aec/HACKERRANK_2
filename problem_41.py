from math import comb

a= int(input())
letters= input().split()
n= int(input())

total_combinations= comb(a, n)
count_a= letters.count('a')

if(a-count_a>=n):
    occurance_a= comb(a-count_a, n)

else:
    0

probability= 1-(occurance_a/total_combinations)
print(f"{probability:.3f}")