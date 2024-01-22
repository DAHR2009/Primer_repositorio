import random

elements = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lon = int(input('Escribe la longitud de la contraseña'))

password = ''

for i in range(lon):
    password += random.choice(elements)

print(password) 
