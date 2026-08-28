
shape = input('Enter a shape (Triangle, square, rectangle):\n').lower()
match shape:
    case 'triangle':
        print('   /|')
        print('  / |')
        print(' /  |')
        print('/___|')
    case 'square':
        print('|‾‾‾|')
        print('|___|')
    case 'rectangle':
        print('|‾‾‾|')
        print('|   |')
        print('|   |')
        print('|___|')
    case other:
        print('\nInvalid shape')
