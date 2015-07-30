#####################################
# Playerbook for Beyond the Wall
# The Village Hero, from The Village
#####################################

# -*- coding:utf8 -*-

from random import choice, randint

# choice returns a random element from a list

# *********************
# common functions
# *********************

def sumlists(x, y):
        '''Adds the elements of two equally sized lists'''
        z = []
        for i in range(0,len(x)): z.append(x[i] + y[i])
        return z

def d(number_of_dice, faces):
        ''' A recursive function. 3d6 = d(3, 6) 2d10 = d(2,10)'''
        if number_of_dice < 1: return 0
        else: return randint(1, faces) + d(number_of_dice -1, faces)

def ability_bonus(ability):
  ''' assumes ability scores >= 8'''
  if ability < 9: return -1
  elif ability < 13: return 0
  elif ability < 16: return 1
  elif ability < 18: return 2
  else: return 3

def show_list(lista):
        for i in range(len(lista)): print(i, lista[i])

def choose_from_list(x):
        ''' display a menu asking user to pick an item from list x '''
        show_list(x)
        y = safe_input_int("Choose from the list by selecting a number: ",len(x) - 1)
        return x[y]

def update_stats(x,y):
        ''' x = list containing the data to update  y = 1 update skills y = 2 update equipment y = 3 update knacks else do nothing'''
        global background
        global pip
        global skills
        background += "\n{}".format(x[0])
        pip = sumlists(pip, x[1])
        z = " {},".format(x[2])
        if y == 1: skills += z
        elif y == 2: knack += z
        elif y == 3: equipment += z
        else: return

def safe_input_int(message, maximo):
  ''' filters input from the user, only allowing integers (numbers) of a given range'''
  print(maximo)
  try:
    j = int(input(message))
    if j > maximo: return safe_input_int(message, maximo)
    else: return j
  except:
    return safe_input_int(message, maximo)

# *********************
# "questions"
# *********************

