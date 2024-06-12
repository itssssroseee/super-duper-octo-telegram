class PlayerCharacter:
    
    def __init__(self,health, armor_rating,attack_power):
        self.__health = health
        self.__armor_rating = armor_rating
        self.__attack_power = attack_power
        
    def set_health(self, health):
        if health < 1:
            self.__health = 1
            raise Exception('health should be more than 1. It was set automatically to 1.')
        elif  health > 100:
            self.__health = 100
            raise Exception('health shouldn\'t be more than 100. It was set automatically to 100')
        else:
            self.__health = health
            
    def set_armor_rating(self, armor_rating):
        if armor_rating < 1:
            self.__armor_rating = 1
            raise Exception('health should be more than 1. It was set automatically to 1.')
        
        elif armor_rating > 20:

            self.__armor_rating = 20
            raise Exception('health shouldn\'t be more than 20. It was set automatically to 20.')
        else:
            self.__armor_rating = armor_rating

    
    def set_attack_power(self,attack_power):
        if attack_power < 1:
            self.__attack_power = 1
            raise Exception('health should\'t be more than 1. It was set automatically to 1.')
            
        elif attack_power > 20:
             self.__attack_power = 20
             raise Exception('health shouldn\'t be more than 20. It was set automatically to 20.') 
        else:
            self.__attack_power = attack_power

    def get_health(self):
        return self.__health
    
    def get_armor_rating(self):
        return self.__armor_rating
    
    def get_attack_power(self):
        return self.__attack_power

  
def main():
    
    health = int(input("Enter Wizard's health (1-100): "))
    if health < 1:
        health = 1
        print('health should be more than 1. It was set automatically to 1.')
    elif  health > 100:
        health = 100
        print('health shouldn\'t be more than 100. It was set automatically to 100')
     
    armor_rating = int(input("Enter Wizard's rating (1-20): "))
    if armor_rating < 1:
        armor_rating = 1
        print('health should be more than 1. It was set automatically to 1.')
    elif armor_rating > 20:
        armor_rating = 20
        print('health shouldn\'t be more than 20. It was set automatically to 20.')
    
    attack_power = int(input("Enter Wizard's power ( 1-20): "))
    if attack_power < 1:
        attack_power = 1
        print('health should\'t be more than 1. It was set automatically to 1.')
    elif attack_power > 20:
        attack_power = 20
        print('health shouldn\'t be more than 20. It was set automatically to 20.') 
    
    # Define object using constructor
    wizard = PlayerCharacter(health, armor_rating, attack_power)

        # Output using getter from main
    print()
    print(f"The health of the wizard is {wizard.get_health()}")
    print(f"The armor rating of the wizard is {wizard.get_armor_rating()}")
    print(f"The attack power of the wizard is {wizard.get_attack_power()}")

    
if __name__ == '__main__':
    main()
