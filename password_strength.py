#author : Rudraksh Pathak
#This program checks for password strength 
import re
def passkey_strength(password):
    #required criterias for the password 
    min_len = 8 #NIST standard for the min leength
    upper_exist = re.search(r'[A-Z]', password)
    lower_exist = re.search(r'[a-z]', password)
    num_exist = re.search(r'\d', password)
    special_exist = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    if len(password) < 8:
        return "password is too short! must be atleast 8 digits long"
    if not upper_exist:
        return "include some uppercase letters."
    if not lower_exist:
        return "include some lowercase letters."
    if not num_exist:
        return "Include some digits"
    if not special_exist:
        return "include some special characters"


    return "Strong Password! O_o"

if __name__ == "__main__":
    password=input("enter your password: ")
    Strength = passkey_strength(password)
    print(Strength)
    


        
    
