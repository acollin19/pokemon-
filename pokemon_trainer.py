# Assignment 4, Question 2
# Author: Angele Park Collin

from item import Item
from pokemon import Pokemon

class PokemonTrainer:
    '''A class to represent a Pokemon trainer.'''
# Initializer method--> creating the four attributes
    def __init__(self, name):
        self.name=name
        self.pokemon=[]
        self.items=[]
        self.current_active_pokemon=None
        
    def __iadd__(self,other):
        if isinstance(other, Pokemon):
            self.add_pokemon(other)
            return self
        
        elif isinstance(other, Item):
            self.add_item(other)
            return self
              
        else:
            raise TypeError("Object must be of type Pokemon or Item")
            
    def add_pokemon(self, pkmn):
# Add the pokemon (parameter pkmn) into list of pokemons but if no active one then set to parameter
        self.pokemon.append(pkmn) 
        if self.current_active_pokemon==None:
            self.current_active_pokemon=pkmn
        
    def add_item(self, item):
        self.items.append(item)
    
    def switch_active_pokemon(self, index):
       self.current_active_pokemon=self.pokemon[index]
        
    def has_usable_pokemon(self):
        for each_pokemon in self.pokemon:
# Access the attribute current_hp for each_pokemon (class pokemon).
            if each_pokemon.fainted == False:
                return True            
        return False
            