def parents(location):
    parent_list_default = [
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
    question = "What did your parents do in the village? What did you learn from them?"
    if location == "default": parent_list = parent_list_default
    else: parent_list = parent_list_default # I know it doesn't make much sense right now, but it will as we expand the app to include more and more playerbooks
    answer = choice(parent_list)
    answer[0] = question + "\n\t" + answer[0]
    return answer

def childhood():
        childhood_list = [
                ["Children often fight, but you never lost.", [2,0,0,0,1,0],""],
                ["There wasn't a game you chouldn't win.", [0,2,0,1,0,0],""],
                ["You were the toughest kid around.", [0,2,0,0,0,1],""],
                ["No secret escaped you.", [0,1,0,2,0,0],""],
                ["Your empathy made you a sought after confidant.", [0,1,0,0,2,0],""],
                ["You never met someone who didn't like you.", [1,0,0,0,0,2],""],
                ["You solved everyone else's problems, and never mentioned your own.", [2,1,0,0,0,1],""],
                ["Everyone has something to teach, and you learned a little from them all.", [0,0,1,1,1,0],""]
                ]
        question = "How did you distinguish yourself as a child?"
        answer = choice(childhood_list)
        answer[0] = question + "\n\t" + answer[0]
        return answer

def friends():
        friends_list = [
                ["Laboring with the blacksmith took your mind off your troubles.", [2,0,0,0,0,1],""],
                ["The fishermen took a liking to you and you swapped stories with them.", [0,0,2,0,1,0],""],
                ["You went camping with the hunters.", [0,2,0,1,0,0],""],
                ["The elders taught you the ancient game of chess.", [0,0,1,2,0,0],""],
                ["You are about to marry into the Miller's family.", [1,0,0,0,2,0],""],
                ["You broke someone's heart, or maybe they broke yours.", [0,1,0,0,2,0],""],
                ["The old wido needed help around the house.", [1,0,0,1,0,1],""],
                ["The grizzled mercenary who settle in town taught you.", [0,1,1,0,1,0],""]
                 ]
        question = "The other player characters were your best friends. Who else in the village befriended you while you were growing up?"

        answer = choice(friends_list)
        answer[0] = question + "\n\t" + answer[0]
        return answer
        

def q4(pc_type):
        ''' q4 the 4th question in the player-books for lack of a better name'''
        questions_dict = {"Self Taught Mage" : "Who wrote your precious book of magic?",
                          "Untested Thief" : "Who taught you how to cheat or steal?",
                          "Village Hero" : "How did you earn your name?", 
                          "Witch's Prentice" : "What first caused the witch to choose you?",
                          "Would-be Knight" : "Where did you practice your skill at arms?",
                          "Young Woodsman" : "What sort of woodsman are you?"}
        stm = [
                ["An old sage from the south.", [0,0,0,3,0,0], "ancient history"],
                ["A famous bard who traveled far and wide.", [0,0,0,0,0,3], "survival"],
                ["A great archmage from the sunken kingdom.", [0,0,0,3,0,0], "forbidden knowledge"],
                ["The head of a secret order from long ago.", [0,0,0,0,3,0], "politics"],
                ["A plunderer of forgotten tombs.", [0,0,3,0,0,0], "trapping"],
                ["A mighty wizard who marched with great armies.", [0,3,0,0,0,0], "command"]
                ]
        
        ut = [
                ["An old pickpocket from the city to the south.", [0,0,3,0,0,0], "pickpocketing"],
                ["An unscrupulous old sneak in the village.", [0,0,0,0,3,0], "stealth"],
                ["You trained yourself by trial and error.", [0,0,0,3,0,0],"trapping"],
                ["The village locksmith.", [0,0,3,0,0,0], "lockpicking"],
                ["A local thug with few friends.", [3,0,0,0,0,0], "athletics"],
                ["A savvy and charming traveller.", [0,0,0,0,0,3], "deceit"]
                ]
        
        vh = [
                ["A great bear attacked at the edge of the village, but you wrestled it to the ground.", [3,0,0,0,0,0], "animal lore"],
                ["You bested a foul and unnatural monster in the woods.", [0,3,0,0,0,0], "alertness"],
                ["You repelled an attack by nighttime raiders and tended to the wounded afterward.", [0,0,0,0,3,0], "healing"],
                ["You saved a child from a pack of wolves.", [0,0,3,0,0,0], "survival"],
                ["When a long drought came, you got the farmers through the worst of it.", [0,0,0,0,3,0], "farming"],
                ["You ran off the wicked sheriff who had plagued the village for years.", [0,0,0,0,0,3], "politics"]
                ]

        wp = [
               ["She was impressed by the old stories and lore that filled your head.", [0,0,0,3,0,0], "folklore"],
               ["No other six-year old had his own still.", [0,0,0,0,0,3], "brewing"],
               ["You command respect wherever you go.", [0,0,0,3,0,0], "intimidate"],
               ["The woods where she wanders are your second home.", [0,0,0,0,3,0], "survival"],
               ["Your craftsmanship.", [0,0,3,0,0,0], "a trade skill"],
               ["You always tend the sick in the village.",  [0,3,0,0,0,0], "herbalism"]
                ]

        wbk = [
                ["Raiders from the north sometimes reach the village, and you were always the first volunteer in the forces which defended against them.", [3,0,0,0,0,0], "command"],
                ["You are truly untested, but often boast otherwise.", [0,0,0,0,0,3], "deceit"],
                ["You spent long days riding and practicing alone.", [0,3,0,0,0,0], "riding"],
                ["A real knight came to town and you rode with him for a time.", [0,0,0,0,0,3], "etiquette"],
                ["When traders from the south came to the village, you found an old warrior’s training manual and you studied it every day thereafter.", [0,0,3,0,0,0], "military history"],
                ["You first saw action with the archers in the levy.", [0,0,3,0,0,0], "drinking"]
                ]

        yw = [
                ["You hunt large game in the wilderness.",[3,0,0,0,0,0], "hunting"],
                ["The roads and paths around the village are not safe and you watch them.", [0,3,0,0,0,0], "Alertness"],
                ["The clamor and bustle of the village disturb you and so you find solace in the wilderness.", [0,3,0,0,0,0], "Survival"],
                ["You wander the wilds, making nary a sound.", [0,0,3,0,0,0], "Stealth"],
                ["You are a tireless tracker, following your prey for days at a time.", [0,3,0,0,0,0], "tracking"],
                ["You are a great trapper, never coming home empty handed.", [0,0,0,0,3,0], "Trapping"]
                ]


        answers_dict = {"Self Taught Mage" : stm, "Untested Thief" : ut, "Village Hero" : vh,
                   "Witch's Prentice" : wp, "Would-be Knight": wbk, "Young Woodsman" : yw}

        answer = choice(answers_dict[pc_type])

        answer[0] = questions_dict[pc_type] + "\n\t" + answer[0]

        return answer

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
                ["They blessed you and built you a home.", [0,0,0,0,2,0], "your own home", ""],
                ["You were given an ancestral trophy.", [0,0,0,2,0,0], "trophy", ""],
                ["The smith gave you a very well-crafted weapon.", [2,0,0,0,0,0], "a very fine weapon", ""],
                ["Land is the greatest reward, so they gave you a field to plow.", [0,2,0,0,0,0], "a small farm", ""],
                ["The village gave you a rich wedding.", [0,0,0,0,0,2], "a spouse", "3"],
                ["You bear the town’s colors.", [0,2,0,0,0,0], "The village standard", ""]
                ]

        return choice(rewards_list)


# *****************************************
# values (hit points, initiative, ...
# *****************************************

def get_initiative():
        x = 1 + ability_bonus(pip[2])
        if pc_class == "Warrior": x += 1
        elif pc_class == "Rouge": x +=2
        return x

