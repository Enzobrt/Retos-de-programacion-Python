"""
#Read
open('dictionaries.py', 'r')

#Write
open('dictionaries.py', 'w')

#Apend
open('dictionaries.py', 'a')

#Read and write
open('dictionaries.py', 'r+')
"""
# Reading files
file = open('prueba.py', 'r')
print(file.readeable())
print(file.read())
print(file.readline()[0])


file.close()
