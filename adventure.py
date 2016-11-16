# Alex Thoennes
# 4-26-13




import turtle
import random

class Treasure:
    def shop(self, item):
        self.item = item
        
    def __init__(self, search):
        self.search = search

# monster class used every time a monster appears
class Monster:
    name = ""
    def __init__ (self, hp, exp, level, nameChoice):

        # name list
        names = ["Goblin", "Kamodo-Dragon", "Troll", "Skeleton", "Pikachu", "Amanda", "Anti-Christ", "Creeper", "Rouge Tomato", "1000 Year Old Banana", "Bullrog",
                 "Death Hound", "Monkey", "Potted Plant", "Unspeakable Unbelievable Horror", "Wicked Pants", "Demonic Panda", "Mongo", "Feral Dog", "Evil Snowman"]
        self.hp = hp
        self.exp = exp
        self.level = level
        self.name = names[nameChoice]

# character class that is used for the start of the game
class Character:

    race = ""
    clas = ""
    name = ""
    exp = 0
    level = 1
    magic = 50
    gold = 100
    armor = 0
    hp = 100
    
    def __init__(self):#self, race, clas, name, exp, level, magic, gold, armor):

        # list of races
        races = ["Human", "Elf", "Halfling", "Orc", "Dwarf", "Maiar"]

        # class list
        classes = ["Warrior", "Mage", "Thief"]

        # declare name prompt
        self.name = input("What is thine name warrior?")
        
        # choose race prompt
        choice = input('Choose thines race. \n1)Elf\n2)Human\n3)Dwarf\n4)Hafling')
        self.race = races[int(choice) - 1]

        # class prompt
        choice = input("Choose thine class. \n1)Warrior\n2)Mage\n3)Theif")
        self.clas = classes[int(choice) - 1]

class Room:
    def __init__(self,north, south, east, west):
        self.n = north
        self.s = south
        self.e = east
        self.w = west
        self.monster = None

    def __init__(self):
        self.n = None
        self.s = None
        self.e = None
        self.w = None
        self.monster = None
        
    def setName(self, name):
        self.roomName = name

    def setDescription(self, description):
        self.roomDescription = description

    def goNorth(self):
        return self.n

    def goSouth(self):
        return self.s

    def goEast(self):
        return self.e

    def goWest(self):
        return self.w

    def setNorth(self, north):
        self.n = north
        
    def setSouth(self, south):
        self.s = south

    def setEast(self, east):
        self.e = east

    def setWest(self, west):
        self.w = west


### main ###

## create the dungeon rooms
start = Room()
start.setName('Entrance')
start.setDescription('')

rm1 = Room()
rm1.setName('Temple of Generic Niceness.')
rm1.setDescription('Good for CLERICS.\n')

rm2 = Room()
rm2.setName('Throne Room.')
rm2.setDescription('Good for HOBBITS and DWARVES but bad for ELVES.\n')

rm3 = Room()
rm3.setName('Seemingly Empty Room.\n')
rm3.setDescription('')

rm4 = Room()
rm4.setName('Library')
rm4.setDescription('Good for MAGES and CLERICS.\n')

rm5 = Room()
rm5.setName('Doom Room')
rm5.setDescription('Bad for CLERICS.\n')

rm6 = Room()
rm6.setName('Room of Short Jokes')
rm6.setDescription('Bad for HALFLINGS and DRWARVES.\n')

rm7 = Room()
rm7.setName('Odd Room')
rm7.setDescription('')

rm8 = Room()
rm8.setName('Twisty Tunnel')
rm8.setDescription('')

rm9 = Room()
rm9.setName('Low Passage')
rm9.setDescription('Bad For ELVES but good for HALFLINGS.\n')

rm10 = Room()
rm10.setName('Club House')
rm10.setDescription('Good for WARRIORS.\n')

rm11 = Room()
rm11.setName('Room of Questionable Odors')
rm11.setDescription('Bad for  HALFLINGS.\n')

rm12 = Room()
rm12.setName('Ye Swanky DonJon Shoppe')
rm12.setDescription('Good for ELVES.\n')

