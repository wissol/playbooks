#####################################
# Playerbook for Beyond the Wall
# The Village Hero, from The Village
#####################################

from random import choice, randint
# choice returns a random element from a list

# common fuctions

def sumlists(x, y):
        '''Adds the elements of two equally sized lists'''
        z = []
        for i in range(0,len(x)):
                z.append(x[i] + y[i])
        return z

def d(number_of_dice, faces):
        ''' A recursive function. 3d6 = d(3, 6) 2d10 = d(2,10)'''
        if number_of_dice < 1:
                return 0
        else:
                return randint(1, faces) + d(number_of_dice -1, faces)
        # A non recursive alternative
        # x = 0
        # for i in range(1, number_of_dice):
        #       x += randint(1,6)
        # return x
        
def ability_bonus(ability):
        if ability < 9:
                return -1
        elif ability < 13:
                return 0
        elif ability < 16:
                return 1
        elif ability < 18:
                return 2
        else:
                return 3
        
def parents():
	parent_list = [
		["You are an orphan. Things were hard for you.", [0,0,0,1,2,2], ""], 
		["Your father was an outcast, rightfully or not.", [0,1,0,2,1,0], "survival"],
		["Your father were fishermen and you grew up by the river.", [1,0,2,0,1,0], "fishing"],
		["Your family worked a small farm outside the village.", [0,2,0,0,1,1], "farming"],
		["Your father was the local smith and taught you both hammer and bellows.", [2,1,0,0,0,1], "smithing"],
		["You led the sheep out onto the mountain like your father before you.", [1,2,1,0,1,1], "" ],
		["You worked the loom, cutting and twisting, as the Fates.", [0,0,2,1,0,1], "weaving"],
		["Your parents ran the local inn. You grew up meeting many travellers and hearing their tales.", [0,0,1,1,1,2],""],
		["Your father or mother kept the old stories. Your head is filled with them.", [0,0,0,2,1,1], "folklore"],
		["Your father was a watchman, stern but fair with child and stranger alike.", [2,1,0,0,0,1], "athletics"],
		["You went on journeys into the woods to gather herbs and berries.", [0,1,1,0,2,0], "herbalism"],
		["Your father was a local merchant. You learn to name your price and charm your customers.", [0,0,1,1,0,2], "Haggling"]
		]

	return choice(parent_list)


def childhood():
        childhood_list = [
                ["Children often fight, but you never lost.", [2,0,0,0,1,0]],
                ["There wasn't a game you chouldn't win.", [0,2,0,1,0,0]],
                ["You were the toughest kid around.", [0,2,0,0,0,1]],
                ["No secret escaped you.", [0,1,0,2,0,0]],
                ["Your empathy made you a sought after confidant.", [0,1,0,0,2,0]],
                ["You never met someone who didn't like you.", [1,0,0,0,0,2]],
                ["You solved everyone else's problems, and never mentioned your own.", [2,1,0,0,0,1]],
                ["Everyone has something to teach, and you learned a little from them all.", [0,0,1,1,1,0]]
                ]

        return choice(childhood_list)

def friends():
        friends_list = [
                ["Laboring with the blacksmith took your mind off your troubles.", [2,0,0,0,0,1]],
                ["The fishermen took a liking to you and you swapped stories with them.", [0,0,2,0,1,0]],
                ["You went camping with the hunters.", [0,2,0,1,0,0]],
                ["The elders taught you the ancient game of chess.", [0,0,1,2,0,0]],
                ["You are about to marry into the Miller's family.", [1,0,0,0,2,0]],
                ["You broke someone's heart, or maybe they broke yours.", [0,1,0,0,2,0]],
                ["The old wido needed help around the house.", [1,0,0,1,0,1]],
                ["The grizzled mercenary who settle in town taught you.", [0,1,1,0,1,0]]
                 ]

        return choice(friends_list)

def great_deed():
        deed_list = [
                ["A great bear attacked at the edge of the village, but you wrestled it to the ground.", [3,0,0,0,0,0], "animal lore"],
                ["You bested a foul and unnatural monster in the woods.", [0,3,0,0,0,0], "alertness"],
                ["You repelled an attack by nighttime raiders and tended to the wounded afterward.", [0,0,0,0,3,0], "healing"],
                ["You saved a child from a pack of wolves.", [0,0,3,0,0,0], "survival"],
                ["When a long drought came, you got the farmers through the worst of it.", [0,0,0,0,3,0], "farming"],
                ["You ran off the wicked sheriff who had plagued the village for years.", [0,0,0,0,0,3], "politics"]
                ]

        return choice(deed_list)

def skill_at_arms():
        skill_at_arms_list = [
                ["You manned the shield wall in a time of war.", [0,2,0,0,0,0], "spear"],
                ["The old war hero in town taught you everything he knew.", [2,0,0,0,0,0], "sword"],
                ["You always led the boar hunts.", [0,2,0,0,0,0], "spear"],
                ["Chopping wood built your strength.", [0,2,0,0,0,0], "axe"],
                ["You distinguished yourself in the village levy.", [0,0,2,0,0,0], "long bow"],
                ["Bad luck taught you everything you know.", [0,0,0,2,0,0], "staff"]
                ]
        return choice(skill_at_arms_list)

