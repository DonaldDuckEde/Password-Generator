from function import generatepassword

print("welcome to EasyPass")

def get_user_input():
    try:
        use_characters = int(input("How many character would you like? "))
        use_numbers = input("Can it has numbers? ")
        use_upper = input("Can it has uppercase letters? ")
    except ValueError():
        print("Please enter a valid input")
        get_user_input()
    
    