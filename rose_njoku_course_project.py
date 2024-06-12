import random
print("Welcome to Falls of Eternity. This is a simple RPG simulator written in Python.")
class Humanoid():
    def __init__(self):
        self.__height = 0
        self.__weight = 0
        self.__hair_color = ""
        self.__eye_color = ""

        self.__strength = random.randint(1, 18)
        self.__dexterity = random.randint(1, 18)
        self.__constitution = random.randint(1, 18)
        self.__intelligence = random.randint(1, 18)
        self.__wisdom = random.randint(1, 18)
        self.__charisma = random.randint(1, 18)

        self.__sleep_resist = 0
        self.__magic_resist = 0

    def height(self):
        return self.__height

    def weight(self):
        return self.__weight

    def hair_color(self):
        return self.__hair_color

    def eye_color(self):
        return self.__eye_color

    def strength(self):
        return self.__strength

    def dexterity(self):
        return self.__dexterity

    def constitution(self):
        return self.__constitution

    def intelligence(self):
        return self.__intelligence

    def wisdom(self):
        return self.__wisdom

    def charisma(self):
        return self.__charisma

    def sleep_resistance(self):
        return self.__sleep_resist

    def magic_resistance(self):
        return self.__magic_resist

    def __str__(self):
        my_string = (f"Height: {self.__height}ft\n" +
                     f"Weight: {self.__weight} lbs\n" +
                     f"Hair Color: {self.__hair_color}\n" +
                     f"Eye Color: {self.__eye_color}\n" +
                     f"Str: {self.__strength}\n" +
                     f"Dex: {self.__dexterity}\n" +
                     f"Con: {self.__constitution}\n" +
                     f"Int: {self.__intelligence}\n" +
                     f"Wis: {self.__wisdom}\n" +
                     f"Char: {self.__charisma}\n")

        return my_string

    def set_height(self, height):
        if 3 <= height <= 7:
            self.__height = height
            return True
        return False

    def set_weight(self, weight):
        if 60 <= weight <= 300:
            self.__weight = weight
            return True
        return False

    def set_hair_color(self, hair_color, valid_colors):
        if hair_color in valid_colors:
            self.__hair_color = hair_color
            return True
        return False

    def set_eye_color(self, eye_color, valid_colors):
        if eye_color in valid_colors:
            self.__eye_color = eye_color
            return True
        return False

    def set_strength(self, strength):
        self.__strength = strength

    def set_dexterity(self, dexterity):
        self.__dexterity = dexterity

    def set_constitution(self, constitution):
        self.__constitution = constitution

    def set_intelligence(self, intelligence):
        self.__intelligence = intelligence

    def set_wisdom(self, wisdom):
        self.__wisdom = wisdom

    def set_charisma(self, charisma):
        self.__charisma = charisma


class Elf(Humanoid):
    def __init__(self):
        super().__init__()
        self.__sleep_res = 100
        self.set_dexterity(self.dexterity() + 2)
        self.set_charisma(self.charisma() + 2)

    def __str__(self):
        my_string = ("Race: Elf\n" +
                     super(Elf, self).__str__() +
                     f"sleep_resist:{self.__sleep_res}\n")
        return my_string


class Dwarf(Humanoid):
    def __init__(self):
        super().__init__()
        self.__magic_res = 20
        self.set_strength(self.strength() + 2)
        self.set_constitution(self.constitution() + 2)
        self.set_charisma(self.charisma() - 2)

    def __str__(self):
        my_string = ("Race: Dwarf\n" +
                     super(Dwarf, self).__str__() +
                     f"magic_res:{self.__magic_res}\n")
        return my_string


class Human(Humanoid):
    def __init__(self):
        super().__init__()
        self.boost_attribute()

    def boost_attribute(self):
        valid_attr = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        while True:
            print("As a Human, you may add +2 bonus points to a single attribute of your choosing ")
            print(valid_attr)
            boost_choice = input("Select which attribute to boost(+2): ").lower()
            if boost_choice in valid_attr:
                break
            else:
                print("incorrect choice, try again...")

        if boost_choice == "strength":
            self.set_strength(self.strength() + 2)
        elif boost_choice == "dexterity":
            self.set_dexterity(self.dexterity() + 2)
        elif boost_choice == "constitution":
            self.set_constitution(self.constitution() + 2)
        elif boost_choice == "intelligence":
            self.set_intelligence(self.intelligence() + 2)
        elif boost_choice == "wisdom":
            self.set_wisdom(self.wisdom() + 2)
        elif boost_choice == "charisma":
            self.set_charisma(self.charisma() + 2)

    def __str__(self):
        my_string = ("Race: Human\n" + super(Human, self).__str__())
        return my_string


def character_creator():
    character = None
    valid_races = ["human", "elf", "dwarf"]
    print("You may choose from the following playable races: " + str(valid_races))
    while True:
        race = input("Enter race: ").lower()
        if race in valid_races:
            if race == "human":
                character = Human()
            elif race == "elf":
                character = Elf()
            elif race == "dwarf":
                character = Dwarf()
            break
        else:
            print("Invalid race, try again...")

    while True:
        height = float(input("\nEnter character height(3ft - 7ft): "))
        if character.set_height(height):
            break
        else:
            print("Invalid height, try again...")

    while True:
        weight = float(input("\nEnter character weight(60lbs - 300lbs): "))
        if character.set_weight(weight):
            break
        else:
            print("Invalid weight, try again...")

    valid_hair_colors = ["white", "silver", "gray", "black", "brown", "green", "blue", "yellow", "pink", "red",
                         "blonde"]
    print("\nChoose hair color from" + str(valid_hair_colors))
    while True:
        hair_color = input("Enter character hair color: ").lower()
        if character.set_hair_color(hair_color, valid_hair_colors):
            break
        else:
            print("Invalid Hair Color, try again...")

    valid_eye_colors = ["white", "black", "red", "green", "blue", "brown", "purple", "amber"]
    print("\nChoose eye color from " + str(valid_eye_colors))
    while True:
        eye_color = input("Enter character eye color: ").lower()
        if character.set_eye_color(eye_color, valid_eye_colors):
            break
        else:
            print("Invalid eye color, try again...")

    print("Your character's final attributes are: " )

    print(character)

    print("Thank you for playing Falls of Eternity! ")
    
if __name__ == "__main__":
    character_creator()

        
