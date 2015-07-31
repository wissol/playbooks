#####################################
# Playerbook for Beyond the Wall
# by Miguel de Luis
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
        print(x,y)
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

def get_answer(question, lista):

        x = choice(lista)
        x[0] = question + "\n\t" + x[0]
        return x


def show_list(lista):
        for i in range(len(lista)): print(i, lista[i])

def choose_from_list(x):
        ''' display a menu asking user to pick an item from list x '''
        show_list(x)
        y = safe_input_int("Choose from the list by selecting a number: ",len(x) - 1)
        return x[y]

def safe_input_int(message, maximo):
  ''' filters input from the user, only allowing integers (numbers) of a given range'''
  try:
    j = int(input(message))
    if j > maximo: return safe_input_int(message, maximo)
    else: return j
  except:
    return safe_input_int(message, maximo)

def update_stats(x,y):
        ''' x = list containing the data to update  y = string telling what to update'''
        global background, pip, skills, equipment, magic, ws, knack
        background += "\n{}".format(x[0])
        pip = sumlists(pip, x[1])
        z = " {},".format(x[2])
        if y == "skills": skills += z
        elif y == "knack": knack += z
        elif y == "equipment": equipment += z
        elif y == "ws": ws = x[2]
        elif y == "magic": magic += z
        else: return

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

        return get_answer(question, childhood_list)

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

        return get_answer(question, friends_list)
        

def q4():
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

        return get_answer(questions_dict[pc_type], answers_dict[pc_type])

def q5():
        questions_dict = {"Self Taught Mage" : "What sort of mage was the author of the book?",
                          "Untested Thief" : "How do you attain your ill-gotten gains?",
                          "Village Hero" : "Where did you gain your skill at arms?", 
                          "Witch's Prentice" : "With what did the witch have power?",
                          "Would-be Knight" : "What is your preferred fighting style?",
                          "Young Woodsman" : "What is your hidden talent?"}
        stm = [
                ["A clever illusionist.", [0,0,0,0,0,2], "Greater Illusion(s), Wizard’s Mark(r), Glamour Weaving(c)"],
                ["A war wizard.", [0,2,0,0,0,0], "Burning Hands(s), Mage Armor(r), Glamour Weaving(c)"],
                ["A summoner of dark spirits.", [0,0,0,2,0,0], "Abjuration(s), Circle of Protection(r), Second Sight(c)"],
                ["A master of hidden q6.", [0,0,0,2,0,0],  "Terrifying Presence(s), Witch’s Watchman(r), Conjure Sound(c)"],
                ["A charming enchanter.", [0,0,0,0,0,2], "False Friend(s), Arcane Experiment(r), Hexing(c)"],
                ["A traveling sorcerer.", [0,2,0,0,0,0], "Feather Fall(s), Gather Mists(r), Blessing(c)"]
                ]
        
        ut = [
               ["You do little work yourself, but instead beg from the other villagers.", [0,2,0,0,0,0], "Begging"],
               ["When travelers from far away places pass through town you take interesting baubles from their purses.", [0,0,2,0,0,0], "Pickpocketing"],
               ["You can secretly find your way behind any door.", [0,0,0,2,0,0], "Lockpicking"],
               ["You charm everyone you meet.", [0,0,0,0,0,2], "Deceit"],
               ["Despite your other skills, you still work an honest profession.", [0,0,0,2,0,0], "A trade skill"],
               ["You do a little of this and a little of that and always get by.", [0,2,0,0,0,0], "Survival"]
               ]
        
        vh = [
               ["You manned the shield wall in a time of war.", [0,2,0,0,0,0], "spear"],
               ["The old war hero in town taught you everything he knew.", [2,0,0,0,0,0], "sword"],
               ["You always led the boar hunts.", [0,2,0,0,0,0], "spear"],
               ["Chopping wood built your strength.", [0,2,0,0,0,0], "axe"],
               ["You distinguished yourself in the village levy.", [0,0,2,0,0,0], "long bow"],
               ["Bad luck taught you everything you know.", [0,0,0,2,0,0], "staff"]
                ]

        wp = [
               ["With colors and hues.", [0,0,2,0,0,0], "Greater Illusion(s), Gather Mists(r), Glamour Weaving(c)"],
               ["With beasts", [0,0,0,0,2,0], "Call the Swarm(s), Bind Familiar(r), and the Beast Ken(r)"],
               ["With spirits and the unseen world.", [0,0,0,2,0,0], "Whispering Wind(s), Unseen Servant(r), Second Sight(c)"],
               ["With health and body.", [0,0,0,0,2,0], "Healing Touch(s), Goodberry(r), Blessing(c)"],
               ["With things that grow.", [0,2,0,0,0,0], "Pass without Trace(s), Staff of Might(r), Druid’s Touch(c)"],
               ["With people.", [0,0,0,0,0,2], "Sense Nature(s), Witch’s Watchman(r), Blessing(c)"]
                ]

        wbk = [
                ["Clever swordplay and a quick guard.", [0,0,2,0,0,0], "Longsword"],
                ["A glorious mounted charge.", [2,0,0,0,0,0], "Lance"],
                ["Constant and tireless pressure.", [0,2,0,0,0,0], "Mace"],
                ["Relentless attacks.", [2,0,0,0,0,0], "Battle Axe"],
                ["Flashy bladework.", [0,0,0,0,0,2], "Longsword"],
                ["Fierce intimidation and heavy blows.", [0,2,0,0,0,0], "Great Sword"]
                ]
        yw = [
                ["A soulful voice", [0,0,0,0,0,2], "singing"],
                ["Simple skills.", [0,0,0,0,2,0], "A trade skill"],
                ["You collect old lore.", [0,0,0,2,0,0], "Ancient History"],
                ["A musical gift.", [0,0,0,0,2,0], "play a musical instrument"],
                ["You are able to work the skins from your kills.", [2,0,0,0,0,0], "Tanning"],
                ["You make the greatest stews.", [0,0,2,0,0,0], "Cooking"]
                ]

        answers_dict = {"Self Taught Mage" : stm, "Untested Thief" : ut, "Village Hero" : vh, "Witch's Prentice" : wp, "Would-be Knight": wbk, "Young Woodsman" : yw}

        return get_answer(questions_dict[pc_type], answers_dict[pc_type])

