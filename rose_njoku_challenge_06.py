import random 

def getUserNumber():
    try:
        user_number = int(input("How many numbers do you want to write: "))
        return user_number
    except ValueError:
        print("Please enter an integer")
        user_number = getUserNumber()
        return user_number

user_number = getUserNumber()

randomString = ""

i = 0
# This will output the random str
while i < user_number:

    randomInteger = random.randint(1,500)

    randomString += str(randomInteger) + " "

    i += 1

file = open('D:\StudentTestCodeFiles\random_numbers.txt', 'w')
file.write(randomString)
file.close()
    