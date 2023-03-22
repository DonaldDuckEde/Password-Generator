import random
import string

print("Password Generator")

def generatePassword(upper, length):
    if length > 128:
        try:
            askSure = input("Are you sure you want to generate a password with more than 128 characters? ")
        except ValueError: 
            print("Please enter a valid input.") 
              
        if askSure.lower() == "yes":
            print("Generating Password...")
            for i in range(length):
                password = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
                print(password, end = "")
        else:
            print("shutting down...")        
    else:
        print("Generating Password...")
        for i in range(length):
            password = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            print(password, end = "")
    
    
def getPassInfo():
    try:
        passLen = int(input("How many characters would you like in your password? "))
        useChar = input("Would you like to use uppercase letters? ").lower()
    except ValueError:
        print("Please enter a valid input.")
        
    if useChar == "yes":
        useUpper = True
    else:
        useUpper = False
    try:        
        generatePassword(useUpper ,passLen)
    except:
        print("Something went wrong. Please try again.")    
    
try:
    getPassInfo()
except ValueError:
    print("Please enter a valid input.")
except:
    print("Something went wrong, please try again.")