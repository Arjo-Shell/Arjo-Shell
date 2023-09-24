import os
from os.path import expanduser

# All registry data
ARJO_REG_DATA = {
    "osName": "ARJO SHELL",
    "osCodename": "CODENAME ARJO SHELL",
    "version": "0.2023.9.24.1",
    "lastStableVersion": "0",
    "yearCreated": "2023",
    "monthCreated": "9",
    "dayCreated": "24.1",
}

ARJO_REG_LIST = [ARJO_REG_DATA["osName"], ARJO_REG_DATA["osCodename"], ARJO_REG_DATA["version"], ARJO_REG_DATA["lastStableVersion"], ARJO_REG_DATA["yearCreated"], ARJO_REG_DATA["monthCreated"], ARJO_REG_DATA["dayCreated"]]

# Name of the registry filename
REG_FILENAME = "ARJO_REG.arjo"

#Arjo Setup File Header
print(ARJO_REG_DATA["osName"])
print(f"SETUP FOR: {ARJO_REG_DATA['version']}")

#Registry Setup
try:
    with open(f"{expanduser('~')}\{REG_FILENAME}", 'w') as ARJO_REGISTRY:
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
    with open(f"{expanduser('~')}\{REG_FILENAME}", 'r') as ARJO_REGISTRY:
        with open("ARJO.py", 'w') as ARJO:
            ARJO.write("ARJO_REG_DATA = {\n")
            for i in ARJO_REG_DATA:
                ARJO_REG_DATA_I = ARJO_REG_DATA[i]
                if ARJO_REG_DATA[i] != ARJO_REG_LIST[-1]:
                    ARJO.write(f"   '{i}': '{ARJO_REG_DATA_I}',\n")
                else:
                    ARJO.write(f"   '{i}': '{ARJO_REG_DATA_I}'\n")
            ARJO.write("}\n")
            print("REGISTRY BINDING HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("FATAL ERROR - REGISTRY BINDING ERROR (0x002)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()

if os.name == 'nt':
    os.system(f"attrib +h {expanduser('~')}\{REG_FILENAME}")

#Arjo Setup (COMMANDS)
try:
    with open("ARJO.py", 'a') as ARJO:
        ARJO.write("import os\n")
        ARJO.write("from os.path import expanduser\n")
        ARJO.write("while True:\n")
        ARJO.write("    command = input()\n")
        ARJO.write("    if command == 'REGISTRY':\n")
        ARJO.write("        os.system('cls')\n")
        ARJO.write("        print('ARJO REGISTRY')\n")
        ARJO.write("        print('=============')\n")
        ARJO.write("        for i in ARJO_REG_DATA:\n")
        ARJO.write("            print(i)\n")
        ARJO.write("        print('=============')\n")
except Exception as error:
    print("\nUNKNOWN ERROR")
    print("INFORMATION:\n", error)


