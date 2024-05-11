# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
    print("Hello!")

hello()

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

print(pack(1, 2, 3))

# A function called eat_lunch(). This function should accept a list of any length, 
# and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". The function should not return anything.

def eat_lunch(list):
    if len(list) != 0:
        for index, item in enumerate(list):
            if index == 0:
                print(f'First I eat {item}')
            else:
                print(f'Next I eat {item}')
    else:
        print('My lunchbox is empty!')

eat_lunch(['Curry', 'Salad', 'Popcorn'])
# eat_lunch([]) // to test empty list