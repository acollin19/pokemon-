# Assignment 4, Question 2
# Author: Angele Park Collin

class Item:
    '''Represents an item that can be used in battle.'''
    def __init__(self, name):
        self.name=name
        
    def use(self, pokemon):
        raise NotImplementedError 
        

class HealthPotion(Item):
    
    def __init__(self, name, amount_of_hp_to_restore):
# Calling the parents in it function to reuse        
        Item.__init__(self,name)
        self.name=name
        self.amount_of_hp_to_restore=amount_of_hp_to_restore
        
        
    def use(self, pokemon):
        pokemon.gain_HP(self.amount_of_hp_to_restore)
        


class LuckyEgg(Item): # Increases EXP
    def __init__(self, name):       
        Item.__init__(self,name)
        
    def use(self, pokemon):
        pokemon.gain_exp=pokemon.exp + 3
        
        
class PowerUp(Item): # HP increases back to max
    def __init__(self, name):       
        Item.__init__(self,name)
    
    def use(self, pokemon):
        pokemon.current_hp=pokemon.max_hp
        

class  WideLens(Item): # Increases the attack power
    def __init__(self, name):       
        Item.__init__(self,name)
        
    def use(self, pokemon):
        pokemon.attack_power=pokemon.attack_power + 5
        
        
