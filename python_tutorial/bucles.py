"""
Usando un bucle (for o while), sumar todos los n�mmeros del 1 al 100 e imprimir
el resultado

acum = 0
for i in range(5**2 + 1):
    acum = acum + i
print(acum)

n = 5**2
suma_gaussiana = n*(n+1)//2
print(suma_gaussiana)
"""
#While loop

i = 1
while i <= 10:
    print(i)
    i += 1

print('Done with loop')

#For loop

for letter in ('Giraffe Academy'):
    print(letter)

friends = ['Jim', 'Kevin', 'Karen']
for friends in friends:
    print(friends)

for index in range(3, 10):
    print(index)

friends = ['Jim', 'Kevin', 'Karen']
for index in range(len(friends)):
    print(friends[index])

friends = ['Jim', 'Kevin', 'Karen']
for index in range(5):
    if index == 0:
        print('First iteration')
    else:
        print('Not first')
