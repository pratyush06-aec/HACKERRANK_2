n= int(input())
for _  in range(n):
    a, b= input().split()
    try:
        a= int(a)
        b= int(b)
        print(a//b)

    except (ZeroDivisionError, ValueError) as e:
        print("Error Code: " , e)