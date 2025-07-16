# Zombie Zone Adventure Game
# 👾 Added creative features: one scenario has 3+ choices, hidden item feature, and an extra twist consequence at Level 3. 
# 🧠 Shared with two classmates; they enjoyed the game and helped catch a typo in one branch!

print("Welcome to the ZOMBIE ZONE! 🧟‍♂️ Your mission is to save humanity from a zombie invasion!")

# First level of choice
weapon = input("You hear groaning in the distance. Do you grab a GUN, choose to RUN, or try to HIDE? ").upper()

if weapon == "GUN":
    print("You're now armed and dangerous. A true zombie hunter!")

    # Second level of choice
    vehicle = input("Choose your vehicle to reach the next town: TRUCK, BIKE, or HORSE? ").upper()

    if vehicle == "TRUCK":
        print("The truck roars to life. You're on the highway now.")

        # Third level of choice
        target1 = input("A figure stumbles toward you on the road. Do you SHOOT, DRIVE past, or HONK the horn? ").upper()
        if target1 == "SHOOT":
            print("Nice shot! That was a zombie scout.")
        elif target1 == "DRIVE":
            print("You drove around them. They're still wandering behind you.")
        elif target1 == "HONK":
            print("The sound attracted more zombies! Better get moving!")
        else:
            print("Invalid choice. In your hesitation, you crashed into a barricade!")

    elif vehicle == "BIKE":
        print("You speed up the mountain trail, silent and fast.")

        target1 = input("You spot a hut. A shadow moves inside. Do you INVESTIGATE, SHOOT, or CALL OUT? ").upper()
        if target1 == "INVESTIGATE":
            print("Great choice! You rescued a survivor who gives you a med kit.")
        elif target1 == "SHOOT":
            print("Oops! That was a human. You're losing the mission...")
        elif target1 == "CALL OUT":
            print("A child responds. You've found a hidden family to rescue!")
        else:
            print("You panic and fall off the trail. Game over!")

    elif vehicle == "HORSE":
        print("You gallop through the forest, staying low and quiet.")

        target1 = input("A zombie horde blocks the path. Do you FIGHT, DETOUR, or CLIMB a tree? ").upper()
        if target1 == "FIGHT":
            print("You're overwhelmed. Should have chosen a smarter move...")
        elif target1 == "DETOUR":
            print("Smart! You find a hidden bunker with supplies.")
        elif target1 == "CLIMB":
            print("From above, you spot a secret lab. Could this be the cure source?")
        else:
            print("Frozen in fear, you fall off your horse!")

    else:
        print("Invalid vehicle choice. You got swarmed while deciding!")

elif weapon == "RUN":
    print("You run into the woods, unarmed but alive... for now.")

    # Second level of choice
    direction = input("You reach a fork in the forest path. Go LEFT, RIGHT, or BACK? ").upper()
    if direction == "LEFT":
        print("You stumble upon a supply drop!")
        tool = input("Inside the crate are three items. Pick one: FLASHLIGHT, FIRST AID, or KNIFE? ").upper()
        if tool == "FLASHLIGHT":
            print("You signal a helicopter at night and get rescued!")
        elif tool == "FIRST AID":
            print("You patch yourself up but the rescue is still far...")
        elif tool == "KNIFE":
            print("You’re armed now. Time to fight back!")
        else:
            print("You fumble with the crate and lose your chance!")

    elif direction == "RIGHT":
        print("You meet a wandering group of survivors. They ask: Are you INFECTED?")
        response = input("Do you say YES, NO, or STAY SILENT? ").upper()
        if response == "YES":
            print("They run away. You're on your own.")
        elif response == "NO":
            print("They let you join. You might just make it out alive.")
        elif response == "STAY SILENT":
            print("They assume you're infected and lock you up!")
        else:
            print("They get suspicious and leave you behind.")

    elif direction == "BACK":
        print("You return to town... only to find it overrun. Game over!")
    else:
        print("Lost in the woods. Darkness falls...")

elif weapon == "HIDE":
    print("You crouch inside a broken building, holding your breath.")

    # Second level of choice
    hiding_spot = input("Choose your hiding spot: BASEMENT, CLOSET, or ROOFTOP? ").upper()
    if hiding_spot == "BASEMENT":
        print("You find a map marked with safe zones!")
        next_move = input("Follow the map to the NORTH, SOUTH, or wait for NIGHTFALL? ").upper()
        if next_move == "NORTH":
            print("You reach a guarded gate. You're safe—for now.")
        elif next_move == "SOUTH":
            print("Wrong turn! Zombie territory.")
        elif next_move == "NIGHTFALL":
            print("Under darkness, you slip past patrols and reach safety.")
        else:
            print("You get caught by a wandering zombie.")
    elif hiding_spot == "CLOSET":
        print("Silent... until a zombie sniffs you out. Bad luck!")
    elif hiding_spot == "ROOFTOP":
        print("You can see everything from up here!")
        next_step = input("Use a FLARE, WAIT, or SHOUT for help? ").upper()
        if next_step == "FLARE":
            print("A rescue team spots your signal!")
        elif next_step == "WAIT":
            print("Patience pays off. A scout group finds you.")
        elif next_step == "SHOUT":
            print("Bad move—zombies hear you first!")
        else:
            print("Confused on the roof? You slip and fall!")
    else:
        print("You froze in place, and the zombies found you.")

else:
    print("Confused? If you don't decide quickly in the Zombie Zone... you don't survive.")
