Grades = list()

for i in range(10):
    add = int(input("Enter grade:"))
    Grades.append(add)

Grades.sort(reverse=True)
print("\nGrade list:",Grades)