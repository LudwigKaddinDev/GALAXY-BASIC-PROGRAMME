# This programme is for the ROBLOX game of GALAXY. 
# It can be used to calculate how many materials you still need for a new ship, based on USER input. 
# You can also use it to keep track of your materials mined (and skip ship cost calculation all together). 

global info
info = [["This programme is for the ROBLOX game of GALAXY"], # 0
        ["It can be used to calculate how many materials you still need for a new ship, based on USER input.", ], # 1
        ["You can also use it to keep track of your materials mined (and skip ship cost calculation all together)."], # 2
        ["CREDITS: LudwigKaddin, Pieter Spronck (for pcinput module)"]] # 3

import os
from pcinput import getString, getInteger
import csv
import threading

# List of MATERIALS (raw ores):
# Name of the ores in string values are ORENAME_NAME variables.

COST_ENABLED = True
TOGGLE = 0
ENTERED_VALUE = False
#firstTime = 0

global SILICATE
global SILICATE_NAME
global CARBON
global CARBON_NAME
global IRIDIUM
global IRIDIUM_NAME
global ADAMANTITE
global ADAMANTITE_NAME
global PALLADIUM
global PALLADIUM_NAME
global TITANIUM
global TITANIUM_NAME
global QUANTIUM
global QUANTIUM_NAME

SILICATE = 0
CARBON = 0
IRIDIUM = 0
ADAMANTITE = 0
PALLADIUM = 0
TITANIUM = 0
QUANTIUM = 0

SILICATE_NAME = "Silicate"
CARBON_NAME = "Carbon"
IRIDIUM_NAME = "Iridium"
ADAMANTITE_NAME = "Adamantite"
PALLADIUM_NAME = "Palladium"
TITANIUM_NAME = "Titanium"
QUANTIUM_NAME = "Quantium"

MATS_NAME = [SILICATE_NAME, CARBON_NAME, IRIDIUM_NAME, ADAMANTITE_NAME, PALLADIUM_NAME, TITANIUM_NAME, QUANTIUM_NAME]
MATS_VALUE = [SILICATE, CARBON, IRIDIUM, ADAMANTITE, PALLADIUM, TITANIUM, QUANTIUM]

SHIP_VALUE = list(MATS_VALUE)



print("The names of the current known materials are:", MATS_NAME)
print()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def coreFunction():      

    loadData()

    global SHIP_VALUE
    global COST_ENABLED
    global TOGGLE
    global ENTERED_VALUE

    ORES = 7
    v = int(0)

    print("You currently own: ")
    print()
    while v < ORES:
        print(MATS_NAME[v], MATS_VALUE[v])
        v += 1
    
    print()

    if COST_ENABLED == True and ENTERED_VALUE == True:

        x = int(0)

        if ENTERED_VALUE == True:
            print("The ship you want costs:")
            print()
            while x < ORES:
                print(MATS_NAME[x], SHIP_VALUE[x])
                x += 1

        print()

        y = int(0)

        if ENTERED_VALUE == True:
            print("You still need:")
            print()
            while y < ORES:
                if int(SHIP_VALUE[(y)]) - int(MATS_VALUE[y]) <= 0:
                    print(MATS_NAME[y], "0")
                    y += 1
                else:
                    print(MATS_NAME[y], int(SHIP_VALUE[y]) - int(MATS_VALUE[y]))
                    y += 1
        print()    

    print("Press 'u' to update materials mined.")
    print("Press 'x' to exit out of the program.")
    if COST_ENABLED == True:
         print("Press 'c' to set a shipcost.")
    print("Press 'h' to see what this program is meant for.")
    print("Press 'f' to enable/disable ship cost calculation.")
    print()
    print("Press 'r' to reset your inventory.")
    print()

    selection = getString("Please make your selection now: ")

    if selection == 'u':
        cls()
        updateInventory()
    elif selection == 'x':
        print()
        saveData()
        SystemExit()
    elif selection == 'h':
        cls()
        x = int(0)
        l = 4
        while x < l:
            print(info[x])
            #if x == 3:
                #print()
                #print(info[x])
            x += 1
        print()
        coreLoop = input("Press Enter to continue.")
        if coreLoop == "":
            cls()
            coreFunction()
        elif coreLoop != "":
            cls()
            coreFunction()
    elif selection == 'c':
        if COST_ENABLED == True:
           cls()
           shipCost()
        else:
            print("You have disabled this feature.")
            timer5 = threading.Timer(2, cls)
            timer5.start()
            timer6 = threading.Timer(2.1, coreFunction)
            timer6.start()
    elif selection == 'f':
        if TOGGLE == 0:
            COST_ENABLED = False
            print("Ship cost calculation is now disabled.")
            timer3 = threading.Timer(2, cls)
            timer3.start()
            timer4 = threading.Timer(2.1, coreFunction)
            timer4.start()
            TOGGLE = 1
        elif TOGGLE == 1:
            COST_ENABLED = True
            print("Ship cost calculation is now enabled.")
            timer10 = threading.Timer(2, cls)
            timer10.start()
            timer11 = threading.Timer(2.1, coreFunction)
            timer11.start()
            TOGGLE = 0
    elif selection == 'r':
        listlength = len(MATS_VALUE)
        for i in range(listlength):
            MATS_VALUE[i] = 0
            SHIP_VALUE[i] = 0
        print()
        print("All data has been reset.")
        ENTERED_VALUE = False
        saveData()
        timer100 = threading.Timer(2, cls)
        timer100.start()
        timer110 = threading.Timer(2.1, coreFunction)
        timer110.start()
    else:
        print()
        print("Please make a valid selection.")
        timer = threading.Timer(2, cls)
        timer.start()
        timer2 = threading.Timer(2.1, coreFunction)
        timer2.start()

    return;

