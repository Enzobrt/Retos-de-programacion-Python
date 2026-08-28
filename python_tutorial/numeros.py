from math import math  # nos da acceso a más funciones

my_num = -5
print(str(my_num) + ' is my favorite number')  # lo transforma en un string.
print(abs(my_num))  # lo trensforma en un valor absoluto.
print(pow(2, 2))  # sirve para elevar.
print(max(5, 9))  # comprueba cual es mayor
print(min(2, 1))  # comproueba cual es menor
print(round(3.2))  # aproxima el valor

print(math.floor(3.7))  # coge el más bajo
print(math.ceil(3.7))  # coge el más alto
print(math.sqrt(36))  # hace la raíz cuadrada del número

"""
# Compare
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 4, 5))

# Raise to the power
def raise_to_power(base_num, pow_num):
    ""
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))
"""
