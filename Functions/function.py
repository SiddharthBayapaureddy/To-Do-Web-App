# Defining commonly repeated functions

# For making a default parameter, just mention it in the argument of the function
# Non-default parameters should be placed before the default ones 

def get_todos(filepath='todos.txt'):
    '''
    Reads the text file, if mentioned in the arguement, or takes the todos.txt as the default parameter and returns the list 
    '''
    with open(filepath, 'r') as files:
        to_dos = files.readlines()    
    return to_dos

# This is although correct, it would be easier to have a default parameter (which should be placed second)
#def write_todos(filepath , list_arg):
 #   with open(filepath , 'w') as files:
  #      files.writelines(list_arg)

def write_todos(list_arg , filepath='todos.txt'):
    '''
    Modifies the text file, by overwriting it with the new list arguement mentioned. And the default text file is todos.txt
    '''
    with open(filepath , 'w') as files:
        files.writelines(list_arg)


# If the __name__ is run directly on the actual file, it'll show '__main__'. But if it's run on a different file,
# it'll show the name of the file it's been imported from. In this case, i.e., functions
if __name__ == '__main__':
    print('This is the Functions Page')

