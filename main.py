# All registry data
ARJO_REG_DATA = {
    "osName": "ARJO SHELL",
    "osCodename": "CODENAME ARJO SHELL",
    "version": "0.23.9.23.1",
    "lastStableVersion": "0",
    "yearCreated": "2023",
    "monthCreated": "9",
    "dayCreated": "23.1",
}

# Name of the registry filename
REG_FILENAME = "ARJO_REG.arjo"

#Arjo Setup File Header
print(ARJO_REG_DATA["osName"])
print(f"SETUP FOR: {ARJO_REG_DATA['version']}")

#Registry Setup
try:
    with open(REG_FILENAME, 'w') as ARJO_REGISTRY:
        for i in ARJO_REG_DATA:
            ARJO_REGISTRY.write(ARJO_REG_DATA[i])
            ARJO_REGISTRY.write("\n")
    print("\nREGISTRY HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("\nFATAL ERROR - REGISTRY SETUP FAILED (0x001)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()

#Arjo Setup (REGISTRY)
try:
    registry_bind = []
    with open(REG_FILENAME, 'r') as ARJO_REGISTRY:
        with open("ARJO.py", 'w') as ARJO:
            for i in ARJO_REGISTRY:
                i = list(i)
                del i[-1]
                j = ""
                for item in i:
                    for subitem in item:
                        j += subitem
                i = j
                registry_bind.append(i)
            ARJO.write("RAW_REGISTRY = [")
            for i in registry_bind:
                if i != registry_bind[-1]:
                    ARJO.write(f"'{i}'")
                    ARJO.write(",")
                else:
                    ARJO.write(f"'{i}'")
            ARJO.write("]")
            ARJO.write("\nprint(RAW_REGISTRY)")
            print("REGISTRY BINDING HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("FATAL ERROR - REGISTRY BINDING ERROR (0x002)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()
