[![Build Status](https://travis-ci.org/jamesacampbell/pypigpen.svg?branch=master)](https://travis-ci.org/jamesacampbell/pypigpen)
```
                      ,.
                     (_|,.
                    ,' /, )_______   _
                 __j o``-'        `.'-)'
                (")                 \'
                 `-j                |
                   `-._(           /
                      |_\  |--^.  /
                     /_]'|_| /_)_/
                        /_]'  /_]'
                      
```

This script uses the pigpen plaintext font dictionary available here as a convenient json file:
https://gist.github.com/jamesacampbell/f3612d454268f105faf34aef56499bb2 

And if you are interested there is a pigpen cipher display for an HTML page in my codepen here:
https://codepen.io/jamesacampbell/full/OjWvoR

for instance ```"a" = "_|" and "b" = "|_|".```

and also available included in this repo as jsondata.json

# pypigpen
Pigpen cipher encipher and decipher in python 3.

## Description

Creates a plaintext file called cipher.txt in the same directory you execute the script that includes your enciphered text. See the example below. Use ```decipher.py [name of .txt]``` to decipher.

## Example

```
Welcome.
This will print a cipher to a text file called cipher.txt.
Use decipher.py to reverse.
What do you want to encipher? (use . for new line):
I like big butts. And I cannot lie.

Output:
|-   |._|-|._|[]   |_||--|   |_|<>>v

   _|[.]]   |-   |__|[.][.][.>   |._|-[]
   
```
Thanks to http://ascii.co.uk/art/pig hjw for the pig ascii art.
