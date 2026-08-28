"""
Usando indices, a partir la cadena de caracteres: abecedario, que contiene
el abecedario, crear una variable llamada vocales que tenga solo las vocales.
"""
abecedario = 'abcdefghijklmnñopqrstuvwxyz'
vocales = abecedario[0] + abecedario[4] + abecedario[8] + abecedario[15] 
vocales = vocales + abecedario[21]


consonates = abecedario[2]+abecedario[3]+abecedario[5]+abecedario[3]+abecedario[6]+abecedario[7]+abecedario[9]+abecedario[10]+abecedario[11]+abecedario[12]+abecedario[13]+abecedario[14]+abecedario[16]+abecedario[17]+abecedario[18]+abecedario[19]+abecedario[20]+abecedario[22]+abecedario[23]+abecedario[24]+abecedario[25]+abecedario[26]
print('Vocales:', vocales, '\nConsonantes:', consonates)
