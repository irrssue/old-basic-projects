student_heights = input("input the list of student heighs: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


total_height = 0
for height in student_heights:
    total_height += height

total_students = 0
for students in student_heights:
    total_students += 1

final = total_height / total_students
print(f"The average height of students is {round(final)}")
