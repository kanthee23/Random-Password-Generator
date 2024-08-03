"""
Random Password Generator
-------------------------
Python script to generate a random password of 8 characters. Each time the program is run, a new password will be generated randomly. The passwords generated will be 8 characters long and will have to include the following characters in any order:

Uppercase letters from A to Z, - 1 Min
Lowercase letters from a to z, - 1 Min
Digits from 0 to 9,            - 1 Min
signs such as !, ?, “, # etc.  - 1 Min

"""

import random
# first 4 symbol define for maintain minum number of chractors
password_charactor = ['u','l','d','s']
# store password charactors
password = []

# Create 8 symbols for password charactors
while len(password_charactor) < 8:
    num =  random.randint(1,4)
    if num == 1:
        password_charactor.append('u')
    elif num == 2:
        password_charactor.append('l')
    elif num == 3:
        password_charactor.append('d')
    elif num == 4:
        password_charactor.append('s')
    else:
        pass

# covert symbol to charactors
for symbol in password_charactor:
    if symbol == 'u':
        num = random.randint(65,90)
        password.append(chr(num))
    elif symbol == 'l':
        num = random.randint(97,122)
        password.append(chr(num))
    elif symbol == 'd':
        num = random.randint(48, 57)
        password.append(chr(num))
    elif symbol == 's':
        sym_askii = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,123,124,125,126]
        num = random.randint(0, len(sym_askii)-1)
        password.append(chr(sym_askii[num]))

# Shuffle a list
random.shuffle(password)
# coverto to string and print
print(''.join(password))
