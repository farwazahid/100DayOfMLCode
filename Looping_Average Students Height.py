
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height  += height
print(total_height)
no_of_students = len(student_heights)
average = round(total_height / no_of_students)
print(average)

  