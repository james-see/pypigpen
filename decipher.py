
# Author: James Campbell
# What: Deciphers text using pigpen plaintext standard cipher
# Requirements: Python 3.x and above

import json
import sys

with open('jsondata.json') as f:
    jsondict = json.loads(f.read())

# //// tests

# print(jsondict['a'])
pypigpen = """
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
                      
"""
print(pypigpen)
print('Welcome. \nThis will print plaintext to a text file called decipher.txt. \nUse cipher.py to encipher.\n')
if len(sys.argv) < 2:
    print('usage: python3 decipher.py [full path and name of text file to decipher]\n')
    exit()

with open(sys.argv[1],"r") as f:
    listofcipherwords = f.read().split()
    print(listofcipherwords[0])
    exit('working so far')
    for word in helloworld:
        # print("\n{}".format(letter))
        if letter == '.':
            print('\n')
            f.write('\n')
            continue
        letter = letter.lower()
        print(jsondict[letter]+" ", end="")
        f.write(jsondict[letter])
exit('\nthanks for playing')