n= int(input("Enter the range: "))
integer_list= map(int, input().split())
t= tuple(integer_list)
print(hash(t))