"""
Usando otro bucle, comprobar de entre los números del 1 al 100 son cuántos son
divisibles por 2 pero no por 4 
"""

contador = 0

for i in range(10):
    if (i + 1) % 4 == 2:
         contador += 1 # contador = contador + 1        
           
print(contador)