rm13 = Room()
rm13.setName('Ye Cheape DonJon Shoppe')
rm13.setDescription('Bad for ELVES.\n')

rm14 = Room()
rm14.setName('Stinking Pit')
rm14.setDescription('Bad for ELVES.\n')

rm15 = Room()
rm15.setName('Sticky Floor')
rm15.setDescription('Bad for HALFLINGS.\n')

rm16 = Room()
rm16.setName('Gym')
rm16.setDescription('')

rm17 = Room()
rm17.setName('Mush Room')
rm17.setDescription('Good for HALFLINGS but bad for WARRIORS.\n')

rm18 = Room()
rm18.setName('Sun Room')
rm18.setDescription('Bad for DWARVES and THEIFVES.\n')

rm19 = Room()
rm19.setName('Forge')
rm19.setDescription('Good for DWARVES.\n')

rm20 = Room()
rm20.setName('Big Room')
rm20.setDescription('')

rm21 = Room()
rm21.setName('Tomb Room')
rm21.setDescription('bad for MAGES but bad for WARRIORS.\n')

rm22 = Room()
rm22.setName('Den of Thieves')
rm22.setDescription('Bad for CLERICS but good for THIEVES.\n')

rm23 = Room()
rm23.setName('Ye Olde Don Jon Shoppe')
rm23.setDescription('')

rm24 = Room()
rm24.setName('Hall of Shame')
rm24.setDescription('Bad for Everyone\n')

rm25 = Room()
rm25.setName('Pawn Shoppe')
rm25.setDescription('Good for THIEVES.\n')

rm26 = Room()
rm26.setName('Attic')
rm26.setDescription('Good for HALFLINGS.\n')

rm27 = Room()
rm27.setName('Magnet Room')
rm27.setDescription('Bad for WARRIORS and THIEVES.\n')

rm28 = Room()
rm28.setName('Slimy Puddle')
rm28.setDescription('')

rm29 = Room()
rm29.setName('Padded Cell')
rm29.setDescription('Bad for WARRIORS\n')

rm30 = Room()
rm30.setName('Level-0-Mat')
rm30.setDescription('')

rm31 = Room()
rm31.setName('Throne Room')
rm31.setDescription('Good for ELVES and WARRIORS.\n')

rm32 = Room()
rm32.setName('\nKitchen')
rm32.setDescription('Good for HALFLINGS.\n')




## connect the rooms
start.setNorth(rm1)
start.setSouth(rm2)
start.setEast(rm3)
start.setWest(rm4)

rm1.setSouth(start)
rm1.setEast(rm14)
rm1.setNorth(rm15)
rm1.setWest(rm12)

rm2.setNorth(start)
rm2.setEast(rm5)
rm2.setSouth(rm6)
rm2.setWest(rm13)

rm3.setWest(start)
rm3.setSouth(rm5)
rm3.setNorth(rm14)

rm4.setEast(start)
rm4.setSouth(rm13)

rm5.setNorth(rm3)
rm5.setSouth(rm16)
rm5.setWest(rm2)

rm6.setNorth(rm2)
rm6.setSouth(rm7)
rm6.setEast(rm16)
rm6.setWest(rm12)

rm7.setNorth(rm6)
rm7.setEast(rm8)
rm7.setSouth(rm10)

rm8.setNorth(rm16)
rm8.setWest(rm7)
rm8.setSouth(rm9)

rm9.setNorth(rm8)
rm9.setWest(rm10)
rm9.setEast(rm22)

rm10.setNorth(rm7)
rm10.setEast(rm9)
rm10.setWest(rm11)

rm11.setEast(rm10)
rm11.setWest(rm13)
rm11.setSouth(rm12)

rm12.setNorth(rm11)
rm12.setWest(rm6)
rm12.setEast(rm1)
rm12.setSouth(rm23)

rm13.setNorth(rm4)
rm13.setEast(rm17)
rm13.setSouth(rm2)
rm13.setWest(rm11)

rm14.setNorth(rm15)
rm14.setSouth(rm3)
rm14.setWest(rm1)