def q6():

        questions_dict = {"Self Taught Mage" : "A spirit of Chaos was drawn by your power. How did you fight it off?",
                          "Untested Thief" : "As happens with many thieves, your first job went bad. What did you do when you got caught?",
                          "Village Hero" : "Every hero has a secret, so what’s yours?", 
                          "Witch's Prentice" : "The witch was hard on you. How did you finally prove yourself to her?",
                          "Would-be Knight" : "When did you first draw blood?",
                          "Young Woodsman" : "How do you make yourself uesful to the village?"}

        stm = [
                ["You stood before it with steady hands. The friend to your right stood by your side and did not waver, and gains +1 Wis.", [0,0,0,0,2,0], "Commanding Word"],
                ["You called it by its true name and cast it back into the abyss. The friend to your right helped you discover the name, and gains +1 Int.", [0,0,0,2,0,0], "Magic Missile"],
                ["Although you drove it off, it still waits for you just beyond the walls of sight. The friend to your right helped you slip its grasp, and gains +1 Dex.", [0,0,2,0,0,0], "Magic Missile"],
                ["Your clever words were enough to turn aside the worst of its trouble. The friend to your right also bandied words with the spirit, and gains +1 Cha.", [0,0,0,0,0,2], "Petrifying Gaze"],
                ["You stood behind the wall of your power until it grew weak. The friend to your right learned a lot from your brave stand, and gains +1 Int.", [0,0,0,2,0,0], "Mystical Shield"],
                ["You withstood its blows, while your friend sealed it beneath the earth. Your stalwart friend to the right saved the day, and gains +1 Con.",[0,2,0,0,0,0], "Healing Touch"]
                ]

        ut = [
                ["You fought for your life and escaped. The friend to your right fought off your attackers to help you get away, and gains +1 Str.", [2,0,0,0,0,0], "Athletics"],
                ["You hid until it was safe. The friend to your right got caught up in your heist and had to hide out too, and gains +1 Dex.", [0,0,2,0,0,0], "Stealth"],
                ["You took a beating and learned a lesson. The friend to your right proved they would never desert you and took some licks too, and gains +1 Con.", [0,2,0,0,0,0], "Survival"],
                ["You pleaded your case and walked free. The friend to your right spoke on your behalf, and gains +1 Int.", [0,0,0,2,0,0], "Oratory"],
                ["You fessed up and made it right. The friend to your right helped you see the error of your ways, and gains +1 Wis.", [0,0,0,0,2,0], "Folklore"],
                ["You fast-talked the mark and made nice. The friend to your right bought you both drinks and joined the party, and gains +1 Cha.", [0,0,0,0,0,2], "Drinking"]
                ]

        vh = [
                ["You have found your one true love. The friend to your right knows who your love is and helped you gain your beloved’s affection, and gains +1 Wis.", [0,0,0,0,2,0], "defensive fighter"],
                ["Despite the awe in which your fellow villagers hold you, you lost your nerve and ran one time. The friend to your right fled danger with you and tells no one, and gains +1 Dex.", [0,0,2,0,0,0], "fleet"],
                ["You were bested by the next village’s hero last summer. The friend to your right was therewith you and took a beating from his buddies, and gains +1 Con.", [0,2,0,0,0,0], "another weapon specialization"],
                ["Once, some years ago, you killed someone you shouldn’t have. The friend to your right was as culpable as you, and gains +1 Str.", [2,0,0,0,0,0], "great strike"],
                ["You made a deal with a wandering sorcerer to gain protection from dark magics. The friend to your right convinced him to ensorcel you, and gains +1 Cha.", [0,0,0,0,0,2], "resilience"],
                ["You don’t feel that you deserve the adoration of your neighbors and consider yourself a hero by luck alone. The friend to your right shares your doubts, and gains +1 Int.", [0,0,0,2,0,0], "resilience"]
                ]

        wp = [
                ["Last summer you protected her from bandits in the forest and helped her escape the danger. The friend to your right helped you fi ght them off while you aided the witch in escaping, and gains +1 Str.", [2,0,0,0,0,0], "Mystical Shield"],
                ["For years you worked for her calmly and patiently, and never questioned her wisdom or authority. The friend to your right often calmed you when you grew frustrated with your lot, and gains +1 Wis.", [0,0,0,0,2,0], "Sanctuary of Peace"],
                ["You watched her for many years and learned all the secrets of her garden. The friend to your right often spent time there with you, keeping you company and learning at your side, and gains +1 Int.", [0,0,0,2,0,0], "Entanglement"],
                ["While she was always helpful to them, the witch was never trusted by the superstitious villagers. You defended the witch when they blamed her for a drought and would have cast her out. The friend to your right gave a rousing speech, and gains +1 Cha.", [0,0,0,0,0,2], "Petrifying Gaze"],
                ["You always paid close attention when the witch went into the woods, and you learned all of the hidden paths and mystical places there. The friend to your right has often traveled these paths with you, and gains +1 Int.", [0,0,0,2,0,0], "Entanglement"],
                ["One night a stranger came to rob the witch while she was in a deep trance. You caught him unawares and frightened him away, protecting your mistress. The friend to your right helped you rout the robber, and gains +1 Cha.", [0,0,0,0,0,2], "Terrifying Presence"]
                ]

        wbk = [
                ["You haven’t yet, but might pretend otherwise. The friend to your right often helps you pretend that you are more seasoned than you are, and gains +1 Cha.", [0,0,0,0,0,2], "Defensive Fighter"],
                ["One night, you surprised a murderous thug passing through town and looking for trouble. The friend to your right helped you get the jump on the villain, and gains +1 Int.", [0,0,0,2,0,0], "Fleet"],
                ["You accidentally slew a partner in training. The friend to your right stayed your hand when you almost made the same mistake again, and gains +1 Str.", [2,0,0,0,0,0], "Weapon Specialization (choose)"],
                ["When some ruffians attacked your beloved, you fought like a king of old, with great presence. The friend to your right fought off the gang with you, and gains +1 Cha.", [0,0,0,0,0,2], "Great Strike"],
                ["A boastful stranger challenged you to a duel and found you more than he could handle. The friend to your right distracted the stranger’s friends when they sought to aid your opponent, and gains +1 Dex.", [0,0,2,0,0,0], "Weapon Specialization (choose)"],
                ["A brigand was waylaying villagers on the road, but you decided to put an end to his robbery. The friend to your right traveled the roads with you for two weeks, hunting the thief down, and gains +1 Con.", [0,2,0,0,0,0], "Resilience"]
                ]

        yw = [
                ["You make long treks in the wilderness collecting herbs. The friend to your right often comes with you, and gains +1 Con.", [0,2,0,0,0,0], "Herbalism"],
                ["There are many forgotten paths in the woods and you guard them all, but not always alone. The friend to your right has stood with you time and again on those paths, and gains +1 Str.", [2,0,0,0,0,0], "Alertness"],
                ["In the winter, stores are often low and you bring in meat in lean times. The friend to your right brought down a wild boar with you last winter, and gains +1 Dex.", [0,0,2,0,0,0], "Hunting"],
                ["Sometimes armies from the south move on distant roads. Unseen, you watch them when they do. The friend to your right stayed with you last summer, watching just such a movement of troops, and gains +1 Dex.", [0,0,2,0,0,0], "Stealth"],
                ["You bring delicate herbs to the healer and aid him in his work. The friend to your right often aids you in this endeavor, and gains +1 Wis.", [0,0,0,0,2,0], "Herbalism"],
                ["The most dangerous animals often need culling, and you do this for the other villagers. Once, the friend to your right aided you in tracking a pack of ravenous wolves threatening the village, and gains +1 Int.", [0,0,0,2,0,0], "Tracking"]
                ]

        answers_dict = {"Self Taught Mage" : stm, "Untested Thief" : ut, "Village Hero" : vh, "Witch's Prentice" : wp, "Would-be Knight": wbk, "Young Woodsman" : yw}

        return get_answer(questions_dict[pc_type], answers_dict[pc_type])

