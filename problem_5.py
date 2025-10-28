
n= int(input("Enter the range: "))
student_marks= []

for _ in range(n):
    name= str(input("Enter the name: "))
    score= float(input("Enter the score of the student: "))
    student_marks.append([name, score])

scores= sorted(set([s[1] for s in student_marks]))
second_lowest= scores[1]

names= sorted([s[0] for s in student_marks if(s[1]== second_lowest)])

for name in names:
    print(name)