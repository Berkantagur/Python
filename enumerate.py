# Enumerate: The enumerate function in Python converts a data collection object into an enumerate object.
students = ["Berkant", "Aydora", "Ali Fuat", "Selminaz", "Özgür", "İlayda", "Alperen", "Birce"]

Women = []
Men = []

for index, student in enumerate(students, 1):

    if index % 2 == 0:
        Women.append(student)
    else:
        Men.append(student)

print(Women)
print(Men)