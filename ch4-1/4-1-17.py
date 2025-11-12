n = int(input())
tutors = sorted([int(x) for x in input().split()])
students = sorted([int(x) for x in input().split()])

total = 0
for i in range(n):
    most_skilled_tutor = tutors[-1-i]
    least_skilled_student = students[i]
    total += most_skilled_tutor - least_skilled_student
print(total)