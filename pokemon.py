# Assignment 4, Question 2
# Author: Angele Park Collin

import random
from element_types import ElementType

class Pokemon:
    '''Class to represent a Pokemon.'''
# Set three attributes of the same name as the parameters
    def __init__(self, name, pokemon_type, moves):
        self.name=name
        self.pokemon_type=pokemon_type
        self.moves=moves
# Set values for the following attributes
        self.level=1
        self.exp=0
        self.max_hp=random.randint(0,100)
        self.current_hp=self.max_hp
        self.attack_power=random.randint(1,5)
        self.defense_power=random.randint(1,5)
        self.fainted=False
        
    def __str__(self):
# Returns string in a readable format with two choices depending on if the pokemon fainted        
        if self.fainted == True:    
            return "{} ({} type);  HP: {}/{}; attack: {}; defense: {} Fainted".format(self.name, self.pokemon_type, self.current_hp, self.max_hp, self.attack_power, self.defense_power)
        else:
           return "{} ({} type);  HP: {}/{}; attack: {}; defense: {}".format(self.name, self.pokemon_type, self.current_hp, self.max_hp, self.attack_power, self.defense_power)
       
    def defend(self, strength):
# Calculating damage to current hp
        damage=random.randrange(len([1, strength - self.defense_power]))
        self.current_hp=self.current_hp-damage
# If current hp is 0 or negative then pokemon fainted 
        if self.current_hp<=0:
            self.fainted=True
# If damage was smaller than half its max hp the it took damage, other it's a critical hit
        if damage < 0.5*self.max_hp:
            print ("{} took {} damage.".format(self.name, damage))
        elif damage > 0.5*self.max_hp:
            print ("Critical hit!")          
        
    def attack(self, opponent, move):
# Calling the defend method on the opponent 
        opponent.defend(self.attack_power*(random.randint(1, move.damage)))
        
    def gain_HP(self, amount):
# Making sure the current hp does not go past the max hp when adding the amount       
        original_hp=self.current_hp
        self.current_hp+=amount       
        if self.current_hp > self.max_hp:
# if hp goes over then the amount increased is the change from current to max
            amount=self.max_hp - original_hp
            self.current_hp=self.max_hp
# Message saying how much HP was gained      
        print ("{} gained {} HP!".format(self.name, amount))
        
    def gain_exp(self, opponent_level):
# Adding the amoung of experience points gained to experience
        experience_points=random.randint(1, opponent_level)
        self.exp+=experience_points
        level=0
# if experience reached 10 then they go up a level if it does not, then they just gain exp
        if self.exp>=10:
            self.exp=0
            level+=1
            print ("{} gained a level. They are no level {}.".format(self.name, level))
        else:
            print ("{} gained {} EXP! ".format(self.name, experience_points))
         

class ElectricPokemon(Pokemon):
# Creating sub class, inheriting from parent class Pokemon
    def __init__(self, name, moves):
# Calling the parents class initializer method on self object      
        Pokemon.__init__(self, name, ElementType.ELECTRIC, moves)
       
        
    def attack(self, opponent, move):
# Checking the opponent's pokemon type and attacking based on their type  
        if self.pokemon_type == ElementType.GROUND:
            opponent.defend((2*self.attack_power)*random.randint(1, move.damage))
            print("It's super effective!")
            
        elif (self.pokemon_type == ElementType.ELECTRIC) or (self.pokemon_type == ElementType.FLYING):
            opponent.defend((0.5*self.attack_power)*random.randint(1, move.damage))
            print("It's not very effective...")
# if pokemon type not Electric, ground, or flying then call parent class' attack method           
        else:   
            Pokemon.attack(opponent, move)
        
            
