def StoredPasswords(checkPass):
# This is 50 passwords in the tuple
    passwords = (
        "123456",
        "123456789",
        "12345",
        "qwerty",
        "password",
        "12345678",
        "111111",
        "123123",
        "1234567890",
        "1234567",
        "qwerty123", # index 10
        "000000",
        "1q2w3e",
        "aa12345678",
        "abc123",
        "password1",
        "1234",
        "qwertyuiop",
        "123321",
        "password123",
        "1q2w3e4r5t",
        "iloveyou",
        "654321",
        "666666",
        "987654321",
        "123",
        "123456a",
        "qwe123",
        "1q2w3e4r",
        "7777777",
        "1qaz2wsx",
        "123qwe",
        "zxcvbnm",
        "121212",
        "asdasd",
        "a123456",
        "555555",
        "dragon",
        "112233",
        "123123123",
        "monkey",
        "11111111",
        "qazwsx",
        "159753",
        "asdfghjkl",
        "222222",
        "1234qwer",
        "qwerty1",
        "123654",
        "123abc")
    
# IF you get a match, stop comparing the values  
    for password in passwords:
        if password == checkPass:
            found = "Your password is too common.  Please consider changing it."
            index = passwords.index(password)
            print("The password was found on index",index)
            return found
#IF no values match, then store the string: "You have a strong password." into a variable called notFound
    notFound = "You have a strong password."
    return notFound

#calling StoredPasswords(checkPass) from getUserPass().  
def getUserPass():
    userName = input("Please enter a username: ")
    userPass = input("Please enter a password: ")
    result = StoredPasswords(userPass)
    print(result)

def main():
    getUserPass()


if __name__=='__main__':
    main()