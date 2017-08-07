
# Author: James Campbell
# What: Deciphers text using pigpen plaintext standard cipher
# Requirements: Python 3.x and above

import json
import sys


def get_file(filename):
with open(filename) as f:
    jsondict = json.loads(f.read())
    return jsondict

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

jsondict = get_file('jsondata.json')

with open('decipher.txt','w') as d:
    with open(sys.argv[1],"r") as f:
        listofcipherletters = f.read().split()
        # tests
        # print(listofcipherletters)
        #exit('working so far')
        for letter in listofcipherletters:
            # print("\n{}".format(letter))
            if letter == '\n':
                print('\n')
                d.write('\n')
                continue
            name = [alphabet for alphabet, cipher in jsondict.items() if cipher == letter]
            print(''.join(name),end="")
            writeable = str(''.join(name))
            d.write(writeable)
exit('\nthanks for playing\nsaved as decipher.txt')