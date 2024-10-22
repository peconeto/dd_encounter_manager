class Goblin:
    """Goblin creature (2014 Monster Manual)"""

    def __init__(self, name):
        self.name = name
        self.size = "small"
        self.creatureType = "humanoid"
        self.alignment = Alignment("neutral", "evil")
        self.armorClass = 15
        self.hitPointsMax = 7
        self.hitPoints = self.hitPointsMax
        self.speed = 30
        self.weapons = [Scimitar()]
        self.abilityScores =  AbilityScores(
            strength = 8,
            dexterity = 14,
            constitution = 10,
            intelligence = 10,
            wisdom = 8,
            charisma = 8
            )
        self.proficiencyBonus = 2
        self.challengeRating = 0.25
        self.initiativeRoll = None
        self.initiativeRollModified = None
        self.initiativeRank = None
    
    def __str__(self):
        return f"Goblin {self.name} smells blood!"

    def rollForInitiative(self):
        self.initiativeRoll = roll_dice(20)
        self.initiativeRollModified = self.initiativeRoll + ability_score_to_modifier(self.abilityScores.dexterity)
        return f"Goblin {self.name} rolled a {self.initiativeRoll}."

    def attack(self, target, weapon):
        attackDetails = monster_attack(
            target = target,
            weapon = weapon,
            attack_roll_modifier = 4,
            damage_roll_modifier = 2
            )
        return attackDetails
