import os
ARJO_REG_DATA = dict()
with open('ARJO_REG.arjo', 'r') as REGISTRY:
   REGISTRY2 = list(REGISTRY)
   ARJO_REG_DATA['osName'] = REGISTRY2[0]
   ARJO_REG_DATA['osCodename'] = REGISTRY2[1]
   ARJO_REG_DATA['version'] = REGISTRY2[2]
   ARJO_REG_DATA['lastStableVersion'] = REGISTRY2[3]
   ARJO_REG_DATA['yearCreated'] = REGISTRY2[4]
   ARJO_REG_DATA['monthCreated'] = REGISTRY2[5]
   ARJO_REG_DATA['dayCreated'] = REGISTRY2[6]

while True:
    command = input()
    if command == 'REGISTRY':
        os.system('cls')
        print('ARJO REGISTRY')
        print('=============')
        for i in ARJO_REG_DATA:
            print(i)
        print('=============')
        registry_loop = True
        while registry_loop == True:
            subcommand = input("Insert Registry Action: ")
            if subcommand == 'read':
                filter = input("Insert Registry Filename: ")
                if filter in ARJO_REG_DATA:
                    print(ARJO_REG_DATA[filter])
