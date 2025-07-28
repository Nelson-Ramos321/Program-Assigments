import random
from ability import Ability
from armor import Armor

class hero:
    def __init__(self, nam, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors =[]
        self.abilities = []
        
        def battle(self, opponent):
            '''Fight another hero and chooses a winner randomly'''
            winner = random.choice([self.name, opponent.name])
            print(f"The winner of this battle is{winner}!")
        
        def add_ability(self,ability):
            '''Appends an ability to a hero's list of abilitys'''
            self.abilities.append(ability)

        def sum_of_attacks(self):   
            '''iterates through the entire list of abilities and '''
            total_damage = 0
            for ability in self.abilities:
                total_damage += ability.attack()
                return total_damage 
            def add_armor(self, armor):
                '''Appends armor to a hero's list of armor'''
                self.armors.append(armor)
                print(f"{armor} has been added to hero list of armor"")
            def defend(self):
            '''iterates through a entire list of armor '''
            total_block = 0
            for armor in self.armors:
                total_block += armor.block()
                return total_block
    if __name__ == "__main__":
        my_hero = Hero("grace hopper", 200)
        my_hero2 = Hero("spider-man", 300)
        print(my_hero.name)
        print(my_hero.current_health)
        ability1 = Ability("explosion", 300)
        ability2 = Ability("electricution", 150)
        ability3 = Ability("Web shooter", 50)
        ability4 = Ability("Punch", 20)
        my_hero.add_ability(ability1)
        my_hero.add_ability(ability4)
        my_hero2.add_ability(ability2)
        my_hero2.add_ability(ability3)
        print(my_hero.abilities)
        print(my_hero2.abilities)
g