def q7():
        
        questions_dict = {"Self Taught Mage" : "A real wizard from the south passed through the village when you came of age. What did he think of you?",
                          "Untested Thief" : "What was your greatest heist?",
                          "Village Hero" : "What rewards have you received from your village for your heroic acts?", 
                          "Witch's Prentice" : "Where is the witch now?",
                          "Would-be Knight" : "Now that you are ready, how will you seek your fortune?",
                          "Young Woodsman" : "What did you find in the woods that no one knows about?"}
        stm = [
                ["You impressed him with your knowledge.", [0,0,0,2,0,0], "a book you barely understand", "", ""],
                ["He said he would brook no rivals and you fled from him in the night.", [0,0,0,0,2,0], "", "", "Steed of the Sorecer(r)"],
                ["He performed a secret naming ceremony for you.", [0,2,0,0,0,0], "a engrave silver ring", "", ""],
                ["He was amused by your first steps toward learning magic and taught you a trick.", [0,0,0,0,0,2], "", "", "Unseen Servant(r)"],
                ["He inducted you into his secret order.", [0,0,0,0,2,0], "Wizard's Staff", "", ""],
                ["You were warned of his coming, became afraid, and hid from him.", [0,0,2,0,0,0], "", "", "Bind Familiar(r)"]
                ]

        ut = [
                ["You managed to nab a great bag of coins from a rich merchant.", [0,0,2,0,0,0], "" , "6", ""],
                ["You convinced an old man to will you his farm.", [0,0,0,2,0,0], "an all farm", "", ""],
                ["You nicked something special from a stranger passing through.", [2,0,0,0,0,0], "a very very sharp dagger", "", ""],
                ["You stole something from an odd man in the woods.", [0,2,0,0,0,0], "a strange silver ribbon", "", ""],
                ["You talked your way into a temple in the next village and left with something precious.", [0,0,0,0,0,2], "a mysterious idol", "", ""],
                ["You stole from another thief.", [0,0,2,0,0,0], "a fine set of lockpicks", "", ""]

                ]
        
        vh = [
                ["They blessed you and built you a home.", [0,0,0,0,2,0], "your own home", "", ""],
                ["You were given an ancestral trophy.", [0,0,0,2,0,0], "trophy", "", ""],
                ["The smith gave you a very well-crafted weapon.", [2,0,0,0,0,0], "a very fine weapon", "", ""],
                ["Land is the greatest reward, so they gave you a field to plow.", [0,2,0,0,0,0], "a small farm", "", ""],
                ["The village gave you a rich wedding.", [0,0,0,0,0,2], "a spouse", "3", ""],
                ["You bear the town’s colors.", [0,2,0,0,0,0], "The village standard", "", ""]
                ]

        wp = [
                ["She still works in the village as she always has.", [0,0,0,2,0,0], "healing potion", "4", ""],
                ["She vanished one day; her location is a mystery even to you.", [0,0,0,0,2,0], "the witch's hut", "", ""],
                ["Recently, a dark spirit came to claim you. She died banishing it and protecting you.", [0,2,0,0,0,0], "the witch's charred staff", "", ""],
                ["She went on a mission less than a week ago, leaving you in charge back home.", [0,0,0,0,0,2], "a silver brooch showing your authority", "", ""],
                ["She is in hiding, working on something secret.", [0,0,0,2,0,0], "a small crystal which can light your way", "", ""],
                ["For long months she has been tending someone in dangerous pregnancy", [0,0,0,0,2,0], "a lucky charm", "", ""]
                ]

        wbk = []

        yw = []

        answers_dict = {"Self Taught Mage" : stm, "Untested Thief" : ut, "Village Hero" : vh, "Witch's Prentice" : wp, "Would-be Knight": wbk, "Young Woodsman" : yw}

        return get_answer(questions_dict[pc_type], answers_dict[pc_type])


