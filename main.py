from random import randint
from pprint import pprint
from subprocess import call
from os import name
from time import sleep
def clear():
    # check and make call for specific operating system
    _ = call('clear' if name =='posix' else 'cls')



LargestNumber = int(input("what should be the Largest Numeber on the table : "))
def genHand(number, Face):
    hand =[]
    for x in range(number):
        hand.append(randint(1, Face))
    return(hand)
def printDoggo():
    Doggo =[
    """            /)-_-(\        /)-_-(\                    """,
    """             (o o)          (o o)                     """,
    """     .-----__/\o/            \o/\__-----.             """,
    """    /  __      /              \      __  \            """,
    """\__/\ /  \_\ |/                \| /_/  \ /\__/        """,
    """     \\     ||                  ||      \\            """,
    """     //     ||                  ||      //            """,
    """     |\     |\                  /|     /|         """]
    for x in Doggo:
        print(x)
def printCat():
    cat =[
    """  A_A                      A_A            """,
    """ (-.-)                    (-.-)           """,
    """  |-|                      |-|            """,
    """ /   \                    /   \           """,
    """|     |   __         __  |     |          """,
    """|  || |  |  \__   __/  | |  || |          """,
    """ \_||_/_/               \_\_||_/      """] 
    for x in cat:
        print(x)
def printBye():
    bye = [""" _                    """,
    """ | |                   """,
    """ | |__  _   _  ___     """,
    """ | '_ \| | | |/ _ \     """,
    """ | |_) | |_| |  __/    """,
    """ |_.__/ \__, |\___|    """,
    """        __/ |         """,
    """       |___/      """]
    for x in bye:
        print(x)
def printLove():
    Rose =[
    """              ...:::::::...        ...:::::::...                  """,                                                                                
    """           .:::::::::::::::::. .::::::::::::::::::.               """,                                                                                   
    """        .::::::::::::::::::::::::::::::::::::::::::::.            """,                                                                                      
    """      .:::::::::::::::::::'.-=.-~, ':::::::::::::::::::.          """,                                                                                        
    """    .:::::::::::::::::::' /{,_;--'},'::::::::::::::::::::.        """,                                                                                          
    """   .:::::::::::::::::::: |  .=~`|//| :::::::::::::::::::::.       """,                                                                                           
    """  .::::::::::::::::::::: | /   ; \ | :::' __, '::::::::::::.      """,                                                                                            
    """ .:::::::::::::::::::::' ||    | | | :' .' \/\  ::::::::::::.     """,                                                                                             
    """.:::::::::::::::::::::: |\|    | | |\  / \ /_|  :::::::::::::.    """,                                                                                              
    """::::::::::::::::::::::. \ |  | /|'/ / | \ /_ |  ::::::::::::::    """,                                                                                              
    """::::::::::::::' ,_ '::: `\ \/|/ / /`.: \ /__/  :::::::::::::::    """,                                                                                              
    """:::::::::::::  /\/`'. ':. `\ `./.'/\ : /.--' .::::::::::::::::    """,                                                     
    """:::::::::::::  |_\ / \  ::. '. ,/|\/| //  ''''':::::::::::::::    """,                                                     
    """:::::::::::::  | _\ / | .::  | | \ \///  .""'-.  :::::::::::::    """,                                                     
    """::::::::::::::  \__\ / .: .'/| |  `)`/__//_/_/_\  ::::::::::::    """,                                                     
    """'::::::::::::::  '--.\ : /\/_| |} /.---. \ \ \ /  :::::::::::'    """,                                                     
    """ '::::::::::::''     \\ |\/_/| | //`  . `'...-'  :::::::::::'     """,                                                    
    """  ::::::::::  .-""'.  \\\/ /{| |//  .:::::....::::::::::::::      """,                                                   
    """   ':::::::  /_\_\_\\__\`(`  | '/  :::::::::::::::::::::::'       """,                                                  
    """    '::::::  \ / / / .---.\  | |  :::::::::::::::::::::::'        """,                                                 
    """     '::::::. '-..,'` .:.`\\ | |} ::::::::::::::::::::::'         """,                                                
    """       '::::::......:::::: \\| |  ::::::::::::::::::::'           """,                                              
    """        ':::::::::::::::::: \` |  ::::::::::::::::::'             """,                                            
    """          '::::::::::::::::  | |  ::::::::::::::::'               """,                                          
    """            ':::::::::::::: {| |  ::::::::::::::'                 """,                                        
    """              '::::::::::::  | |  ::::::::::::'                   """,                                      
    """                '::::::::::  | |  ::::::::::'                     """,                                    
    """                  '::::::::  | |} ::::::::'                       """,                                  
    """                    '::::::  | |  ::::::'                         """,                                
    """                     ':::::. |/  ::::::'                          """,                               
    """                       ':::.....:::::'                            """,                             
    """                         ':::::::::'                              """,                           
    """                           ':::::'                                """,                         
    """                             ':'                                  """]   
    print('To Ms Rose, who I miss very much.')   
    for x in Rose:
        print(x)