def get_fortune_points():
        if pc_class == "Rouge": return 5
        else: return 3

def get_hp():
        hp = ability_bonus(pip[1])
        if pc_class == "Warrior": hp += 10
        elif pc_class == "Rouge": hp += 8
        else: hp += 6
        return hp

def get_bab():
        if pc_class == "Warrior": return 1
        else: return 0

def get_class_abilities():
        if pc_class == "Warrior": return "Weapon Specialization and Knacks"
        elif pc_class == "Mage": return "Sense Magic and Spell Casting"
        else: return "Fortune’s Favor and Highly Skilled"

def get_silvers():
        silver = d(4,6)
        if reward[3] == "": return silver
        else: return silver + d(int(reward[3]),6)    

        
# main program
types = ["Self Taught Mage", "Untested Thief", "Village Hero", "Witch's Prentice", "Would-be Knight", "Young Woodsman"]

initial_skills = {"Village Hero": "Folklore",
                "Self Taught Mage": "Ancient History",
                "Untested Thief": "Stealth",
                "Witch's Prentice": "Herbalism",
                "Would-be Knight": "Riding",
                "Young Woodsman": "Survival"}

alignments = ["Lawful", "Neutral", "Chaotic"]
classes_dict = {"Village Hero": "Warrior",
                "Self Taught Mage": "Mage",
                "Untested Thief": "Rouge",
                "Witch's Prentice": "Mage",
                "Would-be Knight": "Warrior",
                "Young Woodsman": "Rogue"}

name = input("Your name: ")
pc_type = choose_from_list(types)
pc_class = classes_dict[pc_type]
fortune_points = get_fortune_points()
alignment = choose_from_list(alignments)

background = "Greetings! {} our {}, you are a {} level 1 {}.".format(name, pc_type, alignment, pc_class)
skills = initial_skills[pc_type] #includes class abilities
ws = "" # weapon specialization
pip = 6*[8] # STR, CON, DEX, INT, WIS, CHA all start at 8

# initial values

pip_dict = {"Village Hero": [2,2,0,0,0,0], "Self Taught Mage": [0,0,0,4,0,0,0], "Untested Thief": [0,0,4,0,0,0], "Witch's Prentice": [0,0,0,2,2,0],
            "Would-be Knight": [4,0,0,0,0,0], "Young Woodsman": [0,0,2,0,2,0]}

pip = sumlists(pip, pip_dict[pc_type]) 

equipment_dict = {"Village Hero": "Knife, peasants’ clothing, your favored weapon, the sturdiest shield in the village (+2 AC), meals and lodging forever in your home town.",
                  "Self Taught Mage": "a dagger, common robes, an ancient tome, many pouches, the components for a single Level One ritual.",
                  "Untested Thief": "several daggers, dark clothing, a light-weight sack, a 10’ coil of rope",
                  "Witch's Prentice": "a dagger, simple clothing, a flamboyant cloak or hat, a small musical instrument",
                  "Would-be Knight": "knife, peasants’ clothing, a horse of your own, your favored weapon, leather armor (+2 AC), four days feed for your mount",
                  "Young Woodsman": "knife, practical clothing, leathers (+2 AC), heavy cloak, flint and tinder, waterskin, a weapon of your choice"}

equipment = equipment_dict[pc_type]

update_stats(parents("default"), 1)

update_stats(childhood(),4)

update_stats(friends(),4)

update_stats(q4(pc_type),1)

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



initiative = get_initiative()
armor_class = 10 + ability_bonus(pip[2])


silvers = get_silvers()


bab = get_bab()
to_hit_melee = bab + ability_bonus(pip[0])
to_hit_missile = bab + ability_bonus(pip[2])
hit_points = get_hp()


# print to screen


print("\n" + "="*30 + " Background " + "="*30 + "\n")
print(" "*5,background)

print("\n" + "="*30 + " Basic Values " + "="*30 + "\n")

print("STR {}, CON {}, DEX {}, INT {}, WIS {}, CHA {}\n".format(pip[0], pip[1], pip[2], pip[3], pip[4], pip[5]))

print("* Initiative: {}".format(initiative))
print("* Armor class: {} + any armour".format(armor_class))
print("* Fortune points: {}".format(fortune_points))
print("* Hit points {}".format(hit_points))

print("* BAB: {}".format(bab))
print("* To hit bonus (hand to hand): {} + equipment, etc".format(to_hit_melee))
print("* To hit bonus (missile): {} + equipment, etc".format(to_hit_missile))

print("\n" + "="*30 + " Skills " + "="*30 + "\n")

print("*Skills: {}\n*Weapon specialization: {}\n*Knack: {}".format(skills, ws, knack))

print("\n" + "="*30 + " Equipment " + "="*30 + "\n")

print(equipment)
print("\nSilvers: ", silvers)



print("Saves: Breath Weapon: 17, Polymorph: 15, Spell: 17, Magic Item:16")


