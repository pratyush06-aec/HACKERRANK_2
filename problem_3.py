x= int(input("Enter the number: "))
y= int(input("Enter the number: "))
z= int(input("Enter the number: "))
n= int(input("Enter the number: "))

coordinates= [[i, j, k]
              for i in range(x+ 1)
              for j in range(y+ 1)
              for k in range(z+ 1)
              if (i+j+k)!= n]

print(coordinates)