"""
Author: Vimagh Solomon
Purpose: Week 3 Assignment

"""

# Additional creativity: one of the scenario has more than 3 choices. 
# The game was shared with a friend and they enjoyed it.

print("Welcome to the Zombi zone! Your mission here is to save humans frorm Zombi invasion")

#First level of choices
weapon = input("What would you like to do, pick a GUN, RUN or HIDE? ").upper()
if weapon == "GUN":

    print("You are now ready Zombi humter!.")

#Second level of choice
    vehicle = input("What kind of vehicle would you prefer? TRUCK,BIKE or WALK ").upper()

    if vehicle == "TRUCK":

        print("Take the Highway to the left.")

#Third level of choice
        target1 = input("You sight a stranger walking on the highway. What do you do? SHOOT,DRIVE or CRASH the stranger?").upper()

        if target1 == "SHOOT":

            print("Good job Zombi hunter!. You just got your first target.")

        elif target1 =="DRIVE":

            print("Oops! You just missed your first target.")

        elif target1 =="CRASH":

            print("Hmm He is about to get back up with a rage. Keep moving.")

        else:

            print("Invalid move, there is no way forward.")


    elif vehicle == "BIKE":

        print("Follow the mountain trail to the right.")

        target1 = input("You see a hut and you can see someone hidden in it. SHOOT, INVESTIGATE or CALL-OUT? ").upper()

        if target1 == "INVESTIGATE":

            print("Welldone! You just rescued the first human")

        elif target1 == "SHOOT":

            print("Oh man! that was a wrong target.")

        elif target1 == "CALL-OUT":
            print("A child responds. You've found a hidden family to rescue!")

        else:

            print("You panic and crash the bike. Game over!")

    elif vehicle == "FOOT":
        print("You walk quietly through the forest.")

        target1 = input("You see a Zombi on the  path, what do you do? FIGHT,CLIMB A TREE or CHANGE PATH?").upper()
        if target1 == "FIGHT":
            print("You are getting weak. You coud be defeated.")

        elif target1 == "CLIMB":
            print("You sight the cure lab you heard about in a distance.")

        elif target1 == "CHANGE":
            print("You see a bunker where you can get some rest.")
        else:
            print("You froze and got bitten by the Zombie")
    else:
        print("Inalid choice. You got bitten by a Zombie while looking for a vehicle to use.")


elif weapon == "RUN":

    print("Come on Hunter! you can do this.")

    direction = input("You reach a fork road, you go LEFT, RIGHT or BACK").upper()

    if direction == "LEFT":

        print("You stumble on a bag with tools with 3 items")

        tools = input("YOu pick one tool: FLASHLIGHT, JACKET, DAGGER").upper()

        if tools == "FLASHLIGHT":

            print("You can find your way at night to the lab, zombies dont move at night.")

        elif tools == "JACKET":

            print("Keep warm, there is still a long way to go.")

        elif tools == "KNIFE":
            print("You now have more weapons hunter! ")

        else:
            print("you missed a chance with that tool bag.")

    elif direction == "RIGHT":
        print("You see a family walking, they ask if You are a Zombie")
        
        response = input("What is your response? , YES, NO, SILENCE").upper()
        
        if response == "YES":
            print("They run from you")

        elif response == "NO":
            print("They invite you to walk to the lab with them.")

        elif response == "SILENCE":
            print("They become suspicious and run")

        else: 
            print("They assume you are a Zombie and lock you up.")

    elif direction == "BACK":
        print("You return and get swamped by Zombies. Game Over.")

    else: 
        print("Dead end, Gameover.")

elif weapon == "HIDE":
    print("You hide in an abandonned house")

    hiding = input("You Hide in the BASEMENT, ROOM, ROOFTOP").upper()

    if hiding == "BASEMENT":
        print("You see an invisible jacket to help you get to the lab.")

        next_move = input("Walk NORTH, SOUTH, or wait for NIGHTFALL? ").upper()
        if next_move == "NORTH":
            print("You reach a guarded gate. You're safe—for now.")
        elif next_move == "SOUTH":
            print("Wrong turn! Zombie territory.")
        elif next_move == "NIGHTFALL":
            print("Under darkness, zombies are weak and you reach safety.")
        else:
            print("You get caught by a rare night walking zombie.")
    elif hiding == "ROOM":
        print("Silent... until a zombie sniffs you out. Bad luck!")
    elif hiding == "ROOFTOP":
        print("You can see everything from up here!")
        next_step = input("Use a FLARE, WAIT, or SHOUT for help? ").upper()
        if next_step == "FLARE":
            print("A rescue team spots your signal!")
        elif next_step == "WAIT":
            print("Patience pays off. A scout group finds you.")
        elif next_step == "SHOUT":
            print("Bad move—zombies hear you first!")
        else:
            print("You slip and fall!")
    else:
        print("You froze in place, and the zombies found you.")

else:
    print("Confused? If you don't decide quickly in the Zombie Zone... you don't survive.")