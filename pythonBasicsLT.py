# Topic 1 - Assignment # 1 Code
# Programmer: Laura Terry
# Date 06/10/2019
# Version: 1


#
#           Program Description
#

"""  Write a program that will include comments and an example function for each of the following:
    User Input, Arithmetic's and Variables, If Statements, Nested If Statements, Loops, For and While,
    Strings, Tuples, Lists/Dictionaries and Files/Exceptions
"""

###                 User Input
print("User Input")

def users_name():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    full_name = first_name + " " + last_name                # Concatenating strings
    print("Hello ", full_name)                                              # Using print to display 

users_name()        # Calling function


###                 Arithmetic's and Variables
print("\nArithmetic's and Variables")

from math import sqrt                       # Importing the sqrt function from math (Global Variable) 

def calculate(num1, num2, num3):
    total = sqrt(num1 + num2) / num3            # total is a local variable
    return total                                                  # Using return instead of print 

calculated_values = calculate(num1 = 5, num2 = 6, num3 = 9)     # Passing parameters when the function is called
print(calculated_values)                                                                    # Allowing place to put the value


###                  If Statements
print("\nIf Statements")

def statement():
    x = 50              # local variables
    y = 25
    z = 0
    
    entered_num = int(input("Please enter a number: "))
    if entered_num < x and entered_num > y:                         # Comparing the users number entered to the variables x, y and z
        print("Your number is between ", y," and ", x)
    elif entered_num < x and entered_num < y:
        print("Your number is between ", z,  "and ", y)
    else:
        print("Your number is greater than ", x)

statement()


###                 "Nested" If Statements
print("\nNested If Statements")

def grade():
    checked_grade = float(input("Please enter a grade score: "))            # Asking user to enter score that will be checked in the nested statement
    if checked_grade >= 90:                                                                     # to determine the grade letter
        print("The score of ", checked_grade, "is an 'A'")
    else:
        if checked_grade >= 80:
            print("The score of",  checked_grade, "is a 'B'")
        else:
            if checked_grade >= 70:
                print("The score of", checked_grade, "is a 'C'")
            else:
                if checked_grade >= 60:
                    print("The score of", checked_grade, "is a 'D'")
                else:
                    print("The score of", checked_grade, "is a 'F'")

grade()
                       
###                     Loops For
print("\nFor Loops")

def pet():
    pets = ["Olive", "Cody", "Jesse"]           # List for looping through

    for a_pet in pets:              # Loops through the list
        print(a_pet)                    # Will print out the whole list of pet names
        
pet()


###                         Loops While
print("\nWhile Loops")

def checked_fruit():
    fruit_to_guess = "strawberry"                   # Variables
    user_input = " "
    
    print("Guess the fruit")
    
    while user_input != fruit_to_guess and user_input != "q":                   # Loop asks user to guess the fruit until they get it correct or 'q' to quit
        user_input = input("Please enter a fruit to check or q to quit: ")
    if user_input ==fruit_to_guess:
        print("Correct!  The fruit is strawberry")
    else:
        print("Goodbye")
    
checked_fruit()


###                       Strings
print("\nStrings")

def name(first_name, middle_name, last_name):                           # Concatenating three strings
    full_name = first_name + " " + middle_name + " " + last_name
    print(full_name)
    print(full_name.upper())
    print(len(first_name))                                          # Find the length of the first name string
    print(middle_name.replace('Turbo', 'super pug'))   # Replace the middle name with a new name

name(first_name = "Olive", middle_name = "Turbo", last_name = "Terry")  # Passing parameters



###                           Tuples            # Immutable.  Great for a collection of elements you do NOT want changed.
print("\nTuples")

def calendar():
        months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        days = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        print(months)
        print(days_of_week)
        print(days)
        todays_day_of_week = days_of_week[1]            # Choosing the index number for today's week day name, month and date
        todays_month = months[5]
        todays_day = days[9]
        print("\nToday is ",  todays_day_of_week, ", ",todays_month, " ", todays_day, "th")
        
calendar()

###                                 List/Dictionaries
print("\nList/Dictionaries")

