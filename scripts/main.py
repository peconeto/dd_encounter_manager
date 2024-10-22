# Public libraries
from operator import attrgetter

# Local modules
from functions import *
from classes_helper import *
from classes_monsters import *
from classes_player import *
from classes_weapons import *

# Code
goblin1 = Goblin("Joe")

player1 = Player(name = "Ivan",
                 race = "human",
                 playerClass = "barbarian",
                 abilityScores = AbilityScores(16, 15, 14, 13, 12, 11),
                 proficiencyBonus = 3,
                 alignment = Alignment("lawful", "good"),
                 hitPointsMax = 30,
                 armorClass = 15,
                 weapons = [BattleAxe()]
                )

# Introduce combatants
combatants = [goblin1, player1]

random.shuffle(combatants) # Introduce combatants in a random order

for combatant in combatants:
    print(combatant)

# Roll for initiative
print("Roll for initiative!")
display(goblin1.rollForInitiative())
display(player1.rollForInitiative())

# Sort combatants list by modified initiative roll
combatants.sort(key = attrgetter('initiativeRollModified'), reverse = True) # Going to assume no ties for now, need to implement tie resolver later

# Assign list index as initiativeRank attribute to lock in order of combat
index = 0
for combatant in combatants:
    combatant.initiativeRank = index
    print(f'{combatant.name} will take turn {num_to_ordinal(index + 1)}.')
    index += 1

# Attack
active_player = combatants[0] # First index will attack
attack1 = active_player.attack(target = combatants[1], weapon = active_player.weapons[0]) # Targets the only other combatant with the default weapon

print(f'For troubleshooting only - attack roll: {attack1.attackRoll}')
print(f'For troubleshooting only - modified attack roll: {attack1.attackRollModified}')
print(f'For troubleshooting only - damage roll: {attack1.damageRoll}')
print(f'For troubleshooting only - armor class: {combatants[1].armorClass}')

# Show target hit points before attack
print(attack1.target.hitPoints)

# Resolve attack
if attack1.attackRoll == 1:
    print("Womp womp it's a nat 1 and misses.")
elif attack1.attackRoll == 20:
    attack1.target.hitPoints = attack1.target.hitPoints - (attack1.damageRoll * 2)
    print(f'A critical hit dealing {attack1.damageRoll * 2} damage!')
elif attack1.attackRollModified >= attack1.target.armorClass:
    attack1.target.hitPoints = attack1.target.hitPoints - attack1.damageRoll
    print(f'It hits, causing {attack1.damageRoll} damage.')
elif attack1.attackRollModified < attack1.target.armorClass:
    print("It misses.")

# Show target hit points after attack
print(attack1.target.hitPoints)
print(combatants[1].hitPoints) # This does the same thing! Cool!

# Result
if attack1.target.hitPoints <= 0:
    print(f'{attack1.target.name} faints.')
else:
    print(f'{attack1.target.name} is still standing.')

