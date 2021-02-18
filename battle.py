import random # choose random move in battle() function

def battle(trainer1, trainer2):
    assert trainer1 is not None and trainer2 is not None
    print("Hey, {}! It's time to battle!".format(trainer1.name.upper()))
        
    print("{} wants to fight!".format(trainer2.name.upper()))
    print("{} sent out {}!".format(trainer2.name.upper(), trainer2.current_active_pokemon.name.upper()))
    
    print("Go! {}!".format(trainer1.current_active_pokemon.name.upper()))
    
    i = 0
    while trainer1.has_usable_pokemon() or trainer2.has_usable_pokemon():    
        if i % 2 == 0:
            attacker, defender = trainer1, trainer2
            attacker_pkmn, defender_pkmn = trainer1.current_active_pokemon, trainer2.current_active_pokemon
        else:
            attacker, defender = trainer2, trainer1
            attacker_pkmn, defender_pkmn = trainer2.current_active_pokemon, trainer1.current_active_pokemon
        
        print("Attacking:", attacker_pkmn) # calls __str__ method
        print("Defending:", defender_pkmn) # calls __str__ method
        
        if attacker == trainer1:
            print("\nFIGHT\tPKMN\nITEM\tRUN")
            VALID_COMMANDS = ['FIGHT', 'PKMN', 'ITEM', 'RUN']
            action = None
            while action not in VALID_COMMANDS:
                action = input("> ")
        
                if action == "FIGHT":
                    print("\n".join(["{} {}".format(i+1, move) for i, move in enumerate(attacker_pkmn.moves)]))
                    move_num = -1
                    while move_num < 0 or move_num >= len(attacker_pkmn.moves):
                        move_num = int(input("Enter number > ")) + 1
                    move = attacker_pkmn.moves[move_num]
                    print("{} used {}!".format(attacker.name.upper(), move.name.upper()))
                    attacker_pkmn.attack(defender_pkmn, move)
                    
                elif action == "PKMN":
                    print("\n".join(["{} {}".format(i+1, pokemon.name) for i, pokemon in enumerate(trainer1.pokemon)]))
                    pokemon_num = -1
                    while pokemon_num < 0 or pokemon_num >= len(trainer1.pokemon) or trainer1.pokemon[pokemon_num].fainted:
                        pokemon_num = int(input("Enter number > ")) + 1
                    print("{}, enough! Come back!".format(attacker_pkmn.name.upper()))
                    print("Go! {}!".format(trainer1.pokemon[pokemon_num].name.upper()))
                    attacker.switch_active_pokemon(pokemon_num)
                    
                elif action == "ITEM":
                    print("\n".join(["{} {}".format(i+1, item.name) for i, item in enumerate(trainer1.items)]))
                    item_num = -1
                    while item_num < 0 or item_num >= len(trainer1.items):
                        item_num = int(input("Enter number > ")) + 1
                    item = trainer1.items[item_num]
                    print("{} used {} on {}!".format(attacker.name.upper(), item.name.upper(), attacker_pkmn.name.upper()))
                    item.use(attacker_pkmn)
                    
                elif action == "RUN":
                    print("Can't escape!")
                    
                else:
                    print("Invalid!")
                        
        else: # attacker is trainer 2
            # attack with random move
            move = random.choice(attacker_pkmn.moves)
            print("Enemy {} used {}!".format(attacker_pkmn.name.upper(), move.name.upper()))
            attacker_pkmn.attack(defender_pkmn, move)
        
        if defender_pkmn.fainted:
            print("{} fainted!".format(defender_pkmn.name.upper()))
        
        input("Press [return] to continue!")
        print("\n\n")
        i += 1
    
    if pkmn1.fainted:
        print(pkmn2.name, "wins!")
        pkmn2.gain_exp(pkmn1.level)
    else: # pkmn2 fainted
        print(pkmn1.name, "wins!")
        pkmn1.gain_exp(pkmn2.level)
    