def adding_pets():
    pets = [                                            # Creating a list that contains dictionaries
        {
            "count": 1,
            "name": "Olive",
            "age": 2,
            "type": "dog",
            "other info": "Pug",
            },
        {
            "count": 2,
            "name": "Cody",
            "age": 12,
            "type": "dog",
            "other info": "Boston Terrier",
            },
        {
            "count": 3,
            "name": "Cody Jr.",
            "age": 5,
            "type": "Fish",
            "other info": "Upside Down Catfish",
            },
        ]

    for each_pet in pets:                       # For loop to print each pet dictionary
        print(each_pet)

    find_pet = pets[0]                          # Finding a pet in the pets list in dictionary 0
    pet_name = find_pet["name"]     # Getting pets name from the dictionary with the key "name"
    print(pet_name)                             # Printing the pets name

    add_pet = len(pets)                     # Adding a new pet to the list of dictionaries

    new_name = input("Please enter your pets name: ")                       # Collecting users info on pet to add
    new_age = int(input("Please enter your pets age: "))
    new_type = input("Please enter your pet type.  For example dog, cat, fish: ")
    new_other_info = input("Please enter pet breed or other information: ")

    new_pet = {
        "count": add_pet,
        "name": new_name,
        "age": new_age,
        "type": new_type,
        "other info": new_other_info,
        }

    pets.append(new_pet)                    # Adds the new data to the list and creates a new dictionary
    print(new_pet)                                  # Prints the new pets data from the dictionary
    
adding_pets()

###                     Files/Exceptions
print("\nFiles/Exceptions")

def files():
    outFile = open('petNames.txt', 'w')             # Creating new file to write to
    
    outFile.write('The following are the names of my pets: ')       # Adding strings to file
    outFile.write('\nOlive ')
    outFile.write('\nCody & ')
    outFile.write('\nCody Jr. ')
    
    outFile.close()         # Closing the file

                                    # Opening the file
    print("Type the file name, petNames.txt, to open and print the contents.")          # Asking user to open file

    while True:                             # Checking for errors when the user opens the file
        try:
            fileName = open(input("Enter file name: "), 'r')
            print(fileName.readlines())
            print('Check your desktop to find the new file named petNames.txt.')
            print('Once open you should see the same list of names')
            fileName.close()
            break
        except IOError:                                                                                     # Exception error, when users types in wrong name of file 
            print("Error: File not found.")
        
files()



"""Write a function that prompts user for 5 integers and displays the minumum value,
maximum value and the average of entered values.
"""

###             Final Function
print("\nFinal Function")

def calculate_nums():
    print("The following program will take the 5 integers you enter and find the minimum, maximum and the average.\n")
    entered_nums = []      # Empty list for the user to add 5 integers
    for i in range(5):          # For Loop 
        user_input = int(input("Enter an integer: "))
        entered_nums.append(user_input)    # Adding the users integers to the list

    smallest = min(entered_nums)         # Calculating the min, max and average
    print("\nThe minimum value is: ", smallest)
    largest = max(entered_nums)
    print("The maximum value is: ", largest)
    total = sum(entered_nums)       # To calculate the the total to get the average below
    average = total/5
    print("The average of all the intergers is: ", average)

calculate_nums()


## Another way without a for loop

##def calculate_nums():
##    print("Please enter 5 integers\n")
##    num1 = int(input("Enter an integer: "))
##    num2 = int(input("Enter an integer: "))
##    num3 = int(input("Enter an integer: "))
##    num4 = int(input("Enter an integer: "))
##    num5 = int(input("Enter an integer: "))
##    
##    largest = max(num1, num2, num3, num4, num5)
##    smallest = min(num1, num2, num3, num4, num5)
##    total = num1 + num2 + num3 + num4 + num5
##    average = total/5
##
##    print("\nThanks! \n ")
##    print("The minimum value is: ", smallest)
##    print("The maximum value is: ", largest)
##    print("The average value is: ", average)
##
##
##calculate_nums()
##               
##

print("\nGoodbye")
