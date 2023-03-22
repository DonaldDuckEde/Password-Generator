import random
import string

def generatePassword(length):
    pw = []
    for i in range(length):
        pw.append(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    
    for i in range(length):
        temp = length - i
        print(pw[temp])

generatePassword(10)