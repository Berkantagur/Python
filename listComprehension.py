# Comprehension: Comprehensions in Python are used to generate new sequences based on existing sequences. 
# In Python, we have comprehensions for lists, dictionaries, sets and generators. 
# The type of the existing (original) sequence and new sequence need not be the same.

#Exp1:
salaries = [8500, 11300, 9250, 7600, 8100, 10900]

def new_salary(x):
    return x * 20 / 100 + x

null_list = []

"""
for salary in salaries:

    if salary >= 8500:
        null_list.append(int(new_salary(salary)))

    else:
        null_list.append(int(new_salary(salary * 1.3)))

print(null_list)
"""

[salary * 1.3 for salary in salaries if salary < 8500]
[null_list.append(int(new_salary(salary * 1.3))) if salary < 8500 else null_list.append(int(new_salary(salary))) for salary in salaries]
print(null_list)


#Exp2:
students = ["Berkant", "Şeyda", "Gaffar Cuma", "Arzu", "Yiğit", "Ahmet Kürşat"]
unwanted_student = ["Berkant", "Şeyda", "Yiğit"]

print([student.lower() if student in unwanted_student else student.upper() for student in students])
