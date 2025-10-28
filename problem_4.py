n= int(input("Enter the range: "))
student_marks= {}

for _ in range(n):
    names= str(input("Enter the name: ")).split()
    name= names[0]
    for _ in range(3):
        scores= float(input("Enter all the marks: "))
        scores= list(map(float, names[1:]))
        student_marks[name]= scores

query_name= str(input("Enter the name, whose avg. of marks you want to see: "))

scores= student_marks[query_name]
average= sum(scores)/3
print(f"{average:.2f}")