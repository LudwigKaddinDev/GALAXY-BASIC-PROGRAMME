# This module will allow the USER to input the ship material cost.
# This module does not function. It was used to prototype the shipcost function.

from ROBLOX_Algorithm import MATS_NAME

def shipCost():
    
    ORES = 7
    v = int(0)

    while v < ORES:
        print("Press", v, "to edit the amount of", MATS_NAME[v], "the ship you want costs.")
        v += 1
    
    print()

    oreUpdate = getInteger("Make your selection: ")

    if oreUpdate < ORES:
        SHIP_VALUE[oreUpdate] = getInteger("Input the new value: ")
        print()
        updateAgain = getString("Do you with to update another value? (y/n) ")
        if updateAgain == 'y':
            cls()
            updateInventory()
        elif updateAgain == 'n':
            cls()
            coreFunction()
    else:
        print()
        print("Please make a valid selection.")
        timer = threading.Timer(2, cls)
        timer.start()
        timer2 = threading.Timer(2.1, updateInventory)
        timer2.start()
    
    return;
