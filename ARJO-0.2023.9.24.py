import os
from os.path import expanduser

# All registry data
ARJO_REG_DATA = {
    "osName": "ARJO SHELL",
    "osCodename": "CODENAME ARJO SHELL",
    "version": "0.2023.9.24",
    "lastStableVersion": "0",
    "yearCreated": "2023",
    "monthCreated": "9",
    "dayCreated": "24",
}

ARJO_REG_LIST = ["ARJO SHELL", "CODENAME ARJO SHELL", "0.2023.9.24", "0", "2023", "9", "24"]

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
            ARJO.write("print(ARJO_REG_DATA)")
            print("REGISTRY BINDING HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("FATAL ERROR - REGISTRY BINDING ERROR (0x002)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()


if os.name == 'nt':
    os.system(f"attrib +h {expanduser('~')}\{REG_FILENAME}")
