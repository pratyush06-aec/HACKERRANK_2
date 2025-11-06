def average(array):
    num= set(array)
    return sum(num)/len(num)

n= int(input())
arr= map(int, input().split())
print(average(arr))