class Ship:


    def __init__(self, id, nombre, origin, type_class, tier_number, max_velocity):
        self.id = id
        self.nombre = nombre
        self.origin = origin
        self.type_class = type_class
        self.tier_number = tier_number
        self.max_velocity = max_velocity


    def __repr__(self):
        return "Ship ('{}', '{}', {})".format(self.nombre, self.type, self.tier)


