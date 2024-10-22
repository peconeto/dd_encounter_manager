class Scimitar:
    """Weapon: Scimitar (2014 Player's Handbook)"""

    def __init__(self):
        self.name = "scimitar"
        self.cost = 25
        self.damageDiceCount = 1
        self.damageDiceSides = 6
        self.weight = 3
        self.weaponType = "melee"

class BattleAxe:
    """Weapon: Battle Axe (2014 Player's Handbook)"""

    def __init__(self):
        self.name = "battle axe"
        self.cost = 10
        self.damageDiceCount = 1
        self.damageDiceSides = 8
        self.weight = 4
        self.weaponType = "melee"