def updateInventory():
    
    ORES = 7
    v = int(0)

    while v < ORES:
        print("Press", v, "to edit the amount of", MATS_NAME[v], "you currently own.")
        v += 1
    
    print("Press", ORES, "to go back to the main menu.")
    print()

    print("You currently own: ")
    print()

    m = int(0)

    while m < ORES:
        print(MATS_NAME[m], MATS_VALUE[m])
        m += 1
    print()

    oreUpdate = getInteger("Make your selection: ")

    if oreUpdate < ORES:
        MATS_VALUE[oreUpdate] = getInteger("Input the new value: ")
        saveData()
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
    elif oreUpdate == ORES:
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

def shipCost():
    
    global ENTERED_VALUE

    ORES = 7
    v = int(0)

    while v < ORES:
        print("Press", v, "to edit the amount of", MATS_NAME[v], "the ship you want costs.")
        v += 1

    print("Press", ORES, "to go back to the main menu.")
    print()

    print("You current ship costs are: ")
    print()
    m = int(0)

    while m < ORES:
        print(MATS_NAME[m], SHIP_VALUE[m])
        m += 1
    print()

    print()

    oreUpdate = getInteger("Make your selection: ")

    if oreUpdate < ORES:
        SHIP_VALUE[oreUpdate] = getInteger("Input the new value: ")
        ENTERED_VALUE = True
        saveData()
        print()
        updateAgain = getString("Do you with to update another value? (y/n) ")
        if updateAgain == 'y':
            cls()
            shipCost()
        elif updateAgain == 'n':
            cls()
            coreFunction()
        else:
            print()
            print("Please make a valid selection.")
            timer = threading.Timer(2, cls)
            timer.start()
            timer2 = threading.Timer(2.1, shipCost)
            timer2.start()
    elif oreUpdate == ORES:
        cls()
        coreFunction()
    else:
        print()
        print("Please make a valid selection.")
        timer = threading.Timer(2, cls)
        timer.start()
        timer2 = threading.Timer(2.1, shipCost)
        timer2.start()
    
    return;


def saveData():

    with open("output_data.csv", "w", newline="") as out_file:
            data_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(MATS_NAME)):
                data_writer.writerow([str(MATS_NAME[i]), str(MATS_VALUE[i]) ])
    
    with open("shipcost_data.csv", "w", newline="") as out_file2:
            data_writer2 = csv.writer(out_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(MATS_NAME)):
                data_writer2.writerow([str(MATS_NAME[i]), str(SHIP_VALUE[i]) ])

    return;

def loadData():
    
    global ENTERED_VALUE

    with open("output_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        z = 0
        for row in csv_reader:
            MATS_VALUE[z] = row[1]
            z += 1

    with open("shipcost_data.csv") as csv_file3:
        csv_reader3 = csv.reader(csv_file3, delimiter=',')
        b = 0
        for row2 in csv_reader3:
            SHIP_VALUE[b] = row2[1]
            b += 1
            if int(row2[1]) > 0:
                ENTERED_VALUE = True
    return;

print()

coreFunction()