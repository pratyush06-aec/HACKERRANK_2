n, a= map(int, input().split())
marks= []

for _ in range(a):
    marks.append(list(map(float, input().split())))

for student_marks in zip(*marks):
    print(sum(student_marks)/a)