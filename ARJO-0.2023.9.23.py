#Arjo Setup File Header
print("ARJO SHELL")
print("SETUP: 0.2023.9.23")

#Registry Setup
try:
    with open("ARJO_REGISTRY.txt", 'w') as ARJO_REGISTRY:
        ARJO_REGISTRY.write("ARJO SHELL\n") #OS NAME
        ARJO_REGISTRY.write('"CODENAME ARJO SHELL"\n') #OS CODENAME
        ARJO_REGISTRY.write("0.2023.9.23\n") #VERSION STRING
        ARJO_REGISTRY.write("0\n") #LAST_STABLE_VERSION
        ARJO_REGISTRY.write("2023\n") #YEAR OF CREATION
        ARJO_REGISTRY.write("9\n") #MONTH OF CREATION
        ARJO_REGISTRY.write("23\n") #DAY(S) OF CREATION
        ARJO_REGISTRY.close()
    print("\nREGISTRY HAS COMPLETED SUCCESSFULLY")
except Exception as error:
    print("\nFATAL ERROR - REGISTRY SETUP FAILED (0x001)")
    print("ADDITIONAL INFORMATION:\n>", error)
    exit()

#Arjo Setup (REGISTRY)
try:
    registry_bind = []
    with open("ARJO_REGISTRY.txt", 'r') as ARJO_REGISTRY:
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