rm15.setSouth(rm1)
rm15.setWest(rm18)

rm16.setNorth(rm5)
rm16.setSouth(rm8)
rm16.setWest(rm6)

rm17.setWest(rm13)

rm18.setEast(rm15)
rm18.setNorth(rm19)

rm19.setSouth(rm18)
rm19.setWest(rm20)

rm20.setEast(rm19)
rm20.setSouth(rm21)

rm21.setNorth(rm20)

rm22.setWest(rm9)
rm22.setEast(rm25)
rm22.setNorth(rm24)

rm23.setNorth(rm12)

rm24.setSouth(rm22)
rm24.setEast(rm25)

rm25.setNorth(rm22)
rm25.setSouth(rm26)
rm25.setEast(rm28)
rm25.setWest(rm24)

rm26.setNorth(rm25)
rm26.setEast(rm27)

rm27.setNorth(rm28)
rm27.setWest(rm26)

rm28.setNorth(rm29)
rm28.setWest(rm25)

rm29.setNorth(rm30)
rm29.setSouth(rm31)
rm29.setWest(rm32)
rm29.setEast(rm28)

rm30.setEast(rm29)

rm31.setEast(rm29)

rm32.setEast(rm29)

# create the adventurer                          
adv = Character()

print ('\nWelcome to Noegnud ' + adv.name, '\n')

print ('             _____ ')
print ('             \   /' )
print ('             |   |' )
print (' __          |   |____________________________________________')
print ('|  |_________|   |                                              \ ')
print ('|  |         |   |________________________________________________\ ')
print ('|  |_________|   |                                                / ')
print ('|__|         |   |_____________________________________________ / ')
print ('             |   | ')
print ('             |   | ')
print ('             /___\ ')


cmd = ''
currPos = start



