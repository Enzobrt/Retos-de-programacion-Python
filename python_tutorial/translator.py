"""
Giraffe Language
vowels -> g
-------------
dog -> dgt
cat -> cgt
"""


def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += letter
    return translation


print(translate(input('This translator translates to Giraffe Language\n\nEnter a phrase: ')))
