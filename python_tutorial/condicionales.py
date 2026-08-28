"""
Usando los condicionales, crear un programa que imprima por pantalla si un número
es par o no. (Si es par es divisible entre 2)
'El n�mero _ es par' / 'El n�mero _ es impar'

num = 5

if num % 2 == 0:
    print('El', num,'es par')
else:
    print('El', num, 'es impar')
"""

is_male = bool(input('Enter if you are a male: '))
is_tall = bool(input('Enter if you are tall: '))


if is_male and is_tall:
    print('You are a tall male')
elif is_male and not(is_tall):
    print('You are a short male')
elif not(is_male) and is_tall:
    print('You are not a male but are tall')
else:
    print('You are not a male and not tall')