# game loop
while (cmd != 'q'):
    
    ## Adventurers stats (if used secret name)
    if (adv.name == 'Alex' or adv.name == 'alex'):
        adv.hp = 999
        adv.magic = 999
        adv.gold = 999
        
    # help command
    if (cmd == 'h'):
        
        # print list of available actions
        print ('a = attack\nF = fire\nI = ice\nT = thunder\nn = north\ns = south\ne = east\nw = west')

    # display the stats of the player after every action
    print ('\n\n-------------------------------------------------------------------')
    print ('Race: ' + adv.race + ', Class: ' + adv.clas + ', HP: '+ str(adv.hp) + ', Exp: ' + str(adv.exp) +  ', Magic: '
           + str(adv.magic) + ', Level: ' + str(adv.level) + ', Gold: ' + str(adv.gold) + ', Armor: ' + str(adv.armor))
    print ('-------------------------------------------------------------------')

    # need to get to level 10 to win
    if adv.level == 10:
        print ('You WON!!')
        break
    
    cmd = input ('\n' + adv.name + ', what is your command? (h for help)')

    ##controls
    # south
    if (cmd == 's'):

        # if there is a room to go in
        if (currPos.goSouth() is not None):
            
            currPos = currPos.goSouth()
            print("\nRoom: " + currPos.roomName,'\n')
            #print (currPos.roomDescription)
           
        else:
            print ('Thou canst go south. \n')

    # north
    elif (cmd == 'n'):
        
        if (currPos.goNorth() is not None):
            
            currPos = currPos.goNorth()
            print("\nRoom: " + currPos.roomName,'\n')
            #print (currPos.roomDescription)
            
        else:
            print ('Thou canst go north.\n')

    # east
    elif (cmd == 'e'):
        
        if (currPos.goEast() is not None):
            
            currPos = currPos.goEast()
            print("\nRoom: " + currPos.roomName,'\n')
            #print (currPos.roomDescription)
            
        else:
            print ('Thou canst go east.\n')

    # west
    elif (cmd == 'w'):
        
        if (currPos.goWest() is not None):
            
            currPos = currPos.goWest()
            print("\nRoom: " + currPos.roomName,'\n')
            #print (currPos.roomDescription)
        else:
            print ('Thou canst go west.\n')

    # look for treasure
    elif (cmd == 't'):
        search = random.randint(1,10)
        print("\nYou gained " + str(search * 10) + " gold!\n")
        adv.gold = adv.gold + search * 10;

    # basic attack command
    elif (cmd == 'a'):

        # if no current monster
        if (currPos.monster is None):
            print ('\nThere are no monsters to attack...\n')
            
        else:
            # Calculates hit on monster
            damage = random.randint(1,5)
            
            if (adv.level > monster.level):
                damage = adv.level + damage
                print ('\nYou hit the ' + monster.name + ' for ' + str(damage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - damage
                
            else:
                damage = adv.level + damage
                print ('\nYou hit the ' + monster.name + ' for ' + str(damage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - damage
                
            if (currPos.monster.hp <= 0):
                print ('\nYou killed the ' + monster.name + ' and gained ' + str(currPos.monster.exp) + ' exp!\n')
                adv.exp = adv.exp + currPos.monster.exp

                # get rid of the monster
                currPos.monster = None

                # check to see if we leveled up
                if (adv.exp >= 20):
                    # leveled up
                    print ('\nLEVEL UP!\n')
                    adv.level = adv.level + 1
                    adv.exp = 0
                    adv.magic = 50

                    # gain 50 mana for every level up
                    adv.magic = adv.magic + 50

                    # gain 1 armor for every level up
                    adv.armor = adv.armor + 1
                    
            else:
                ##calculate monster attack
                damage = random.randint(0,5)
                damage = damage - adv.armor
                
                if (monster.level > adv.level):
                    damage = ((monster.level + damage) * 2)
                    print ('The '+ str(monster.name) + ' hit you for ' + str(damage) + ' points!\n')
                    adv.hp = adv.hp - damage
                elif (monster.level == adv.level):
                    print ('The ' + monster.name + ' hit you for ' + str(damage) + ' points!\n')
                if (adv.hp <= 0):
                    print ('you DIED!')
                    break

    # fire cost is 5
    elif (cmd == 'F'):

        # no monster at your current position
        if (currPos.monster is None):
            print ('There are no monsters to attack...\n')
            
        else:
            ##Calculates hit on monster
            #damge = random.randint(1,5)
            magicDamage = random.randint(5,10)
            magicCost = 5
            adv.magic = adv.magic - magicCost

            if (adv.level > monster.level):
                magicDamage = adv.level + magicDamage
                print ('\nYou hit the ' + monster.name + ' for ' + str(magicDamage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - magicDamage
                
            else:
                magicDamage = adv.level + magicDamage
                print ('\nYou hit the ' + monster.name + ' for ' + str(magicDamage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - magicDamage

            if (currPos.monster.hp <= 0):
                print ('\nYou killed the ' + monster.name + ' and gained ' + str(currPos.monster.exp) + ' exp!\n')
                adv.exp = adv.exp + currPos.monster.exp
                currPos.monster = None
                
                if (adv.exp >= 20):
                    print ('\nLEVEL UP!\n')
                    adv.level = adv.level + 1
                    adv.exp = 0
                    adv.magic = 50
                    adv.magic = adv.magic + 50
                    adv.armor = adv.armor + 1
                    
            else:
                ##calculate monster attack
                damage = random.randint(0,5)
                damage = damage - adv.armor
                
                if (monster.level > adv.level):
                    damage = ((monster.level + damage) * 2)
                    print ('\nThe ' + monster.name + ' hit you for ' + str(damage) + ' points!\n')
                    adv.hp = adv.hp - damage
                    
                elif (monster.level == adv.level):
                    print ('\nThe ' + monster.name + ' hit you for ' + str(damage) + ' points!\n')

                # end of the game
                if (adv.hp <= 0):
                    print ('You DIED!')
                    break
    # ice cost is 2
    elif (cmd == 'I'):
        if (currPos.monster is None):
            print ('\nThere are no monsters to attack...\n')
        else:
            ##Calculates hit on monster
            magicDamage = random.randint(2,7)
            magicCost = 2
            adv.magic = adv.magic - magicCost

            if (adv.level > monster.level):
                magicDamage = adv.level + magicDamage
                print ('\nYou hit the ' + monster.name + ' for ' + str(magicDamage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - magicDamage
                
            else:
                magicDamage = adv.level + magicDamage
                print ('\nYou hit the ' + monster.name + ' for ' + str(magicDamage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - magicDamage

            if (currPos.monster.hp <= 0):
                print ('\nYou killed the ' + monster.name + ' and gained ' + str(currPos.monster.exp) + ' exp!\n')
                adv.exp = adv.exp + currPos.monster.exp
                currPos.monster = None
                
                if (adv.exp >= 20):
                    print ('\nLEVEL UP!\n')
                    adv.level = adv.level + 1
                    adv.exp = 0
                    adv.magic = 50
                    adv.magic = adv.magic + 50
                    adv.armor = adv.armor + 1
            else:
                ##calculate monster attack
                damage = random.randint(0,5)
                damage = damage - adv.armor
                if (monster.level > adv.level):
                    damage = ((monster.level + damage) * 2)
                    print ('\nThe ' + monster.name + ' hit you for ' + str(damage) + ' points!\n')
                    adv.hp = adv.hp - damage
                    
                elif (monster.level == adv.level):
                    print ('\nThe ' + monster.name + ' hit you for ' + str(damage) + ' points!\n')
                    
                if (adv.hp <= 0):
                    print ('You DIED!')
                    break
                
    # Thunder cost is 7
    elif (cmd == 'T'):
        if (currPos.monster is None):
            print ('\nThere are no monsters to attack...\n')
            
        else:
            ##Calculates hit on monster
            magicDamage = random.randint(7,12)
            magicCost = 7
            adv.magic = adv.magic - magicCost
            
            if (adv.level > monster.level):
                magicDamage = adv.level + magicDamage
                print ('\nYou hit the ' + monster.name + ' for ' + str(magicDamage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - magicDamage
                
            else:
                magicDamage = adv.level + magicDamage
                print ('\nYou hit the ' + monster.name + ' for ' + str(magicDamage) + ' points!\n')
                currPos.monster.hp = currPos.monster.hp - magicDamage
                
            if (currPos.monster.hp <= 0):
                print ('\nYou killed the ' + monster.name + ' and gained ' + str(currPos.monster.exp) + ' exp!\n')
                adv.exp = adv.exp + currPos.monster.exp
                currPos.monster = None
                
                if (adv.exp >= 20):
                    print ('\nLEVEL UP!\n')
                    adv.level = adv.level + 1
                    adv.exp = 0
                    adv.magic = 50
                    adv.magic = adv.magic + 50
                    adv.armor = adv.armor + 1
            else:
                ##calculate monster attack
                damage = random.randint(0,5)
                damage = damage - adv.armor
                
                if (monster.level > adv.level):

                    # damage is also level based
                    damage = ((monster.level + damage) * 2)
                    print ("\nThe " + monster.name + " hit you for " + str(damage) + " points!\n")
                    adv.hp = adv.hp - damage
                    
                elif (monster.level == adv.level):
                    print ("\nThe ' + monster.name + ' hit you for ' + str(damage) + ' points!\n")
                    
                if (adv.hp <= 0):
                    print ("ou DIED!")
                    break
                
    elif (cmd == 'q'):
        
        print ("Thou hast quit the game.")
        
    if (currPos.monster is None):
        
        monsterChance = random.randint(1, 10)

        if monsterChance < 7:
                                #HP#                    #EXP#                   #LEVEL#                 #NAME#
            monster = Monster(random.randint(5, 25),random.randint(10,30),random.randint(1, adv.level + 1), random.randint(1,19))
            print (monster.name + " HP: "+ str(monster.hp) + " Exp: " + str(monster.exp) + " Level: " + str(monster.level))
            currPos.monster = monster
            
    else:
        damage = random.randint(0,5)
        print (monster.name + " HP: " + str(monster.hp) + " Exp: " + str(monster.exp) + " Level: " + str(monster.level))
        
        if (monster.level > adv.level):
            damage = (monster.level + damage)



