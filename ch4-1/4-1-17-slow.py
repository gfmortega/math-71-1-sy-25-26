n = int(input())
tutors = [int(x) for x in input().split()]
students = [int(x) for x in input().split()]

total = 0
while len(tutors) == 0 or len(students) == 0:
    most_skilled_tutor = max(tutors)
    least_skill_student = min(students)

    total += most_skilled_tutor - least_skill_student
    tutors.remove(most_skilled_tutor)
    students.remove(least_skill_student)

print(total)