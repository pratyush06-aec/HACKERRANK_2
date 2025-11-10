a= int(input())
b= input()
marks_index= b.index('MARKS')

total= 0

for _ in range(a):
    row_index= input().split()
    total+= int(row_index[marks_index])

avg= (total)/a
print(f"{avg:.2f}")