# *****************************************
# values (hit points, initiative, ...
# *****************************************

def get_initiative():
        x = 1 + ability_bonus(pip[2])
        if pc_class == "Warrior": x += 1
        elif pc_class == "Rouge": x += 2
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

initial_magic = {"Village Hero": "",
                "Self Taught Mage": "Mage Light(c)",
                "Untested Thief": "",
                "Witch's Prentice": "Hexing(c)",
                "Would-be Knight": "",
                "Young Woodsman": ""}

alignments = ["Lawful", "Neutral", "Chaotic"]

classes_dict = {"Village Hero": "Warrior",
                "Self Taught Mage": "Mage",
                "Untested Thief": "Rouge",
                "Witch's Prentice": "Mage",
                "Would-be Knight": "Warrior",
                "Young Woodsman": "Rogue"}

knack = ""

name = input("Your name: ")
pc_type = choose_from_list(types)
pc_class = classes_dict[pc_type]
fortune_points = get_fortune_points()
alignment = choose_from_list(alignments)
magic = initial_magic[pc_type]

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

update_stats(parents("default"), "skills")

update_stats(childhood(),99)

update_stats(friends(),99)

update_stats(q4(), "skills")

if pc_class == "Mage": update_stats(q5(), "magic")
elif pc_class == "Warrior": update_stats(q5(), "ws")
else: update_stats(q5(), "skills")

if pc_class == "Mage": update_stats(q6(), "magic")
elif pc_class == "Warrior": update_stats(q6(), "knack")
else: update_stats(q6(), "skills")

reward = q7()

update_stats(reward, "equipment")

initiative = get_initiative()
armor_class = 10 + ability_bonus(pip[2])


silvers = get_silvers()
magic += " " + reward[4]

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
print("*Magic: ", magic)

print("\n" + "="*30 + " Equipment " + "="*30 + "\n")

print(equipment)
print("\nSilvers: ", silvers)



print("Saves: Breath Weapon: 17, Polymorph: 15, Spell: 17, Magic Item:16")


