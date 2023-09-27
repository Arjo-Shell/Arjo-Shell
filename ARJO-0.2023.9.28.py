import os

# All registry data
ARJO_REG_DATA = {
    "osName": "ARJO SHELL",
    "osCodename": "APPLESEED",
    "version": "0.2023.9.28",
    "lastStableVersion": "0",
    "yearCreated": "2023",
    "monthCreated": "9",
    "dayCreated": "28",
}

#Creating the File
ARJO_REG_LIST = [
    ARJO_REG_DATA["osName"], 
    ARJO_REG_DATA["osCodename"], 
    ARJO_REG_DATA["version"], 
    ARJO_REG_DATA["lastStableVersion"], 
    ARJO_REG_DATA["yearCreated"], 
    ARJO_REG_DATA["monthCreated"], 
    ARJO_REG_DATA["dayCreated"]
]

# Name of the registry filename
REG_FILENAME = "ARJO_REG.arjo"

#Arjo Setup File Header
print(ARJO_REG_DATA["osName"])
print(f"SETUP FOR: {ARJO_REG_DATA['version']}")

#Registry Setup
try:
    with open(f"{REG_FILENAME}", 'w') as ARJO_REGISTRY:
        for i in ARJO_REG_LIST:
            ARJO_REGISTRY.write(i)
            ARJO_REGISTRY.write("\n")
    print("\nREGISTRY HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("\nFATAL ERROR - REGISTRY SETUP FAILED (0x001)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()

#Arjo Setup (REGISTRY)
try:
    registry_bind = []
    with open(f"{REG_FILENAME}", 'r') as ARJO_REGISTRY:
        with open("ARJO.py", 'w') as ARJO:
            ARJO_LISTNAME = list(ARJO_REG_DATA.keys())
            ARJO.write("import os\n")
            ARJO.write("ARJO_REG_DATA = dict()\n")
            ARJO.write(f"with open('{REG_FILENAME}', 'r') as REGISTRY:\n")
            ARJO.write(f"   REGISTRY2 = list(REGISTRY)\n")
            pos = 0
            for r in ARJO_LISTNAME:
                ARJO.write(f"   ARJO_REG_DATA['{r}'] = REGISTRY2[{pos}]\n")
                pos += 1
            ARJO.write("\n")
            print("REGISTRY BINDING HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("FATAL ERROR - REGISTRY BINDING ERROR (0x002)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()

if os.name == 'nt':
    os.system(f"attrib +h {REG_FILENAME}")

#Arjo Setup (COMMANDS)
try:
    with open("ARJO.py", 'a') as ARJO:
        #Operating System Code
        ARJO.write("while True:\n")
        ARJO.write("    command = input()\n")
        ARJO.write("    if command == 'REGISTRY':\n")
        ARJO.write("        os.system('cls')\n")
        ARJO.write("        print('ARJO REGISTRY')\n")
        ARJO.write("        print('=============')\n")
        ARJO.write("        for i in ARJO_REG_DATA:\n")
        ARJO.write("            print(i)\n")
        ARJO.write("        print('=============')\n")
        ARJO.write("        registry_loop = True\n")
        ARJO.write("        while registry_loop == True:\n")
        ARJO.write("            subcommand = input('Insert Registry Action: ')\n")
        ARJO.write("            if subcommand == 'read':\n")
        ARJO.write("                filter = input('Insert Registry Object: ')\n")
        ARJO.write("                if filter in ARJO_REG_DATA:\n")
        ARJO.write("                    print(ARJO_REG_DATA[filter])\n")
        ARJO.write("            elif subcommand == 'save':\n")
        ARJO.write(f"                os.remove('{REG_FILENAME}')\n")
        ARJO.write(f"                with open('{REG_FILENAME}', 'w') as EXTERNAL_REGISTRY:\n")
        ARJO.write(f"                    for i in ARJO_REG_DATA:\n")
        ARJO.write(f"                        EXTERNAL_REGISTRY.write(ARJO_REG_DATA[i])\n")
        ARJO.write(f"                    if os.name == 'nt':\n")
        ARJO.write(f"                        os.system(f'attrib +h {REG_FILENAME}')\n")
        ARJO.write("            elif subcommand == 'edit':\n")
        ARJO.write("                filter = input('Insert Registry Object to Edit: ')\n")
        ARJO.write("                if filter in ARJO_REG_DATA:\n")
        ARJO.write("                    for i in ARJO_REG_DATA:\n")
        ARJO.write("                        if i == filter:\n")
        ARJO.write("                            ARJO_REG_DATA[i] = input('Insert New Data: ')\n")
        ARJO.write("                            ARJO_REG_DATA[i] += '\\n'")
except Exception as error:
    print("\nUNKNOWN ERROR")
    print("INFORMATION:\n", error)


