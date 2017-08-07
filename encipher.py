# Author: James Campbell
# What: Encrypts text using pigpen cipher
# Requirements: Python 3.x and above

import json
from colorama import Fore, Back, Style

with open('jsondata.json') as f:
    jsondict = json.loads(f.read())

# //// tests

# print(jsondict['a'])
pypigpen = """
------------------------------------
PYPIGPEN
------------------------------------
                  ,.
                 (_|,.
                ,' /, )_______   _
             __j o``-'        `.'-)'
            (")                 \\'
             `-j                |
               `-._(           /
                  |_\  |--^.  /
                 /_]'|_| /_)_/
                    /_]'  /_]'
                      
------------------------------------
"""
print(pypigpen)
print(Fore.CYAN+'Welcome.')
print(Fore.YELLOW+'\nThis will print a cipher to a text file called cipher.txt. \nUse decipher.py to reverse.\n'+Fore.RESET)
helloworld = input("What do you want to encipher? (use . for new line):\n")

# get ready for output
# clear
import os
os.system('cls' if os.name == 'nt' else 'clear')
# start output here
print('Output:\n')

with open('./cipher.txt',"w") as f:
    for letter in helloworld:
        # print("\n{}".format(letter))
        if letter == '.':
            print('\n')
            f.write('\n')
            continue
        letter = letter.lower()
        print(jsondict[letter], end="")
        f.write(jsondict[letter]+' ')
exit('\nthanks for playing\nsaved as cipher.txt\n')