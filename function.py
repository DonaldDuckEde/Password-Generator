import random
import string

def generatepassword(length, upper, digits):
    pw = ""
    for i in range(length):
        pw += random.choice(string.ascii_letters + string.digits)
    return pw
