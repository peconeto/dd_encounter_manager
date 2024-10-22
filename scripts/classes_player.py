class Player:
    """Playable hero"""

    def __init__(self,
                 name,
                 race,
                 playerClass,
                 abilityScores,
                 proficiencyBonus,
                 alignment,
                 hitPointsMax,
                 armorClass,
                 weapons
                ):
        self.name = name
        self.race = race
        self.playerClass = playerClass
        self.abilityScores = abilityScores
        self.proficiencyBonus = proficiencyBonus
        self.alignment = alignment
        self.hitPointsMax = hitPointsMax
        self.hitPoints = self.hitPointsMax
        self.armorClass = armorClass
        self.weapons = weapons
        self.size = "medium"
        self.speed = 30
        self.initiativeRoll = None
        self.initiativeRollModified = None
        self.initiativeRank = None

    def __str__(self):
        return f"{self.playerClass.capitalize()} {self.name} jumps into battle!"

    def rollForInitiative(self):
        self.initiativeRoll = roll_dice(20)
        self.initiativeRollModified = self.initiativeRoll + ability_score_to_modifier(self.abilityScores.dexterity)
        return f"{self.name} rolled a {self.initiativeRoll}."

    def attack(self, target, weapon):
        attackDetails = player_attack(
            player = self,
            target = target,
            weapon = weapon
            )
        return attackDetails
