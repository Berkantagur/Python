def exchange_with_enumerate (string):
    new_string = ""

    for i, letter in enumerate(string):

#If the index is even, capitalize it.
        if i % 2 == 0:
            new_string += letter.upper()
        
#If the index is odd, lowercase it.
        else:
            new_string += letter.lower()
            
    print(new_string)

exchange_with_enumerate("hi i am berkant and i am learning python programming language")