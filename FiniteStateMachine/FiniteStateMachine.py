#Jarrett Tranel 1/31/2021

playerHealth = 100
npcHealth = 100
npcHeals = 2


def state_Wandering():
    print ("")
    print("A man is in a wandering state. Do you approach?")
    print ("1.Yes")
    print ("2.No")
    choice = input()
    if (choice == "2"):
        state_Wandering()
    else:
        state_Alarm()
        
def state_Alarm():
    print ("")
    print("The man is in his alarmed state")
    print("What do you do next?")
    print ("1.Make Small Talk")
    print ("2.Leave the Area")
    print ("3.Equip your weapon")
    choice = input()
    if (choice == "1"):
        state_Friendly()
    elif (choice == "2"):
        state_Wandering()
    elif (choice == "3"):
        state_Attack()

def state_Friendly():
    print ("")
    print("The man is in his Friendly State")
    print("What do you do next?")
    print ("1.Leave the Area")
    print ("2.Equip your weapon")
    choice = input()
    if (choice == "1"):
        state_Wandering()
    elif (choice == "2"):
        state_Attack()

def state_Attack():
    print ("")
    print ("The man is in his attack state")
    global npcHealth
    npcHealth = npcHealth - 25
    print ("You attack him. He is now at " + str(npcHealth) + " health")
    global playerHealth
    playerHealth = playerHealth - 10
    print ("He attacks you. You are now at " + str(playerHealth) + " health")
    if (playerHealth <= 0):
        print ("You are defeated and the man goes back to his wandering stage")

    print("What do you do next?")
    print("1.Run away")
    print("2.Stay and Fight")
    choice = input()
    if (choice == "1"):
        state_Wandering()
    elif (choice == "2"):
        if(npcHealth >= 51):
            state_Attack()
        elif(npcHealth >=26):
            state_Defend()
        else:
            if(npcHeals >= 1):
                state_Heal()
            else:
                state_RunAway()

def state_Defend():
    print ("")
    print ("The man is in his defend state")
    global npcHealth
    npcHealth = npcHealth - 15
    print ("You attack him. He is now at " + str(npcHealth) + " health")
    global playerHealth
    playerHealth = playerHealth - 8
    print ("He attacks you. You are now at " + str(playerHealth) + " health")
    if (playerHealth <= 0):
        print ("You are defeated and the man goes back to his wandering stage")

    print("What do you do next?")
    print("1.Run away")
    print("2.Stay and Fight")
    choice = input()
    if (choice == "1"):
        state_Wandering()
    elif (choice == "2"):
        if(npcHealth >=26):
            state_Defend()
        elif (npcHealth >= 1):
            if(npcHeals >= 1):
                state_Heal()
            else:
                state_RunAway()
        else:
            state_Dead()

def state_Heal():
    print ("")
    print ("The man is in his heal state")
    print ("The man heals 40 health")
    global npcHeals
    global npcHealth
    npcHeals -= 1
    npcHealth += 40
    if (npcHealth >= 51):
        state_Attack()
    else:
        state_Defend()

def state_RunAway():
    print ("")
    print ("The man is in his run away state")
    print ("Do you chase him?")
    print ("1.Yes")
    print ("2.No")
    choice = input()
    if (choice == "1"):
        state_Dead()
    else:
        state_Wandering()

def state_Dead():
    print ("You win this fight")


state_Wandering()