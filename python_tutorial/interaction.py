Alice = input('').lower()

match Alice:
    case 'hello':
        print('Hello to you too.')
    case 'what´s your name?':
        print('My name is Bob')
    case 'goodbye':
        print('See you later.')
    case other:
        print('Goodbye World.')
