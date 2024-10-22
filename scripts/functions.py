import random
import math

def roll_dice(sides = 20):
    """Returns a number between 1 and the sides of a dice using a random uniform distribution (default 20-sided)"""
    roll = random.randint(1, sides + 1)
    
    if sides not in {4, 6, 8, 10, 12, 20, 100}:
        print(f"Warning: It is uncommon to roll a {sides}-sided die. Are you sure?") # Can also use warnings.warn
        return roll
    else:
        return roll

def num_to_ordinal(n):
    """Convert a number to its ordinal representation"""
    #mod = n % 10
    if n % 10 in range(4, 10):
        suffix = "th"
    elif n % 10 == 0:
        suffix = "th"
    elif n % 10 == 1:
        suffix = "st"
    elif n % 10 == 2:
        suffix = "nd"
    elif n % 10 == 3:
        suffix = "rd"
    return f"{n}{suffix}"

def ability_score_to_modifier(ability_score):
    """Converts ability scores to ability score modifiers"""
    modifier = math.floor((ability_score - 10) / 2)
    
    return modifier

def monster_attack(target, weapon, attack_roll_modifier, damage_roll_modifier):
    attack_roll = roll_dice(20)
    
    damage_dice_rolls = []
    for rolls in range(weapon.damageDiceCount):
        damage_dice_rolls.append(roll_dice(weapon.damageDiceSides))
        rolls += 1
    
    attack_details = Attack(
        target = target,
        attackRoll = attack_roll,
        attackRollModified = attack_roll + attack_roll_modifier,
        damageRoll = sum(damage_dice_rolls) + damage_roll_modifier
        )
    
    return attack_details

def player_attack(player, target, weapon):
    attack_roll = roll_dice(20)
    
    damage_dice_rolls = []
    for rolls in range(weapon.damageDiceCount):
        damage_dice_rolls.append(roll_dice(weapon.damageDiceSides))
        rolls += 1

    if weapon.weaponType == "melee":
        attack_and_damage_roll_modifier = ability_score_to_modifier(player.abilityScores.strength)
    elif weapon.weaponType == "ranged":
        attack_and_damage_roll_modifier = ability_score_to_modifier(player.abilityScores.dexterity)
    
    attack_details = Attack(
        target = target,
        attackRoll = attack_roll,
        attackRollModified = attack_roll + player.proficiencyBonus + attack_and_damage_roll_modifier,
        damageRoll = sum(damage_dice_rolls) + attack_and_damage_roll_modifier
        )
    
    return attack_details