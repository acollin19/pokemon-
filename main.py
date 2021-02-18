from item import *
from move import Move
from battle import battle
from pokemon import *
from element_types import ElementType
from pokemon_trainer import PokemonTrainer

# ADDITIONAL FUNCTIONALITY - Adding 3 sub-classes to Item

if __name__ == '__main__':
    name = input("Enter your name: ")
    player = PokemonTrainer(name)
    player += Pokemon("Staryu", ElementType.WATER, [
        Move("water blast", ElementType.WATER, 5),
        Move("water cyclone", ElementType.WATER, 6)
    ])
    
    player += HealthPotion("potion", 20)
    
# ADDITIONAL FUNCTIONALITY
# -------------------------#
    player += LuckyEgg ("Lucky Egg: EXP increased!") # Increases EXP by 3 
    player += PowerUp ("Power Up: Full HP!") # HP increases back to max
    player += WideLens ("Wide Lens: Attack power increased!") # Increases the attack power by 5
# -------------------------#

    rival = PokemonTrainer("Gary")
    rival += Pokemon("Bulbasaur", ElementType.GRASS, [
        Move("constrict", ElementType.GRASS, 3),
        Move("tail swipe", ElementType.GROUND, 5)
    ])
    
    battle(player, rival)