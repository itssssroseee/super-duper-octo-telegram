#This is the alaphabet into mores code
letters = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.',
    'D': '-..', 
    'E': '.',
    'F': '. . _ .', 
    'G': '_ _ .',
    'H': '. . . .',
    'I': ' . .', 
    'J': '. _ _ _',
    'K': '_ . _',
    'L': '. _ . .',
    'M': '_ _',
    'N': '_.',
    'O': '_ _ _',
    'P': '. _ _ .',
    'Q': '_ _ . _',
    'R': '. _ .',
    'S': '. . .',
    'T': '_',
    'U': '. . _',
    'V': '. . . _',
    'W': '. _ _',
    'X': '_ . . _',
    'Y': '_ . _ _',
    'Z': '_ _ . .',
    ' ': '/',
    }

#This is the number in mores code
numbers = {
    '0':'-----',
    '1':'._',
    '2': '.._',
    '3': '. . . _',
    '4': '. . . . _',
    '5': '.',
    '6': '_ . . . .',
    '7': '_ . . .',
    '8': '_ . .',
    '9': '_ .',
}   
# This is special_characters i added this for bonus 
special_characters = {
    "?" :'. . _ _ . .',
    
}

#create a new empty list
list1 = [] 

#The function 
def letter_to_morse(user_input):
    for char in user_input: 
        if char.upper() in letters:
            a = letters[char.upper()]
            list1.append(a)
        elif char in numbers:
            a = numbers[char]
            list1.append(a)
        elif char in special_characters:
            a = special_characters[char]
            list1.append(a)
        else:
            print("The letter was not found in the string")
            break
    print(f'The word {user_input} is written in morse code as', list1)
    

#run the code from here           
list1 = [] 
user_input = input("Please enter a word?")
letter_to_morse(user_input)

