# Enumerate: The enumerate function in Python converts a data collection object into an enumerate object.
people = ["Ayşenur", "Ahmet Furkan", "Beyza E.", "Kaan", "Petek", "Berkant", "Beyza Biryol"]

def divide_people(people):
    groups = [[], []]

    for index, person in enumerate(people):

        if index % 2 == 0:
            groups[0].append(person)
            
        else:
            groups[1].append(person)
            
    print(groups)
    return groups

bb = divide_people(people)
print (bb[0])
print (bb[1])