def secrets():
        secrets_list = [
                ["You have found your one true love. The friend to your right knows who your love is and helped you gain your beloved’s affection, and gains +1 Wis.", [0,0,0,0,2,0], "defensive fighter"],
                ["Despite the awe in which your fellow villagers hold you, you lost your nerve and ran one time. The friend to your right fled danger with you and tells no one, and gains +1 Dex.", [0,0,2,0,0,0], "fleet"],
                ["You were bested by the next village’s hero last summer. The friend to your right was therewith you and took a beating from his buddies, and gains +1 Con.", [0,2,0,0,0,0], "another weapon specialization"],
                ["Once, some years ago, you killed someone you shouldn’t have. The friend to your right was as culpable as you, and gains +1 Str.", [2,0,0,0,0,0], "great strike"], 
                ["You made a deal with a wandering sorcerer to gain protection from dark magics. The friend to your right convinced him to ensorcel you, and gains +1 Cha.", [0,0,0,0,0,2], "resilience"],
                ["You don’t feel that you deserve the adoration of your neighbors and consider yourself a hero by luck alone. The friend to your right shares your doubts, and gains +1 Int.", [0,0,0,2,0,0], "resilience"]
                ]

        return choice(secrets_list)

def rewards():
        rewards_list = [
                ["They blessed you and built you a home.", [0,0,0,0,2,0], "your own home"],
                ["You were given an ancestral trophy.", [0,0,0,2,0,0], "trophy"],
                ["The smith gave you a very well-crafted weapon.", [2,0,0,0,0,0], "a very fine weapon"],
                ["Land is the greatest reward, so they gave you a field to plow.", [0,2,0,0,0,0], "a small farm"],
                ["The village gave you a rich wedding.", [0,0,0,0,0,2], ""],
                ["You bear the town’s colors.", [0,2,0,0,0,0], "The village standard"]
                ]

        return choice(rewards_list)


# main program
name = input("Your name: ")
alignment = input("Your alignment: ")

background = "Greetings! {} our Village Hero, you are a {} level 1 warrior.".format(name, alignment)
skills = "folklore,"
ws = "" # weapon specialization
pip = 6*[8] # STR, CON, DEX, INT, WIS, CHA all start at 8

# initial values

pip = sumlists(pip, [2,2,0,0,0,0]) # adds 2 to STR and CON so the Village Hero starts with STR and CON = 10

equipment = "Knife, peasants’ clothing, your favored weapon, the sturdiest shield in the village (+2 AC), meals and lodging forever in your home town."

my_parents = parents()
background += " {}".format(my_parents[0])
pip = sumlists(pip, my_parents[1])
skills += " {},".format(my_parents[2])

my_childhood = childhood()

background += " {}".format(my_childhood[0])
pip = sumlists(pip, my_childhood[1])

my_friends = friends()
background += " {}".format(my_friends[0])
pip = sumlists(pip, my_friends[1])

my_great_deed = great_deed()
background += " {}".format(my_great_deed[0])
pip = sumlists(pip, my_great_deed[1])
skills += " {}".format(my_great_deed[2])

my_skill_at_arms = skill_at_arms()
background += " {}".format(my_skill_at_arms[0])
pip = sumlists(pip, my_skill_at_arms[1])
ws = my_skill_at_arms[2]

secret = secrets()
background += " {}".format(secret[0])
pip = sumlists(pip, secret[1])
knack = secret[2]

reward = rewards()
background += " {}".format(reward[0])
pip = sumlists(pip, reward[1])
equipment += reward[2] + "."


initiative = 1 + 1 + ability_bonus(pip[2])
armor_class = 10 + ability_bonus(pip[2])

silvers = d(4,6)
if reward[2] == "":
        silvers += d(3,6)

to_hit = 1 + ability_bonus(pip[0])
hit_points = 10+ability_bonus(pip[1])
        

# print to screen


print("\n" + "="*30 + " Background " + "="*30 + "\n")
print(" "*5,background)

print("\n" + "="*30 + " Basic Values " + "="*30 + "\n")

print("STR {}, CON {}, DEX {}, INT {}, WIS {}, CHA {}\n".format(pip[0], pip[1], pip[2], pip[3], pip[4], pip[5]))

print("* Initiative: {}".format(initiative))
print("* Armor class: {}".format(armor_class))
print("* Fortune points: 3")
print("* Hit points {}".format(hit_points))

print("* BAB: 1")
print("* To hit bonus: {}".format(to_hit))

print("\n" + "="*30 + " Skills " + "="*30 + "\n")

print("*Skills: {}\n*Weapon specialization: {}\n*Knack: {}".format(skills, ws, knack))

print("\n" + "="*30 + " Equipment " + "="*30 + "\n")

print(equipment)
print("\nSilvers: ", silvers)



print("Saves: Breath Weapon: 17, Polymorph: 15, Spell: 17, Magic Item:16")


