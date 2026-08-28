
# La serie de fibonacci es una secuencia de números que se obtiene sumando los
# números anteriores
"""
1,1,2,3,5,8,13...
"""
# Implementa una función que imprima la serie de fibonacci hasta el elemento n.


def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    print(n)


if __name__ == '__main':
    fibonacci(0)
    fibonacci(1)
    fibonacci(2)
    fibonacci(3)
