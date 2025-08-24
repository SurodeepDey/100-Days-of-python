import sys

def bandname_generator():
    try:
        print("Welcome to the band name generator.")
        city = input('Which city did you grew up in? \n')
        pet = input('What is the name of your pet? \n')
        print("Your band name could be: " +city +" "+ pet)
        sys.exit(1)
    except Exception as e:
        print("Error: an error occured while execution of the program", str(e))
        sys.exit(0)

#return of the function
bandname_generator()