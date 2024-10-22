class AbilityScores:
    """Ability scores for creatures"""
    
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        ability_scores_set = {strength, dexterity, constitution, intelligence, wisdom, charisma}

        if any(score > 30 for score in ability_scores_set):
            print("Ability scores must be between 1 and 30.")
        elif any(score < 1 for score in ability_scores_set):
            print("Ability scores must be between 1 and 30.")
        else:
            self.strength = strength
            self.dexterity = dexterity
            self.constitution = constitution
            self.intelligence = intelligence
            self.wisdom = wisdom
            self.charisma = charisma

class Alignment:
    """Alignment for creatures"""

    def __init__(self, lawfulness, morality):
        self.valid_lawfulness = {"lawful", "neutral", "chaotic"}
        self.valid_morality = {"good", "neutral", "evil"}

        if lawfulness in self.valid_lawfulness:
            self.lawfulness = lawfulness
        else:
            print(f"Invalid lawfulness: {lawfulness}. Must be one of {self.valid_lawfulness}.")

        if morality in self.valid_morality:
            self.morality = morality
        else:
            print(f"Invalid morality: {morality}. Must be one of {self.valid_morality}.")

class Attack:
    """Attacks for creatures"""

    def __init__(self, target, attackRoll, attackRollModified, damageRoll):
        self.target = target
        self.attackRoll = attackRoll
        self.attackRollModified = attackRollModified
        self.damageRoll = damageRoll
