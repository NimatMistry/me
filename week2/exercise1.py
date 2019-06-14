"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed hello! Let's get started

# I think this is list 
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think this will print each word on a seperate line 
for word in some_words:
    print(word) # It printed everyw word on a seperate line

# I think this will do the exact same thing as the one above 
for x in some_words:
    print(x) # It did the exact same thing 

# I think this tells the program to print 
print(some_words) # It Printed 

# I think this tells the program to print the string "some_words contains more than 3 words" if the list contains more than 3 things 
if len(some_words) > 3:
    print('some_words contains more than 3 words') # It printed 'some_words contains more than 3 words'

# I think this is creating a definition to to return information such as - system, nodem reslease, version, machine, and processor
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think this tell the function to print the information that the platform.uname function calls
    print(platform.uname())

# I think this call the ealier defined usefulFunction and therefor should print the information such as - system, nodem reslease, version, machine, and processor
usefulFunction() # It printed the information - system, nodem reslease, version, machine, and processor
