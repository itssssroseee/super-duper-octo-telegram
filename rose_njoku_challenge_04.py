def game():
    counter = 0
    print("Great. Let me think of one. ")
    while (counter < 5):
        question = input("What can you hold in your right hand, but never in your left hand? ")
        if (question == "your left hand"):
                print("correct!")
                counter += 1
                print(counter)   #counter = counter + 1
        else:
                print("incorrect")
                print (counter)
                break

        # Code for question 2
        question_two = input("What gets wet while drying? ")
        if (question_two.lower() == "a towel"):
                print("correct!")
                counter += 1
                print(counter)
        else:
                print("incorrect")
                print(counter)
                break

        # Question 3
        question_three = input("What kind of band never plays music? ")
        if (question_three.lower() == "a rubber band"): 
                print("correct!")
                counter += 1
                print (counter) #counter = counter + 1
        else:
                print("incorrect")
                print (counter)
                break

        # Question 4
        question_four = input("What is the end of everything? ")
        if (question_four.lower() == "g"): 
                print("correct!")
                counter += 1
                print (counter) #counter = counter + 1
        else:
                print("incorrect")
                print (counter)
                break

        # Question 5
        question_five = input("When is a door no longer a door? ")
        if (question_five.lower() == "when it is ajar"): 
                print("correct!")
                counter += 1
                print (counter) #counter = counter + 1
        else:
                print("incorrect")
                print (counter)
                break
        
    if counter == 5:
        print("Congratulations, you escaped the room of many riddles.")
    else:
        print("Unfortunately, you did not escape the room of many riddles.")
        print("You only answered {0} riddles correctly".format(counter))
        user_choice = input("Would you like to try again?")
        if(user_choice.lower() == "yes" or user_choice.lower() == "y"):
            game()

user_choice = input("Would you like to attempt an escape? ")
if(user_choice.lower() == "yes" or user_choice.lower() == "y"):
    game()
else:
    print("Goodbye")