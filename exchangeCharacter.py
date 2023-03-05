
def exchange (string):
    new_string = ""

#Navigating the indexes of the entered string
    for string_index in range(len(string)):

#If the index is even, capitalize it.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        
#If the index is odd, lowercase it.      
        else:
            new_string += string[string_index].lower()
    
    print(new_string)

exchange ("hi my name is berkant and i am learning python programming language")