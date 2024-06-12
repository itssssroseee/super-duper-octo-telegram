import re

def password(user_pass):
    if len(user_pass) < 8:
        print ("Invalid...must be 8 characters long")
        return False
    else:
        if not re.search(r'[a-zA-Z]', user_pass) or not re.search(r'\d', user_pass):
            return False
            
        if not re.search(r'[a-z]', user_pass) or not re.search(r'[A-Z]', user_pass):
            return False

        if not re.search(r'[@#$%*!]' , user_pass):
            return False

    return True


def main():
    user_pass = input("Please enter a password")

    if password(user_pass):
        print("Password is Good!")
    else:
        print("Passowrd does not work: ")


if __name__ == "__main__": 
    main()