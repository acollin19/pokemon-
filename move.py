
class Move:
    '''Represents a Pokemon move.'''
# Set attributes as the same name as parameter for self object
    def __init__(self, name, move_type, damage):
        self.name=name
        self.move_type=move_type
        self.damage=damage

# Returning a string containing the values of all the attributes in a readable format
    def __str__(self):
        return "{} (type: {}, damage: {})".format(self.name,self.move_type,self.damage)
    
    