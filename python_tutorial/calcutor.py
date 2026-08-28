try:
    def calculator(num1, op, num2):
        result = 0
        match op:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '/':
                result = num1 / num2
            case '*':
                result = num1 * num2
            case '**':
                result = num1 ** num2
        return result


    num1 = float(input('Enter first number: '))
    op = input('Enter operator: ')
    num2 = float(input('Enter second number: '))
    print(calculator(num1, op, num2))

except ValueError:
    print('Please enter a number')
except ZeroDivisionError:
    print('Cannot divide by zero')
