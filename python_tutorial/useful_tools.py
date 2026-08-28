import random

feet_in_mile = 5280
meters_in_kilometer = 1000
# Crear función que transforme una unidad a otra

beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Star']


def get_file_ext(filename):
    return filename[filename.index('.')+1:]
# Obtiene la extension de un archivo


def roll_dice(num):
    return random.randint(1, num)
# Simula tirar un dado de n caras
