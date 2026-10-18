student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)

higest_number = 0
for score in student_scores:
    if score > higest_number:
        higest_number = score

print(f"the highest score is {higest_number}")
