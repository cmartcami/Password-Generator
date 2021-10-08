


#Generador de contraseñas.

import random

length = input('ingrese cantidad de caracteres que desea: ')

lower = 'abcdefghijklmnopqrstuvwxyz'

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = '1234567890'

symbols = '[]{}()*;/'

all = lower + upper + numbers + symbols


password = ''.join(random.sample(all, int(length)))

print(password)

