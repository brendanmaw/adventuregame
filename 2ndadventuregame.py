print("Welcome to Bmaw's Adventure Game V2.0!")
name = input("Enter your name please: ").lower()
health = 100
weapon = True
age = input("Enter your age please: ")
if age <= str(17):
    print("Come back when you're old enough. ")
    quit()
if name == str("drew").lower():
    print("Sorry you cannot have that name, please try a different name")
    quit()
elif name == str("bryr"):
    print("Damn that sucks")

ready_to_begin = input("Ready to begin? (Y/N)").lower()
for ready_to_begin in ready_to_begin:
    if ready_to_begin == "y":
        print("Thanks for trying my game, that's very nice of you", name, "Let's get started")
        print("You currently have", health, "health. Try to survive your adventure and you shall be rewarded!")
        print("You are holding a knife that should assist you. Try not to drop it.\n")
    elif ready_to_begin == "n":
        print("Maybe tomorrow. Thanks anyways,", name,)
        quit()

first_test = input("Would you like to drop your knife? (Y/N)").lower()
for first_test in first_test:
    if first_test == "y":
        weapon = False
        print("Interesting... guess you like a challenge.")
        print("You drop your knife on the ground, you will not have it to assist you in combat any longer.")
    elif first_test == "n":
        print("Good answer. You are clearly a very smart person.")

back_alley = input("You appear in a dimly lit back alley, not sure where you are. Turn left or turn right: ").lower()
if back_alley == "left":
    print("You turn to the left and head down the alley. A large man approaches from the darkness")
    large_man = input(" Should you fight him or turn around and run? ")
    if large_man == "fight":
        if weapon == True:
            print("You pull out your knife and attack the man for some reason. He fights back but "
                  "you finish him off. Lose 10 health.")
            health -= 10
            print("You now have", health, "health")
        if weapon == False:
            print("You choose to attack the man unprovoked. You have no weapon so you throw a punch in his direction. "
                  "He dodges and draws a knife stabbing you. You take the damage and run. Lose 25 health")
            health -= 25
            print("You now have", health, "health")
    if large_man == "run":
        if weapon == True:
            print("You turn around and begin running but the man follows you. You show him your knife and he stops. "
                  "You leave unharmed.")
            print("You now have", health,"health")
        elif weapon == False:
            print("You turn around to run but the man quickly grabs you and stabs you. Lose 25 Health ")
            health -= 25
            print("You now have", health,"health")
elif back_alley == "right":
    print("You turn to the right and begin slowly creeping down the alley, you hear noise from behind a dumpster"
            " and decide to check it out. ")
    if weapon == True:
        print("You see a group of junkies shooting up behind the dumpster, They see you and assume a combat stance")
        print("You draw your knife and murder all 4 after a long fight, they do some damage with their needles but you"
              " escape relatively unharmed. Lose 10 health")
        health -=10
        print("You now have", health,"health")
    if weapon == False:
        print("You see a group of junkies shooting up behind the dumpster, They see you and assume a combat stance")
        print("Since you have no weapon they destroy you with toxic needles. Ouch. Lose 50 health.")
        health -= 50
        print("You now have", health,"health.")

corner_store = input("After leaving the alley you arrive at a corner store. Buy medicine or snack?")
if corner_store == "medicine":
    if weapon == True:
        print("You find the Tylenol but realize you have no money. You walk out of the store without paying. ")
        print("The store clerk chases you but backs off when he sees your knife. ")
        print("The Tylenol helps with the pain... gain 25 health")
        health += 25
        print("You have", health,"health")
    if weapon == False:
        print("You find the Tylenol but realize you have no money. You walk out of the store without paying.")
        print("The store clerk chases you and senselessly shoots you in the leg. Lose 25 Health")
        health -= 25
        print("You now have", health,"health")
elif corner_store == "snack":
    corner_store_talk = input("You grab a coke and some chips but have no money, Talk or run? ").lower()
    if corner_store_talk == "talk":
        if weapon == True:
            print("You approach the counter with your knife drawn. The man at the counter instantly shoots"
                  " you in the leg. Lose 25 health. ")
            health -=25
            print("You now have", health,"health")
        elif weapon == False:
            print("You approach the counter and tell the clerk you have no money, he sees you arent dangerous "
                  " and let's you have the snacks. ")
            print("Why did you choose such an unhealthy snack? Lose 25 health.")
            health -= 25
            print("You now have", health,"health")
    if corner_store_talk == "run":
            print("You run out of the store and enjoy your coke and chips. They are unhealthy as fuck"
                      " though, lose 25 health. ")
            health -= 25
            print("You now have", health,"health")

if health <= 0:
    print("Sorry, you died. ")
    quit()
else:
    ()

print("After leaving the corner store you see a man on top of a large building across the street. You decide"
      "to investigate")

rooftop = input("Upon reaching the rooftop you see a man in the corner overlooking the ledge. Talk or Fight").lower()
if rooftop == "talk":
    if weapon == True:
        print("You approach the man and ask what he's doing. He pulls a gun out of his pocket but you lunge with "
              "your knife.")
        print("A long fight ensues, you manage to do some damage but it isn't enough to finish him. ")
        print("The man on the roof was a legendary fighter named Brysten Angelo the Third. He beat you bad. "
              " Lose 50 health")
        health -=50
        print("You now have", health,"health.")
        if health <= 0:
            print("Sorry, you died. ")
            quit()
    if weapon == False:
        print("You approach the man and ask what he's doing. He pulls out a gun and shoots you. You are defenseless.")
        health -=150
        if health <= 0:
            print("Sorry, you died. ")
            quit()
if rooftop == "fight":
    if weapon == True:
        print("You approach the man and see he is armed with a weapon. You recognize him as the legendary "
              " fighter Brysten Angelo the Third. \n You quickly lunge with your knife and damage his jugular "
              " vein rendering him useless. He does some damage to you as well. Lose 25 Health. ")
        health -=25
        if health <= 0:
            print("Sorry you died")
            quit()
    if weapon == False:
        print("You approach the man and see he is armed with a weapon. You recognize him as the legendary "
              " fighter Brysten Angelo the Third. He shoots you in the neck. ")
        health -= 100
        if health <= 0:
            print("Sorry you died")
            quit()

if health >= 1:
    print("After the encounter with Brysten Angelo the Third on the rooftop he offers to teach you how to"
          " perfect the art of combat. You live a happy life. \nGood job surviving the game, please reach out to me"
          "at sognome@gmail.com to collect your prize! ")
    quit()