def printDoggo():
    
    Doggo =[
    """            /)-_-(\        /)-_-(\                       """, 
    """             (o o)          (o o)                        """,
    """     .-----__/\o/            \o/\__-----.                """,        
    """    /  __      /              \      __  \               """,         
    """\__/\ /  \_\ |/                \| /_/  \ /\__/           """,             
    """     \\     ||                  ||      \\               """,         
    """     //     ||                  ||      //               """,         
    """     |\     |\                  /|     /|            """]
    for x in Doggo:
        print(x)
def checkIfWinRound(your_hand, HisHand, Number):
    TheHands = your_hand + HisHand
    NumberOneTheTable = TheHands.count(p[0])
    print(f'Number On The Table Is: {NumberOneTheTable} \nThe Number You Guessed is: {p[1]}')

    if NumberOneTheTable > p[1]:
        clear()
        print('You got it right, you get a cat ')
        print('\n')
        del HisHand[0]
        HisHand = genHand(len(HisHand), LargestNumber)
        your_hand = genHand(len(your_hand), LargestNumber)
        print('\n')
        printCat()
        sleep(1.5)
    else:
        clear()
        print('You didnt get it right, have a dog')
        print('\n')
        printDoggo()
        del your_hand[0]
        HisHand = genHand(len(HisHand), LargestNumber)
        your_hand = genHand(len(your_hand), LargestNumber)
        sleep(1.5)
    return your_hand, HisHand
    
    
    
    
    
#SetupGame
number = int(input('How many Starting Dice?: '))
clear()

Player1Hand = genHand(number, LargestNumber)
Player2Hand = genHand(number, LargestNumber)



breaker = True
while breaker:
    
    
    
    
    
    
    if len(Player1Hand) > 0 and len(Player2Hand) == 0:
        print('did it')
        break
        
        
        
    elif len(Player1Hand) == 0 and len(Player2Hand) > 0:
        print('you suck at life and you should go die')
        break
    else:
        pass
        
        
        
    for x in range(len(Player1Hand)):
        print( f'SwindleStone {x + 1}: {Player1Hand[x]}')


    print(f'Count Of His Hand: {len(Player2Hand)}')
    p = [int(input(f'Number on the dice (1 - {LargestNumber}): ')), int(input('Ammount on the table: '))]
    
    
    
    
    
    if str(p).lower() == str(['EXIT'.lower()]):
        clear()
        print(bye)
        sleep(1)
        breaker = False
        break
        
        
        
        
        
    Caller = input('Do you wanna call em Y/n : ').lower()
    if Caller == 'y':
        Player1Hand, Player2Hand = checkIfWinRound(Player1Hand, Player2Hand, p)
    else:        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    clear()
